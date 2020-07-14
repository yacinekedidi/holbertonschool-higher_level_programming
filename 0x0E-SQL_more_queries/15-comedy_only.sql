-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- QUERY
SELECT ts.title
FROM tv_shows AS ts, tv_show_genres AS tsg, tv_genres AS tg
WHERE tg.id = tsg.genre_id AND tg.name = "Comedy" AND tsg.show_id = ts.id
ORDER BY ts.title;
