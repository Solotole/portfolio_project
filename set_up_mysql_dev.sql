-- setting a mysql database
CREATE DATABASE IF NOT EXISTS brrs_dev_db;
CREATE USER IF NOT EXISTS `brrs_dev`@`localhost` IDENTIFIED BY 'Brrs_dev_pwd123!';
GRANT ALL PRIVILEGES ON brrs_dev_db.* TO `brrs_dev`@`localhost`;
GRANT SELECT ON performance_schema.* TO `brrs_dev`@`localhost`;
