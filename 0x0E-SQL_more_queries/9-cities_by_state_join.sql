-- SQL script that lists all cities
-- each record should display cities.id, cities.name, states.name
SELECT cities.id, cities.name, states.name FROM cities
  LEFT JOIN states ON states.id = cities.state_id;
