-- 15-groups.sql
-- SQL query that lists the number of occurences of all scores
SELECT score, COUNT(*) AS number
	FROM second_table
	GROUP BY score
	ORDER BY number DESC;
