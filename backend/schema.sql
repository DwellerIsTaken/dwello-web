BEGIN;

CREATE TABLE IF NOT EXISTS client_data(
  username TEXT,
  email TEXT PRIMARY KEY,
  password TEXT,
  birth_date DATE
);

COMMIT;