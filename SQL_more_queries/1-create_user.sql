-- 1-create_user.sql
-- Creates MySQL user user_0d_1 with full privileges
-- If the user already exists, the script must not fail

/* create account (no error if déjà là) */
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

/* give ALL privileges everywhere */
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

/* safest way to finish */
FLUSH PRIVILEGES;
