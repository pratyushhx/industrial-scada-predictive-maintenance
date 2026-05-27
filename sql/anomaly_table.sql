CREATE TABLE anomalies (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    ht_motor_current FLOAT,
    outlet_temperature FLOAT,
    alert_type TEXT
);