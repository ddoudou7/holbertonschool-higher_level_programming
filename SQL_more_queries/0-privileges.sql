-- 0-privileges.sql

-- create user_0d_1 if missing
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY '';

-- show grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- create user_0d_2 if missing
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY '';

-- show grants for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
