import psycopg2
import pandas as pd
import time
from sklearn.ensemble import IsolationForest

# DATABASE CONNECTION
conn = psycopg2.connect(
    host="postgres",
    database="industrial_telemetry",
    user="postgres",
    password="PPAASSWWOORRDD"
)

cursor = conn.cursor()

# CREATE TABLE IF NOT EXISTS
cursor.execute("""
CREATE TABLE IF NOT EXISTS ai_predictions (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    anomaly_score FLOAT,
    prediction VARCHAR(20)
)
""")

conn.commit()

print("AI Predictive Maintenance Model Started...", flush=True)

# AI LOOP
while True:

    try:


        # FETCH SENSOR DATA
        print("STEP 1: Querying sensor data...", flush=True)

        query = """
        SELECT
            outlet_temperature,
            inlet_temperature,
            suction_pressure,
            ht_motor_current,
            rotor_field_current,
            air_flow,
            machine_vibration,
            machine_health,
            machine_efficiency
        FROM sensors
        ORDER BY timestamp DESC
        LIMIT 300
        """

        df = pd.read_sql(query, conn)

        print(
            f"STEP 2: Rows fetched = {len(df)}",
            flush=True
        )

        # CLEAN DATA
        df = df.dropna()

        print(
            f"STEP 3: Rows after cleaning = {len(df)}",
            flush=True
        )

        # CHECK DATA SIZE
        if len(df) < 100:

            print(
                "STEP 4: Waiting for more sensor data...",
                flush=True
            )

            time.sleep(5)
            continue

        # TRAIN MODEL
        print("STEP 5: Training Isolation Forest...", flush=True)

        model = IsolationForest(
            contamination=0.03,
            random_state=42,
            n_estimators=150
        )

        model.fit(df)

        print("STEP 6: Model trained", flush=True)

        # PREDICTIONS
        predictions = model.predict(df)

        print("STEP 7: Predictions generated", flush=True)

        scores = model.decision_function(df)

        print("STEP 8: Scores generated", flush=True)

        latest_prediction = predictions[0]
        latest_score = scores[0]

        # SCORE SCALING
        scaled_score = latest_score * 100

        # CLASSIFICATION
        if latest_prediction == -1:

         if scaled_score < 0:
          prediction_label = "FAULT"
         else:
          prediction_label = "WARNING"

        else:
         prediction_label = "NORMAL"

        print(
            f"STEP 9: Prediction = {prediction_label}",
            flush=True
        )

        # STORE RESULT
        print(
            f"STEP 10: Inserting -> "
            f"Score={scaled_score:.2f}, "
            f"Prediction={prediction_label}",
            flush=True
        )

        cursor.execute("""
            INSERT INTO ai_predictions (
                anomaly_score,
                prediction
            )
            VALUES (%s, %s)
        """, (
            float(scaled_score),
            prediction_label
        ))

        conn.commit()

        print(
            f"STEP 11: Stored successfully | "
            f"{prediction_label} | "
            f"Score={scaled_score:.2f}",
            flush=True
        )

        time.sleep(5)

    except Exception as e:

        conn.rollback()

        print(
            f"AI ERROR: {e}",
            flush=True
        )

        time.sleep(5)