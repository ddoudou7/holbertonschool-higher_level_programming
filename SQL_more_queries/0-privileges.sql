-- 0-privileges.sql
-- Ensure user_0d_1 exists, then list its privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Ensure user_0d_2 exists, then list its privileges
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
