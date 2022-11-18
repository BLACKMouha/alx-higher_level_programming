-- 8-cities_of_california_subquery.sql
-- SQL query that lists all cities of California than can be found
SELECT cities.id, cities.name FROM cities
	WHERE cities.state_id = (
		SELECT states.id FROM states WHERE states.name = "California"
	)
	ORDER BY cities.id
;
