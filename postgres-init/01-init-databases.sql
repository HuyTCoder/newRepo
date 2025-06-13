-- PostgreSQL initialization script for healthcare system
-- This script creates all required databases and sets up user permissions

-- Create databases for PostgreSQL services
CREATE DATABASE laboratory_db;
CREATE DATABASE pharmacy_db;

-- Grant all privileges on the databases to the user
GRANT ALL PRIVILEGES ON DATABASE laboratory_db TO mcuong1011;
GRANT ALL PRIVILEGES ON DATABASE pharmacy_db TO mcuong1011;

-- Connect to each database and grant schema privileges
\c laboratory_db;
GRANT ALL ON SCHEMA public TO mcuong1011;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO mcuong1011;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO mcuong1011;

\c pharmacy_db;
GRANT ALL ON SCHEMA public TO mcuong1011;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO mcuong1011;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO mcuong1011;

-- === Medical Records service ===
CREATE USER mcuong1011 WITH ENCRYPTED PASSWORD 'mcuong1011';
CREATE DATABASE medical_records_db OWNER mcuong1011;
GRANT ALL PRIVILEGES ON DATABASE medical_records_db TO mcuong1011;

\connect medical_records_db
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
-- tables will be created by Django migrations


-- Display created databases for verification
\l
