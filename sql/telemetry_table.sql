CREATE TABLE telemetry (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    date TEXT,
    shift TEXT,
    exhaust_no TEXT,
    time TEXT,
    HT_motor_current FLOAT,
    rfc FLOAT,
    suction FLOAT,
    air_flow FLOAT,
    Inlet_temperature FLOAT,
    Outlet_temperature FLOAT
);