CREATE TABLE IF NOT EXISTS transactions (
    transaction_id TEXT PRIMARY KEY,
    city TEXT,
    amount FLOAT,
    merchant TEXT,
    account_id BIGINT,
    transaction_date DATE,
    transaction_time TIME
);
