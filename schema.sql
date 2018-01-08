-- psql cryptowallet < schema.sql

DROP TABLE IF EXISTS sentiment;

CREATE TABLE sentiment(
    id SERIAL PRIMARY KEY,
    rating INTEGER,
    abrv VARCHAR(25) UNIQUE, 
    name VARCHAR(255),
    created TIMESTAMP DEFAULT current_timestamp,
    updated TIMESTAMP DEFAULT current_timestamp,
)