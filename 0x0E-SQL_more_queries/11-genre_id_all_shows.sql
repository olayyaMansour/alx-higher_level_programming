-- 11. Genre ID for all shows
-- Script to list all shows contained in the database hbtn_0d_tvshows with their genre IDs

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
