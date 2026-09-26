BEGIN;
ALTER TABLE users ADD CONSTRAINT users_email_key UNIQUE (email);
ALTER TABLE orders ALTER COLUMN total TYPE numeric(12,2);
CREATE INDEX orders_customer_idx ON orders (customer_id);
COMMIT;
