CREATE TABLE forecasts (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    predicted_current FLOAT,
    recommendation TEXT
);