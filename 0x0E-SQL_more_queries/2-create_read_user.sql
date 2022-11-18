-- 2-create_read_user.sql
-- SQL query that creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- SQL query that creates the MySQL user hbtn_0d_2
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- SQL query that grants privileges to user_0d_2 on the database hbtn_0d_2
GRANT ALL PRIVILEGES ON hbtn_0d_2.* TO user_0d_2@localhost;
