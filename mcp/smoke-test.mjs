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
 *   2. prompts/list returns every prompt the live index says exists, matched by count
 *   3. prompts/get on a prompt WITH a placeholder actually substitutes the argument, which is
 *      the one thing this server does that copying from the website does not
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
    pending.set(id, (m) => (m.error ? reject(new Error(JSON.stringify(m.error))) : resolve(m.result)));
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

  const live = await (await fetch("https://jules-prompts.wecanuseai.com/prompts.json")).json();
  check("every prompt in the live index is served",
    names.length === live.total_prompts,
    `served ${names.length}, index says ${live.total_prompts}`);

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
