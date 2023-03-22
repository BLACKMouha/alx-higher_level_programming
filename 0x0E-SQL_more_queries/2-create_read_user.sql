-- SQL script that creates a database with its user:
-- database:
--      name: hbtn_0d_2
-- user:
--      name: user_0d_2
--      databases: hbtn_0d_2
--      privileges: SELECT
--      password: user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
