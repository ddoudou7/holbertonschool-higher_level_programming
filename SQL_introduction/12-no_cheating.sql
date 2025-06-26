-- 12-no_cheating.sql
-- Updates Bob's score to 10 without referencing his id
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
