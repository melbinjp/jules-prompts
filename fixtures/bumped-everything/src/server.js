const express = require("express");
const { format } = require("date-fns");
const items = require("./items");

const app = express();
app.use(express.json());

app.get("/api/items", (req, res) => res.json(items.all()));
app.post("/api/items", (req, res) => res.status(201).json(items.add(req.body)));
app.del("/api/items/:id", (req, res) => {
  items.remove(req.params.id);
  res.sendStatus(204);
});
app.get("/api/report", (req, res) => res.json({ on: format(new Date(), "yyyy-MM-dd"), count: items.all().length }));

module.exports = app;
