-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- QUERY
SELECT tg.name
FROM tv_genres AS tg, tv_show_genres AS tsg, tv_shows AS ts
WHERE tg.id = tsg.genre_id AND ts.title = "Dexter" AND tsg.show_id = ts.id
ORDER BY tg.name;
