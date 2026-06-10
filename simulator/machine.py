import psycopg2
import random
import time

# ====================================
# DATABASE CONNECTION
# ====================================

conn = psycopg2.connect(
    host="postgres",
    database="industrial_telemetry",
    user="postgres",
    password="PPAASSWWOORRDD"
)

cursor = conn.cursor()

# ====================================
# INITIAL VALUES
# ====================================

outlet_temperature = 85.0
inlet_temperature = 72.0
suction_pressure = 82.0
ht_motor_current = 650.0
rotor_field_current = 520.0
air_flow = 19000.0
machine_vibration = 3.5

machine_health = 96.0
machine_efficiency = 95.0
estimated_rul = 960
machine_state = "NORMAL"
fault_cause = "None"
maintenance_action = "Normal Operation"

fault_timer = 0
warning_timer = 0

# ====================================
# CREATE TABLES
# ====================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS sensors (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    outlet_temperature FLOAT,
    inlet_temperature FLOAT,
    suction_pressure FLOAT,
    ht_motor_current FLOAT,
    rotor_field_current FLOAT,
    air_flow FLOAT,
    machine_vibration FLOAT,
    machine_health FLOAT,
    machine_efficiency FLOAT,
    machine_state VARCHAR(20)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alarms (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    severity VARCHAR(20),
    alarm_message TEXT,
    machine_state VARCHAR(20)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS machine_events (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    event_type VARCHAR(50),
    description TEXT
)
""")

conn.commit()

# ====================================
# INSERT ALARM
# ====================================

def insert_alarm(severity, message):

    cursor.execute("""
    INSERT INTO alarms (
        timestamp,
        severity,
        alarm_message,
        machine_state
    )
    VALUES (
        NOW(),
        %s,
        %s,
        %s
    )
    """, (
        severity,
        message,
        machine_state
    ))

    conn.commit()

# ====================================
# INSERT EVENT
# ====================================

def insert_event(event_type, description):

    cursor.execute("""
    INSERT INTO machine_events (
        event_type,
        description
    )
    VALUES (%s, %s)
    """, (
        event_type,
        description
    ))

    conn.commit()

# ====================================
# SENSOR SIMULATION
# ====================================

def generate_sensor_data():

    global outlet_temperature
    global inlet_temperature
    global suction_pressure
    global ht_motor_current
    global rotor_field_current
    global air_flow
    global machine_vibration
    global machine_health
    global machine_efficiency
    global estimated_rul
    global machine_state
    global fault_cause
    global fault_timer
    global warning_timer
    global maintenance_action

    state_roll = random.random()

    # ==========================
    # NORMAL -> WARNING
    # ==========================

    if machine_state == "NORMAL":

        if state_roll < 0.03:
            machine_state = "WARNING"
            warning_timer = random.randint(5, 10)

            insert_alarm(
                "WARNING",
                "Machine parameters drifting"
            )

            insert_event(
                "STATE_CHANGE",
                "Machine entered WARNING state"
            )

    # ==========================
    # WARNING -> FAULT
    # ==========================

    elif machine_state == "WARNING":
      if state_roll < 0.05:

        machine_state = "FAULT"

        fault_cause = random.choice([
            "Bearing Failure",
            "Motor Overload",
            "Cooling Failure"
        ])

        fault_timer = random.randint(5, 10)
        insert_alarm(
    "CRITICAL",
    f"Critical machine fault: {fault_cause}"
)

        insert_event(
    "FAULT",
    fault_cause
)

    # ==========================
    # NORMAL DATA
    # ==========================

    if machine_state == "NORMAL":

        maintenance_action = "Normal Operation"
        fault_cause = "None"

        outlet_temperature += random.uniform(-1,1)

        outlet_temperature = max(
        72,
        min(outlet_temperature,85)
)
        inlet_temperature = random.uniform(62, 72)

        suction_pressure = random.uniform(90, 95)

        ht_motor_current = random.uniform(500, 580)
        rotor_field_current = random.uniform(420, 520)

        air_flow = random.uniform(19000, 22000)

        machine_vibration += random.uniform(-0.2,0.2)

        machine_vibration = max(
        2,
        min(machine_vibration,4)
)

        # Health now calculated dynamically below
        pass

    # ==========================
    # WARNING DATA
    # ==========================

    elif machine_state == "WARNING":
        
        warning_timer -= 1

        outlet_temperature = random.uniform(85, 100)
        inlet_temperature = random.uniform(70, 85)

        suction_pressure = random.uniform(80, 90)

        ht_motor_current = random.uniform(580, 700)
        rotor_field_current = random.uniform(500, 620)

        air_flow = random.uniform(17000, 20000)

        machine_vibration = random.uniform(4, 8)

        machine_health -= random.uniform(1, 2)
        # Determine likely failure cause

        if machine_vibration > 6:
         fault_cause = "Bearing Failure"
         maintenance_action = "Inspect bearings soon"

        elif outlet_temperature > 90:
         fault_cause = "Cooling Failure"
         maintenance_action = "Check cooling system"

        elif ht_motor_current > 650:
         fault_cause = "Motor Overload"
         maintenance_action = "Inspect motor load"

        else:
         fault_cause = "None"
        maintenance_action = "Monitor machine closely"

        if warning_timer <= 0:

            maintenance_action = "Normal Operation"
            machine_state = "NORMAL"
            fault_cause = "None"

            insert_event(
                "RECOVERY",
                "Recovered from WARNING"
            )

    # ==========================
    # FAULT DATA
    # ==========================

    elif machine_state == "FAULT":

        fault_timer -= 1

        outlet_temperature = random.uniform(100, 120)
        inlet_temperature = random.uniform(80, 100)

        suction_pressure = random.uniform(70, 80)

        ht_motor_current = random.uniform(750, 900)
        rotor_field_current = random.uniform(600, 700)

        air_flow = random.uniform(15000, 18000)

        machine_vibration = random.uniform(8, 15)

        machine_health -= random.uniform(3, 5)

        if fault_timer <= 0:

            machine_state = "NORMAL"
            fault_cause = "None"
            maintenance_action = "Normal Operation"

            machine_health += random.uniform(10, 20)

            insert_event(
                "RECOVERY",
                "Recovered from FAULT"
            )

       # ==========================
    # HEALTH MODEL
    # ==========================

    health_penalty = (
        machine_vibration * 1.5
        + max(0, outlet_temperature - 80) * 0.3
        + max(0, ht_motor_current - 550) * 0.02
    )

    machine_health = 100 - health_penalty

    machine_health += random.uniform(-2, 2)

    machine_health = max(
        0,
        min(machine_health, 100)
    )

    # ==========================
    # RUL ESTIMATION
    # ==========================

    estimated_rul = int(machine_health * 10)

    # ==========================
    # EFFICIENCY MODEL
    # ==========================

    vibration_factor = max(
        0,
        100 - machine_vibration * 5
    )

    pressure_factor = max(
        0,
        100 - abs(suction_pressure - 82)
    )

    airflow_factor = min(
        100,
        air_flow / 230
    )

    machine_efficiency = (
        machine_health * 0.50
        + vibration_factor * 0.20
        + pressure_factor * 0.15
        + airflow_factor * 0.15
    )

    machine_efficiency += random.uniform(-1, 1)

    machine_efficiency = max(
        40,
        min(machine_efficiency, 100)
    )

# ====================================
# INSERT SENSOR DATA
# ====================================

def insert_sensor_data():

    cursor.execute("""
    INSERT INTO sensors (
    outlet_temperature,
    inlet_temperature,
    suction_pressure,
    ht_motor_current,
    rotor_field_current,
    air_flow,
    machine_vibration,
    machine_health,
    machine_efficiency,
    estimated_rul,
    machine_state,
    fault_cause,
    maintenance_action
)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        outlet_temperature,
        inlet_temperature,
        suction_pressure,
        ht_motor_current,
        rotor_field_current,
        air_flow,
        machine_vibration,
        machine_health,
        machine_efficiency,
        estimated_rul,
        machine_state,
        fault_cause,
        maintenance_action
    ))

    conn.commit()

# ====================================
# PRINT STATUS
# ====================================

def print_machine_status():

    print(
        f"STATE: {machine_state} | "
        f"CAUSE: {fault_cause} | "
        f"ACTION: {maintenance_action} | "
        f"TEMP: {outlet_temperature:.2f} °C | "
        f"INLET: {inlet_temperature:.2f} °C | "
        f"VIBRATION: {machine_vibration:.2f} mm/s | "
        f"PRESSURE: {suction_pressure:.2f} psi | "
        f"CURRENT: {ht_motor_current:.2f} A | "
        f"ROTOR: {rotor_field_current:.2f} A | "
        f"AIRFLOW: {air_flow:.2f} m³/h | "
        f"HEALTH: {machine_health:.2f}% | "
        f"EFFICIENCY: {machine_efficiency:.2f}%"
    )

# ====================================
# MAIN LOOP
# ====================================

print("SCADA Simulator Started...\n")

while True:

    generate_sensor_data()

    insert_sensor_data()

    print_machine_status()

    time.sleep(2)