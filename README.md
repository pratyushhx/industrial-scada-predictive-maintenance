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

## Dashboard Screenshots

### Main Dashboard

![Dashboard](dashboard_screenshots/dashboard.png)

---

### Current Gauges

![Gauge](dashboard_screenshots/gauge.png)

---

### Forecast Graph

![Forecast](dashboard_screenshots/forecast_graph.png)

---

### Predictive Recommendations

![Recommendations](dashboard_screenshots/predictive_recommendation.png)

---

### Industrial Alerts

![Alerts](dashboard_screenshots/alert_indicators.png)

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