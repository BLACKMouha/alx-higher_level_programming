-- SQL script that creates the table id_not_null
-- table name: id_not_null
-- columns:
--      id: INT NOT NULL DEFAULT=1
--      name: VARCHAR=256
CREATE TABLE IF NOT EXISTS id_not_null(
  id INT DEFAULT 1,
  name VARCHAR(256)
);
