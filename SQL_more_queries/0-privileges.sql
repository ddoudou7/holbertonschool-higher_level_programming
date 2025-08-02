-- List all privileges of user_0d_1 and user_0d_2 on localhost
-- If a user does not exist, display an informative line instead of failing.

-- ► user_0d_1
SELECT '### user_0d_1 ###' AS '';
SELECT IF(
  EXISTS (SELECT 1 FROM mysql.user WHERE user='user_0d_1' AND host='localhost'),
  'User exists' , 'User user_0d_1@localhost does not exist'
) AS '';
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- ► user_0d_2
SELECT '### user_0d_2 ###' AS '';
SELECT IF(
  EXISTS (SELECT 1 FROM mysql.user WHERE user='user_0d_2' AND host='localhost'),
  'User exists' , 'User user_0d_2@localhost does not exist'
) AS '';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
