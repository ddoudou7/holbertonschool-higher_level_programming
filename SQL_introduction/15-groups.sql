-- 15-groups.sql
-- Lists each score with the count of rows having that score, ordered by count DESC
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
