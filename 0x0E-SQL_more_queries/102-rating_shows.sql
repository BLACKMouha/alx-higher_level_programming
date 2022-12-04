-- 102-rating_shows.sql
-- SQL query that lists all shows by their rating
SELECT title,
	SUM(rate) AS rating
	FROM tv_shows
	LEFT JOIN tv_show_ratings
	ON tv_shows.id = tv_show_ratings.show_id
	GROUP BY title
	ORDER BY rating DESC;
