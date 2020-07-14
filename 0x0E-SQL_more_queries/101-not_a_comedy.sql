-- script that lists all shows without the genre Comedy in the database
-- QUERY
SELECT DISTINCT ts.title
FROM tv_shows AS ts 
LEFT JOIN 
tv_show_genres AS tsg
ON ts.id = tsg.genre_id
LEFT JOIN
tv_genres AS tg
ON tg.id = tsg.genre_id 
WHERE ts.title not IN
(SELECT ts.title 
FROM tv_shows AS ts 
JOIN 
tv_show_genres AS tsg
ON ts.id = tsg.show_id 
JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
WHERE tg.name = "Comedy")
ORDER BY ts.title;
