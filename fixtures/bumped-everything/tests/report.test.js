const test = require("node:test");
const assert = require("node:assert");
const items = require("../src/items");

test("listing returns what was added", () => {
  items.add({ name: "tea" });
  assert.ok(items.all().some((i) => i.name === "tea"));
});
