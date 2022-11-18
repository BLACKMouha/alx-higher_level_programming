-- 6-states.sql
-- SQL query that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- SQL query that creates the table hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id)
);
