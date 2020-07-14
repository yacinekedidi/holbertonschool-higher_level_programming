-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- QUERY
SELECT tg.name as genre, count(tsg.show_id) AS number_of_shows 
FROM tv_genres AS tg JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
GROUP BY tg.name
ORDER BY number_of_shows DESC;
