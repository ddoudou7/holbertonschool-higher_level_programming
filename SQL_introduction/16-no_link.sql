-- 16-no_link.sql
-- Lists score and name where name is not NULL/empty, ordered by score DESC
SELECT score, name
FROM   second_table
WHERE  name IS NOT NULL
  AND  name <> ''
ORDER  BY score DESC;
