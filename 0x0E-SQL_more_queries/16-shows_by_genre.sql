-- 16-shows_by_genre.sql
-- SQL query lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_genres.name FROM tv_shows
	INNER JOIN tv_show_genres
	ON tv_show_genres.show_id = tv_shows.id
	INNER JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id
	ORDER BY title, name;
