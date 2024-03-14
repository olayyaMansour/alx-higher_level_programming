-- 8. Cities of California
-- Script to list all the cities of California from the database hbtn_0d_usa

SELECT cities.id, cities.name
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California'
ORDER BY cities.id;
