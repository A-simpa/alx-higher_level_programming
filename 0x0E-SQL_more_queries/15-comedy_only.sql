-- lists all comedy shows contained in hbtn_0d_tvshows
SELECT title
FROM tv_shows
INNER JOIN
	(tv_genres
	INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id)
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = "Comedy"
ORDER BY title ASC;
