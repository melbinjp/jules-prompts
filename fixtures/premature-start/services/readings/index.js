// readings-service: takes readings from GrowCloud and writes them to Postgres.
const growcloud = require("growcloud-sdk");
const { Pool } = require("pg");

const db = new Pool();
const client = growcloud.connect({ apiKey: process.env.GROWCLOUD_KEY, plan: "free" });

client.on("reading", async (r) => {
  await db.query(
    "INSERT INTO readings (growcloud_device_id, moisture, at) VALUES ($1, $2, $3)",
    [r.growcloudDeviceId, r.value, r.timestamp],
  );
});
