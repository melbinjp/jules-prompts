CREATE TABLE orders (
    id          bigserial PRIMARY KEY,
    customer_id bigint NOT NULL REFERENCES users (id),
    total       double precision NOT NULL,
    placed_at   timestamptz NOT NULL DEFAULT now()
);
