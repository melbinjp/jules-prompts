const test = require("node:test");
const assert = require("node:assert");
const items = require("../src/items");

test("adding an item fills in its defaults", () => {
  const item = items.add({ name: "jam", quantity: 3 });
  assert.equal(item.quantity, 3);
  assert.equal(item.name, "jam");
});
