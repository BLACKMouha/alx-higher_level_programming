-- 100-move_to_utf8.sql
-- SQL query that converts a database to UTF-8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;

-- SQL query that converts a table to UTF-8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
