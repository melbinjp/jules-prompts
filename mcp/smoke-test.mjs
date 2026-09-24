#!/usr/bin/env node
/**
 * Speak real MCP to the server over stdio and check what comes back.
 *
 * This exists because "the code looks right" is not evidence. An MCP server that starts,
 * connects, and offers an empty prompt list is indistinguishable from a working one until a
 * client tries to use it, and by then the person debugging is a stranger.
 *
 * It asserts three things a broken server would fail:
 *   1. it initializes and DECLARES the prompts capability, which is what makes clients show
 *      slash commands at all
 *   2. prompts/list returns every procedure the index at the same ref says exists, by count
 *   3. prompts/get on a prompt WITH a placeholder actually substitutes the argument, which is
 *      the one thing this server does that copying from the website does not
 *
 * If the server dies before answering, this says so at once, with the server's own reason.
 * It used to wait out a 60-second timeout and report "initialize timed out", which hid the
 * cause (a 403 from the index host) behind a symptom.
 *
 * JULES_PROMPTS_REF chooses the commit both sides read. CI sets it to the commit under test.
 */
import { spawn } from "node:child_process";
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

  const listed = await send("prompts/list", {});
  const names = (listed.prompts || []).map((p) => p.name);

  const repo = process.env.JULES_PROMPTS_REPO || "melbinjp/jules-prompts";
  const ref = process.env.JULES_PROMPTS_REF || "main";
  const library = await (await fetch(`https://raw.githubusercontent.com/${repo}/${ref}/library.json`)).json();
  check("every procedure in the index is served",
    names.length === library.procedures.length,
    `served ${names.length}, ${repo}@${ref} library.json lists ${library.procedures.length}`);

  const withArgs = (listed.prompts || []).find((p) => (p.arguments || []).length > 0);
  check("at least one prompt exposes a fillable placeholder",
    Boolean(withArgs),
    withArgs ? `${withArgs.name} takes ${withArgs.arguments.map((a) => a.name).join(", ")}` : "none found");

  if (withArgs) {
    const argName = withArgs.arguments[0].name;
    const sentinel = "SENTINEL-VALUE-12345";
    const got = await send("prompts/get", {
      name: withArgs.name,
      arguments: { [argName]: sentinel },
    });
    const text = got.messages.map((m) => m.content.text).join("\n");
    check("the argument is actually substituted into the body",
      text.includes(sentinel) && !text.includes(`<${argName}>`),
      `sentinel present: ${text.includes(sentinel)}, placeholder gone: ${!text.includes(`<${argName}>`)}`);
    check("the body is the prompt, not the front matter",
      !text.startsWith("---") && text.length > 200,
      `${text.length} chars, starts: ${JSON.stringify(text.slice(0, 40))}`);
  }

  check("the server reported its coverage on stderr",
    /\d+ prompt\(s\) from /.test(stderr),
    stderr.trim().split("\n")[0] || "nothing on stderr");
} catch (e) {
  console.log(`[FAIL] threw: ${e.message}`);
  failures++;
} finally {
  child.kill();
}

console.log(failures === 0 ? "\nMCP SERVER WORKS" : `\n${failures} check(s) failed`);
process.exit(failures === 0 ? 0 : 1);
