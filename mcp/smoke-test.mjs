#!/usr/bin/env node
/**
 * Speak real MCP to the server over stdio and check what comes back.
 *
 * This exists because "the code looks right" is not evidence. An MCP server that starts,
 * connects, and offers an empty prompt list is indistinguishable from a working one until a
 * client tries to use it, and by then the person debugging is a stranger.
 *
 * It asserts what a broken server would fail:
 *   1. it initializes and DECLARES the prompts and resources capabilities, which is what makes
 *      clients show slash commands and files at all
 *   2. prompts/list returns every file the index at the same ref says exists, by name, and
 *      includes `conductor`
 *   3. prompts/get on `conductor` returns SKILL.md without its front matter, and on a guidance
 *      file returns that file's text, byte for byte as the source has it
 *   4. resources/list and resources/read serve the same files
 *   5. a prompt that is not in the index is refused
 *
 * If the server dies before answering, this says so at once, with the server's own reason.
 * It used to wait out a 60-second timeout and report "initialize timed out", which hid the
 * cause (a 403 from the index host) behind a symptom.
 *
 * JULES_PROMPTS_REF chooses the commit both sides read. CI sets it to the commit under test.
 * JULES_PROMPTS_DIR runs the server from a copy on disk instead, and then this test reads the
 * index and the expected text from the same copy and checks the server said it used no network.
 */
import { spawn } from "node:child_process";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const here = path.dirname(fileURLToPath(import.meta.url));
const child = spawn(process.execPath, [path.join(here, "index.js")], {
  stdio: ["pipe", "pipe", "pipe"],
});

let stderr = "";
child.stderr.on("data", (d) => (stderr += d.toString()));

// A request the server can no longer answer fails now, with the server's reason.
let exited = null;
child.on("exit", (code) => {
  exited = `server exited with code ${code}: ${stderr.trim() || "no output"}`;
  for (const [, settle] of pending) settle({ error: exited });
  pending.clear();
});

const pending = new Map();
let buf = "";
child.stdout.on("data", (d) => {
  buf += d.toString();
  let nl;
  while ((nl = buf.indexOf("\n")) !== -1) {
    const line = buf.slice(0, nl).trim();
    buf = buf.slice(nl + 1);
    if (!line) continue;
    const msg = JSON.parse(line);
    if (msg.id !== undefined && pending.has(msg.id)) {
      pending.get(msg.id)(msg);
      pending.delete(msg.id);
    }
  }
});

let nextId = 1;
function send(method, params) {
  const id = nextId++;
  return new Promise((resolve, reject) => {
    if (exited) return reject(new Error(exited));
    pending.set(id, (m) => (m.error ? reject(new Error(typeof m.error === "string" ? m.error : JSON.stringify(m.error))) : resolve(m.result)));
    child.stdin.write(JSON.stringify({ jsonrpc: "2.0", id, method, params }) + "\n");
    setTimeout(() => reject(new Error(`${method} timed out`)), 60000);
  });
}
function notify(method, params) {
  child.stdin.write(JSON.stringify({ jsonrpc: "2.0", method, params }) + "\n");
}

let failures = 0;
function check(label, ok, detail) {
  if (!ok) failures++;
  console.log(`[${ok ? "PASS" : "FAIL"}] ${label}${detail ? " - " + detail : ""}`);
}

try {
  const init = await send("initialize", {
    protocolVersion: "2025-06-18",
    capabilities: {},
    clientInfo: { name: "smoke-test", version: "1.0.0" },
  });
  notify("notifications/initialized", {});

  check("server declares the prompts capability",
    Boolean(init.capabilities && init.capabilities.prompts),
    `capabilities: ${Object.keys(init.capabilities || {}).join(", ") || "none"}`);

  check("server declares the resources capability",
    Boolean(init.capabilities && init.capabilities.resources),
    `capabilities: ${Object.keys(init.capabilities || {}).join(", ") || "none"}`);

  const listed = await send("prompts/list", {});
  const names = (listed.prompts || []).map((p) => p.name);

  const local = process.env.JULES_PROMPTS_DIR;
  const repo = process.env.JULES_PROMPTS_REPO || "melbinjp/jules-prompts";
  const ref = process.env.JULES_PROMPTS_REF || "main";
  const raw = `https://raw.githubusercontent.com/${repo}/${ref}`;
  const library = local
    ? JSON.parse(readFileSync(path.join(local, "library.json"), "utf8"))
    : await (await fetch(`${raw}/library.json`)).json();
  const where = local ? `${local}/library.json` : `${repo}@${ref} library.json`;
  const expected = library.files.map((f) => f.name);
  check("every file in the index is served as a prompt",
    names.length === expected.length && expected.every((n) => names.includes(n)),
    `served ${names.length}, ${where} lists ${expected.length}`);
  check("the conductor itself is a prompt", names.includes("conductor"), names.slice(0, 3).join(", ") + ", ...");
  if (local) {
    check("the local copy was served with no network",
      stderr.includes("(local copy, no network)"),
      stderr.trim().split("\n")[0] || "nothing on stderr");
  }

  // The text the server should give for a file: the source, with SKILL.md's front matter removed.
  async function source(file) {
    const text = local
      ? readFileSync(path.join(local, file.path), "utf8")
      : await (await fetch(`${raw}/${file.path}`)).text();
    if (!text.startsWith("---")) return text;
    return text.slice(text.indexOf("\n---", 3) + 4).replace(/^\n+/, "");
  }
  const promptText = async (name) => {
    const got = await send("prompts/get", { name });
    return got.messages.map((m) => m.content.text).join("\n");
  };

  const entry = library.files.find((f) => f.name === "conductor");
  const entryText = await promptText("conductor");
  check("the conductor prompt is SKILL.md without its front matter",
    entryText === (await source(entry)) && !entryText.startsWith("---") && entryText.length > 2000,
    `${entryText.length} chars, starts: ${JSON.stringify(entryText.slice(0, 40))}`);

  const others = library.files.filter((f) => f.name !== "conductor");
  const different = [];
  for (const f of others) {
    if ((await promptText(f.name)) !== (await source(f))) different.push(f.name);
  }
  check("every guidance and template prompt is its file, unchanged",
    others.length > 0 && different.length === 0,
    different.length ? `differ: ${different.join(", ")}` : `${others.length} files match`);

  const resources = (await send("resources/list", {})).resources || [];
  check("every file in the index is also a resource",
    resources.length === expected.length && resources.some((r) => r.uri === "conductor://SKILL.md"),
    `${resources.length} resources, first: ${resources[0] && resources[0].uri}`);
  const guidance = library.files.find((f) => f.kind === "guidance");
  const uri = `conductor://${guidance.path.replace(/^conductor\//, "")}`;
  const read = await send("resources/read", { uri });
  check("a resource read returns the file's text",
    read.contents[0].text === (await source(guidance)),
    `${uri}: ${read.contents[0].text.length} chars`);

  let refused = false;
  try {
    await send("prompts/get", { name: "not-in-the-index" });
  } catch {
    refused = true;
  }
  check("a prompt that is not in the index is refused", refused);

  check("the server reported its coverage on stderr",
    /\d+ file\(s\) of the conductor from /.test(stderr),
    stderr.trim().split("\n")[0] || "nothing on stderr");
} catch (e) {
  console.log(`[FAIL] threw: ${e.message}`);
  failures++;
} finally {
  child.kill();
}

console.log(failures === 0 ? "\nMCP SERVER WORKS" : `\n${failures} check(s) failed`);
process.exit(failures === 0 ? 0 : 1);
