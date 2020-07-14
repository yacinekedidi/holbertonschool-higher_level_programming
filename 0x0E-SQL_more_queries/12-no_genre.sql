-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- query
SELECT ts.title, tsg.genre_id 
FROM tv_shows AS ts 
LEFT JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
WHERE tsg.show_id IS NULL
ORDER BY ts.title, tsg.genre_id;
