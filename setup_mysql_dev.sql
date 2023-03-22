--This script prepares a MySQL server for the project

-- Create `hbnb_dev_db` database for AirBnB_clone
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev';

-- Grant all privileges to user in the `hbnb_dev_db` database only
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Grant SELECT privilege to user in the `performance_schema` database only
GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
