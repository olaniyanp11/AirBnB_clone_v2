-- This script prepares a MySQL server for the project

-- Create `hbnb_test_db` database for AirBnB_clone
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to user in the `hbnb_test_db` database only
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- Grant SELECT privilege to user in the `performance_schema` database only
GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
