-- 8-cities_of_california_subquery.sql
-- SQL query that lists all cities of California than can be found
SELECT id, name FROM cities
	WHERE id = (
		SELECT id FROM states WHERE name = "California"
	)
;
