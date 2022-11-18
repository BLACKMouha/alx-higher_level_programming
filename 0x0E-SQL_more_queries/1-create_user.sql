-- 1-create_user.sql
-- SQL query that creates the MySQL user 'user_0d_1'.
CREATE USER IF NOT EXISTS
	'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT PRIVILEGE ON *.* TO 'user_Od_1'@'localhost';
