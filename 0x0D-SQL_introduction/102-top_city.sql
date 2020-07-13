-- script that displays the top 3 of cities temperature during July and August ordered by temperature
-- QUERY
SELECT city, avg(value) as avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP by city
ORDER BY avg_temp DESC
LIMIT 3;
