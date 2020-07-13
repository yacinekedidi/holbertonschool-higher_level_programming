-- script that displays the average temperature (Fahrenheit) by city ordered by temperature
-- QUERY
SELECT city, avg(value) as avg_temp 
FROM temperatures
GROUP BY city
ORDER BY avg(value) DESC;
