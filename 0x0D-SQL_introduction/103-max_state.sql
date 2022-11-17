-- 103-max_state.sql
-- SQL displays the max temperature of each state (ordered by State name).
SELECT state, MAX(value) AS max_temp FROM temperatures
	GROUP BY state
	ORDER BY state ASC;
