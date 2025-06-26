-- 8-cities_of_california_subquery.sql
-- Lists all cities of California, ordered by cities.id ASC (no JOIN)

SELECT id, name
FROM   cities
WHERE  state_id = (
    SELECT id FROM states WHERE name = 'California' LIMIT 1
)
ORDER  BY id;
