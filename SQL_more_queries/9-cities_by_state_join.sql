-- 9-cities_by_state_join.sql
-- Lists id, city name and state name ordered by cities.id

SELECT cities.id,
       cities.name,
       states.name
FROM   cities
JOIN   states ON states.id = cities.state_id
ORDER  BY cities.id;
