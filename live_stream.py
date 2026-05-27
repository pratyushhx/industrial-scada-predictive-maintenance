import pandas as pd
from sqlalchemy import create_engine
import time

engine = create_engine(
    "postgresql+psycopg2://postgres:PPAASSWWOORRDD@localhost:5432/industrial_telemetry"
)

df = pd.read_csv("data/industrial_telemetry.csv")
df.columns = df.columns.str.lower()

df["timestamp"] = pd.to_datetime(
    df["date"].astype(str) + " " + df["time"].astype(str),
    errors="coerce"
)

df = df.dropna(subset=["timestamp"])

while True:
    for i in range(len(df)):
        row = df.iloc[[i]]

        row.to_sql(
            "telemetry",
            engine,
            if_exists="append",
            index=False
        )

        print(f"Inserted row {i+1}")

        time.sleep(5)