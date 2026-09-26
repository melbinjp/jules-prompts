const _ = require("lodash");

const store = new Map();

module.exports = {
  all: () => [...store.values()],
  add: (item) => {
    const merged = _.merge({ id: String(store.size + 1), quantity: 0 }, item);
    store.set(merged.id, merged);
    return merged;
  },
  remove: (id) => store.delete(id),
};
