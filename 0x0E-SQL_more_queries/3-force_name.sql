-- 3. Always a name
-- Script to create the table force_name on the MySQL server

CREATE TABLE IF NOT EXISTS force_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
