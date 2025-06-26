-- 11-best_score.sql
-- Lists score then name of rows whose score >= 10, ordered by score DESC
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
