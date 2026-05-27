# Industrial Energy Optimization & Monitoring System

## Project Overview

This project is a real-time industrial telemetry analytics platform developed using Python, PostgreSQL, Grafana, and Prophet forecasting.

The system simulates industrial sinter plant machinery monitoring by continuously streaming telemetry data into PostgreSQL and visualizing live operational metrics through Grafana dashboards.

---

## Features

- Real-time telemetry streaming
- Dynamic Grafana dashboards
- Industrial anomaly detection
- Predictive forecasting using Prophet
- PostgreSQL telemetry backend
- Intelligent recommendation system
- SCADA-style monitoring interface
- Auto-refreshing telemetry visualizations

---

## Real-Time Streaming

This project implements a live telemetry streaming engine using Python and PostgreSQL.

A continuous telemetry ingestion pipeline inserts industrial sensor readings into PostgreSQL at regular intervals, enabling Grafana dashboards to dynamically auto-refresh with live operational data.

The streaming architecture simulates real-world industrial SCADA and IoT telemetry systems.

---

## Tech Stack

- Python
- PostgreSQL
- Grafana
- Pandas
- SQLAlchemy
- Prophet

---

## System Architecture

Telemetry CSV Data  
↓  
Python Streaming Pipeline  
↓  
PostgreSQL Database  
↓  
Grafana Dashboards  
↓  
Anomaly Detection & Forecasting

---

## Workflow

1. Industrial telemetry CSV data is loaded using Pandas.
2. Python streaming pipeline continuously inserts telemetry rows into PostgreSQL.
3. Grafana dynamically queries PostgreSQL and auto-refreshes dashboards.
4. Prophet forecasting predicts future telemetry trends.
5. Alert indicators detect industrial anomalies like:
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
- Recommendation generation

---

## Installation

```bash
pip install -r requirements.txt