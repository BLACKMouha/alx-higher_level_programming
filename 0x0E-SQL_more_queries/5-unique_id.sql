-- SQL scripts that creates the table unique_id
-- table name: unique_id
-- columns:
--      id: INT DEFAULT=1 UNIQUE
--      name: VARCHAR=256
CREATE TABLE IF NOT EXISTS unique_id(
  id INT UNIQUE DEFAULT 1,
  name VARCHAR(256)
  );
