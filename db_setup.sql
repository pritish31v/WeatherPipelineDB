CREATE DATABASE weatherdb;

DROP TABLE IF EXISTS weather_data;

CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    district VARCHAR(100),
    state VARCHAR(100),
    temperature NUMERIC(5,2),
    humidity NUMERIC(5,2),
    weather_description VARCHAR(255),
    timestamp TIMESTAMP DEFAULT NOW()
);
