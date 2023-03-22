-- SQL script that creates a database hbtn_0d_usa and its table states
-- dbname: hbtn_0d_usa
--      tables:
--          name: states
--              columns:
--                  id: INT, UNIQUE, AUTO_GENERATED, NOT NULL, PRIMARY KEY
--                  name: VARCHAR=256, NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
  id INT AUTO_INCREMENT NOT NULL,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY(id)
);
