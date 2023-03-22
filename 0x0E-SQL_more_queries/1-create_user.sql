-- SQL script that creates a user:
-- name: user_0d_1
-- privileges: all
-- databases: all
-- tables: all
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
