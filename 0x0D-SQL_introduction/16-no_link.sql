-- 16-no_link.sql
-- SQL query that list all records with non-empty name and ordered by score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;	
