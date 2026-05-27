# Industrial Energy Optimization & Monitoring System

## Project Overview

This project is a real-time industrial telemetry analytics platform developed using Python, PostgreSQL, Grafana, and Prophet forecasting.

The system simulates industrial sinter plant machinery monitoring by continuously streaming telemetry data into PostgreSQL and visualizing live operational metrics through dynamic Grafana dashboards.

The platform includes:
- Real-time telemetry streaming
- SCADA-style dashboard monitoring
- Industrial anomaly detection
- Predictive forecasting
- Intelligent recommendation generation

---

## Features

- Real-time telemetry streaming using Python
- Dynamic Grafana dashboards with auto-refresh
- PostgreSQL telemetry backend integration
- Industrial anomaly detection engine
- Predictive forecasting using Prophet
- Intelligent recommendation system
- SCADA-style industrial monitoring interface
- Live telemetry simulation pipeline

---

## Tech Stack

### Languages
- Python
- SQL

### Libraries & Tools
- Pandas
- NumPy
- Matplotlib
- SQLAlchemy
- Prophet
- PostgreSQL
- Grafana

---

## Project Structure

```text
industrial-telemetry-platform/
│
├── dashboard_screenshots/
│
├── data/
│   └── industrial_telemetry.csv
│
├── notebooks/
│   ├── telemetry_analysis.ipynb
│   ├── anomaly_detection.ipynb
│   └── forecasting.ipynb
│
├── sql/
│   ├── telemetry_table.sql
│   ├── anomaly_table.sql
│   └── forecast_table.sql
│
├── live_stream.py
├── requirements.txt
└── README.md
```

---

## System Architecture

```text
Telemetry CSV Data
        ↓
Python Streaming Pipeline
        ↓
PostgreSQL Database
        ↓
Grafana Dashboards
        ↓
Anomaly Detection
        ↓
Forecasting Engine
        ↓
Recommendation System
```

---

## Workflow

1. Industrial telemetry CSV data is loaded using Pandas.
2. Python streaming pipeline continuously inserts telemetry records into PostgreSQL.
3. Grafana dynamically queries PostgreSQL and auto-refreshes dashboards.
4. Prophet forecasting predicts future telemetry trends.
5. Alert indicators detect industrial anomalies such as:
   - High motor current
   - High outlet temperature
6. Predictive recommendations are generated for operational monitoring.

---

## Dashboard Screenshots

### Main Dashboard

![Dashboard](dashboard_screenshots/Dashboard.png)

---

### Current Gauges

![Gauge](dashboard_screenshots/Gauge.png)

---

### Predictive Recommendations

![Recommendations](dashboard_screenshots/Predictive_Recommendation.png)

---

### Industrial Alerts

![Alerts](dashboard_screenshots/Alert_Indicators.png)

---

## Key Functionalities

### Real-Time Monitoring
- HT motor current monitoring
- Outlet temperature tracking
- Airflow analysis
- Suction trend monitoring

### Anomaly Detection
- High motor current alerts
- High outlet temperature alerts
- Industrial event visualization

### Forecasting
- Predictive telemetry forecasting using Prophet
- Future machine behavior estimation
- Intelligent operational recommendations

---

## Installation

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Project

### Start Real-Time Telemetry Streaming

```bash
python live_stream.py
```

The script continuously inserts telemetry records into PostgreSQL, enabling Grafana dashboards to update dynamically in real time.

---

## Open Grafana Dashboard

```text
http://localhost:3000
```

---

## Future Enhancements

- Apache Kafka integration
- Docker deployment
- MQTT IoT integration
- Cloud-hosted telemetry pipelines
- Predictive maintenance engine
- Industrial AI recommendation systems

---

## GitHub Repository

https://github.com/pratyushhx/Industrial-Energy-Optimization-System

---

## Author

Developed as an Industrial Internship Project focused on telemetry analytics, predictive monitoring, industrial IoT simulation, and energy optimization systems.