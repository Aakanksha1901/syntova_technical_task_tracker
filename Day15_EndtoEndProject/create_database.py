import mysql.connector
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "car_dataset_india.csv"

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123"
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS car_showroom_db")
cursor.execute("USE car_showroom_db")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cars (
        car_id INT PRIMARY KEY,
        brand VARCHAR(100),
        model VARCHAR(100),
        year INT,
        fuel_type VARCHAR(50),
        transmission VARCHAR(50),
        price DECIMAL(12,2),
        mileage DECIMAL(8,2),
        engine_cc INT,
        seating_capacity INT,
        service_cost DECIMAL(12,2),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

df = pd.read_csv(CSV_PATH)
df.columns = df.columns.str.strip()

df = df.rename(columns={
    "Car_ID": "car_id",
    "Brand": "brand",
    "Model": "model",
    "Year": "year",
    "Fuel_Type": "fuel_type",
    "Transmission": "transmission",
    "Price": "price",
    "Mileage": "mileage",
    "Engine_CC": "engine_cc",
    "Seating_Capacity": "seating_capacity",
    "Service_Cost": "service_cost"
})

columns = [
    "car_id", "brand", "model", "year", "fuel_type",
    "transmission", "price", "mileage", "engine_cc",
    "seating_capacity", "service_cost"
]

df = df[columns]

data = list(df.itertuples(index=False, name=None))

query = """
    INSERT IGNORE INTO cars (
        car_id, brand, model, year, fuel_type, transmission,
        price, mileage, engine_cc, seating_capacity, service_cost
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

cursor.executemany(query, data)
connection.commit()

cursor.execute("SELECT COUNT(*) FROM cars")
print("Total cars imported:", cursor.fetchone()[0])

cursor.close()
connection.close()

print("Database, table, and dataset created successfully!")