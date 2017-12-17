-- psql cryptowallet < schema.sql

DROP TABLE IF EXISTS sentiment;

CREATE TABLE sentiment(
    id SERIAL PRIMARY KEY,
    rating INTEGER,
    abrv VARCHAR(25), 
)