-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- QUERY
SELECT DISTINCT tg.name
FROM tv_shows AS ts, tv_show_genres AS tsg, tv_genres AS tg
WHERE ts.id = tsg.show_id AND tsg.genre_id = tg.id AND tg.name NOT IN 
(SELECT tg.name FROM tv_shows AS ts, tv_show_genres AS tsg, tv_genres AS tg
WHERE ts.id = tsg.show_id AND tsg.genre_id = tg.id AND ts.title = "Dexter")
ORDER BY tg.name;
