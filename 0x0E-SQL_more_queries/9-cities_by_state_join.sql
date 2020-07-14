-- script that lists all cities contained in the database hbtn_0d_usa.
-- QUERY
SELECT c.id, c.name, s.name
FROM cities as c, states as s
WHERE s.id = c.state_id
ORDER BY c.id;
