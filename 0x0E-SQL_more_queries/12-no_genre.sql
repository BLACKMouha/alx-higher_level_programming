SELECT tv_shows.title, tv_show_genres.genre_id
	FROM tv_shows
	LEFT OUTER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.id NOT IN (SELECT DISTINCT tv_show_genres.show_id FROM tv_show_genres)
	ORDER BY tv_shows.title, tv_show_genres.genre_id;
