-- SQL script that creates the database hbtn_0d_usa and its table cities
-- db:
--  name: hbtn_0d_usa
--  tables:
--      cities:
--          id: INT, UNIQUE, NOT NULL, PRIMARY KEY, AUTO GENERATED
--          state_id: INT, NOT NULL FOREIGN KEY TO states[id]
--          name: VARCHAR=256 NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
  id INT AUTO_INCREMENT NOT NULL,
  state_id INT, NOT NULL,
  name VARCHAR(256), NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY (state_id) REFERENCES states(id)
);
