-- SQL script that lists all Comedy shows in the database hbtn_0d_tvshows
-- the tv_genres table contains only one record where name = Comedy
-- Results must be sorted by tv_shows.title
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name  = 'Comedy'
ORDER BY tv_shows.title;
