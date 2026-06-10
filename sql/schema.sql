CREATE TABLE sensors (
id SERIAL PRIMARY KEY,
timestamp TIMESTAMP,

```
outlet_temperature FLOAT,
inlet_temperature FLOAT,
suction_pressure FLOAT,

ht_motor_current FLOAT,
rotor_field_current FLOAT,

air_flow FLOAT,
machine_vibration FLOAT,

machine_health FLOAT,
machine_efficiency FLOAT,

machine_state VARCHAR(20),

fault_cause VARCHAR(100),
maintenance_action VARCHAR(200),

estimated_rul FLOAT
```

);

CREATE TABLE alarms (
id SERIAL PRIMARY KEY,
timestamp TIMESTAMP,

```
severity VARCHAR(20),
alarm_message TEXT,
machine_state VARCHAR(20)
```

);

CREATE TABLE machine_events (
id SERIAL PRIMARY KEY,
timestamp TIMESTAMP,

```
event_type VARCHAR(50),
description TEXT
```

);

CREATE TABLE ai_predictions (
id SERIAL PRIMARY KEY,
timestamp TIMESTAMP,

```
anomaly_score FLOAT,
prediction VARCHAR(20)
```

);
