-- SQL script that lists all the cities of California tha can be found in the database hbtn_0d_usa
-- states table contains only record where name = California
-- Result must be sorted in ascending order by cities.id

SELECT cities.id, cities.name FROM cities
  WHERE state_id = (SELECT id FROM states WHERE states.name = "California")
  ORDER BY cities.id;
