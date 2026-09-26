BEGIN;
DROP INDEX orders_customer_idx;
ALTER TABLE users DROP CONSTRAINT users_email_key;
COMMIT;
