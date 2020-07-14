-- script that creates the table unique_id on your MySQL server.
-- QUERY
CREATE TABLE IF NOT EXISTS `unique_id` (id INT DEFAULT 1,
name VARCHAR(256),
PRIMARY KEY(id));
