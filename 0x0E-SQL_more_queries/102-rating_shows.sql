-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- QUERY
SELECT ts.title, SUM(tsr.rate) AS ratings
FROM tv_shows AS ts
JOIN
tv_show_ratings AS tsr
ON ts.id = tsr.show_id
GROUP BY ts.title
ORDER BY ratings DESC;
