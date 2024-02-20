-- A script that prepares a MySQL server for the HBNB Cloning Project:
-- A database hbnb_dev_db


CREATE DATABASE IF NOT EXISTS bnb_dev_db;

CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

USE bnb_dev_db;

GRANT ALL ON bnb_dev_db TO hbnb_dev;

GRANT SELECT ON performance_schema TO hbnb_dev;
