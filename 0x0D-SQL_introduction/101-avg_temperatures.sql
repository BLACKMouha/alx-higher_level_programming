-- 101-avg_temperatures.sql
-- SQL query that computes the average temperature b city ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
