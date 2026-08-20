#!/usr/bin/env node
/**
 * jules-prompts as an MCP server.
 *
 * WHY THIS EXISTS. The library is currently copy-paste: a person finds it, opens a file,
 * selects the text, and pastes it into an agent. That works once. MCP prompts are surfaced as
 * slash commands by Claude Code, Claude Desktop, VS Code/Copilot, Windsurf and Zed, so the
 * same library becomes something installed rather than something visited, and it stays current
 * because this reads the live repository rather than a bundled copy.
 *
 * WHY IT FETCHES INSTEAD OF BUNDLING. A bundled snapshot is a second copy of the truth, and a
 * second copy is a thing that will disagree with the first and then be trusted anyway. The
 * index and the bodies are read from the repository at startup, so a prompt merged an hour ago
 * is available without anyone republishing anything.
 *
 * WHAT IT DOES THAT COPY-PASTE DOES NOT. Several prompts carry placeholders such as
 * <PR_URL_OR_DIFF_RANGE>. Those are discovered per prompt and exposed as MCP arguments, so the
 * client can ask for them and this substitutes before handing the text over. That is the part
 * a webpage cannot do.
 *
 * FAILURE IS LOUD, DELIBERATELY. If the fetch fails this exits non-zero with the reason rather
 * than starting and serving an empty list. A server that connects and offers nothing looks
 * identical to a client misconfiguration, and the person debugging it would have no way to
 * tell which they were looking at.
 */
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const REPO = process.env.JULES_PROMPTS_REPO || "melbinjp/jules-prompts";
const REF = process.env.JULES_PROMPTS_REF || "main";
const RAW = `https://raw.githubusercontent.com/${REPO}/${REF}`;
const INDEX = process.env.JULES_PROMPTS_INDEX ||
  "https://jules-prompts.wecanuseai.com/prompts.json";

const PLACEHOLDER = /<([A-Z][A-Z0-9_]*)>/g;

async function getJson(url) {
  const r = await fetch(url, { headers: { "User-Agent": "jules-prompts-mcp" } });
  if (!r.ok) throw new Error(`${url} returned ${r.status}`);
  return r.json();
}

async function getText(url) {
  const r = await fetch(url, { headers: { "User-Agent": "jules-prompts-mcp" } });
  if (!r.ok) throw new Error(`${url} returned ${r.status}`);
  return r.text();
}

/** Split YAML front matter from the prompt body. The body is what an agent is given; the
 *  front matter is metadata for the website and would only confuse it. */
function splitFrontMatter(text) {
  if (!text.startsWith("---")) return { meta: {}, body: text };
  const end = text.indexOf("\n---", 3);
  if (end === -1) return { meta: {}, body: text };
  const block = text.slice(3, end);
  const meta = {};
  for (const line of block.split("\n")) {
    const at = line.indexOf(":");
    if (at > 0) meta[line.slice(0, at).trim()] = line.slice(at + 1).trim();
  }
  return { meta, body: text.slice(end + 4).replace(/^\n+/, "") };
}

function placeholdersIn(body) {
  return [...new Set([...body.matchAll(PLACEHOLDER)].map((m) => m[1]))];
}

async function main() {
  const index = await getJson(INDEX);
  const entries = index.prompts || [];
  if (entries.length === 0) throw new Error(`${INDEX} listed no prompts`);

  const loaded = await Promise.all(
    entries.map(async (p) => {
      const text = await getText(`${RAW}/${p.source_path}`);
      const { body } = splitFrontMatter(text);
      return { ...p, body, args: placeholdersIn(body) };
    }),
  );

  const server = new McpServer({ name: "jules-prompts", version: index.version || "1.0.0" });

  for (const p of loaded) {
    const argsSchema = {};
    for (const a of p.args) {
      argsSchema[a] = z.string().optional().describe(`Value for <${a}>`);
    }
    server.registerPrompt(
      p.slug,
      {
        title: p.title,
        description: p.category ? `[${p.category}] ${p.description}` : p.description,
        argsSchema,
      },
      (args) => {
        let text = p.body;
        for (const [k, v] of Object.entries(args || {})) {
          if (v) text = text.split(`<${k}>`).join(v);
        }
        return { messages: [{ role: "user", content: { type: "text", text } }] };
      },
    );
  }

  // Coverage on stderr, where it does not corrupt the stdio protocol. A server that says how
  // many prompts it loaded can be told apart from one that loaded none and connected anyway.
  const withArgs = loaded.filter((p) => p.args.length).length;
  process.stderr.write(
    `jules-prompts: ${loaded.length} prompt(s) from ${REPO}@${REF}, ` +
      `${withArgs} with fillable placeholders, ` +
      `categories: ${(index.categories || []).join(", ")}\n`,
  );

  await server.connect(new StdioServerTransport());
}

main().catch((e) => {
  process.stderr.write(`jules-prompts: failed to start: ${e.message}\n`);
  process.exit(1);
});
