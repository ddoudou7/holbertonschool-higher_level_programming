-- 5-unique_id.sql
-- Creates table unique_id with id DEFAULT 1 and UNIQUE

CREATE TABLE IF NOT EXISTS unique_id (
  id   INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);
