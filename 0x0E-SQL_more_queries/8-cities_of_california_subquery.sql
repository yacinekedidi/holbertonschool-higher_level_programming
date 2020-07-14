-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- QUERY
SELECT c.id, c.name
FROM states as s, cities as c
WHERE s.id = c.state_id AND s.name = "California"
ORDER BY c.id;
