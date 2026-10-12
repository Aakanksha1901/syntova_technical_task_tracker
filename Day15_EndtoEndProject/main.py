import os
import time
from contextlib import contextmanager
from typing import Optional

import mysql.connector
import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI(
    title="Car Showroom Inventory & Analytics API",
    description="Manage car inventory and analyse vehicle prices using MySQL and Pandas.",
    version="1.0.0",
)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "showroom_user"),
    "password": os.getenv("DB_PASSWORD", "showroom_password"),
    "database": os.getenv("DB_NAME", "car_showroom_db"),
}


@contextmanager
def get_connection():
    connection = mysql.connector.connect(**DB_CONFIG)
    try:
        yield connection
    finally:
        connection.close()


def initialize_database():
    """Create the cars table and load the supplied CSV once if the table is empty."""
    last_error = None
    for attempt in range(30):
        try:
            with get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS cars (
                        car_id INT PRIMARY KEY,
                        brand VARCHAR(100) NOT NULL,
                        model VARCHAR(100) NOT NULL,
                        year INT NOT NULL,
                        fuel_type VARCHAR(50) NOT NULL,
                        transmission VARCHAR(50) NOT NULL,
                        price DECIMAL(12,2) NOT NULL,
                        mileage DECIMAL(8,2) NOT NULL,
                        engine_cc INT NOT NULL,
                        seating_capacity INT NOT NULL,
                        service_cost DECIMAL(12,2) NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                connection.commit()
                cursor.execute("SELECT COUNT(*) FROM cars")
                count = cursor.fetchone()[0]
                cursor.close()

                if count == 0:
                    csv_path = os.getenv("CAR_DATA_PATH", "data/car_dataset_india.csv")
                    if os.path.exists(csv_path):
                        df = pd.read_csv(csv_path)
                        df.columns = [column.strip() for column in df.columns]
                        expected = [
                            "Car_ID", "Brand", "Model", "Year", "Fuel_Type",
                            "Transmission", "Price", "Mileage", "Engine_CC",
                            "Seating_Capacity", "Service_Cost"
                        ]
                        missing = [column for column in expected if column not in df.columns]
                        if missing:
                            raise ValueError(f"CSV is missing expected columns: {missing}")
                        rows = []
                        for row in df[expected].itertuples(index=False, name=None):
                            rows.append((
                                int(row[0]), str(row[1]), str(row[2]), int(row[3]),
                                str(row[4]), str(row[5]), float(row[6]), float(row[7]),
                                int(row[8]), int(row[9]), float(row[10])
                            ))
                        with get_connection() as insert_connection:
                            insert_cursor = insert_connection.cursor()
                            insert_cursor.executemany("""
                                INSERT IGNORE INTO cars
                                (car_id, brand, model, year, fuel_type, transmission,
                                 price, mileage, engine_cc, seating_capacity, service_cost)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """, rows)
                            insert_connection.commit()
                            insert_cursor.close()
            return
        except (mysql.connector.Error, OSError, ValueError) as error:
            last_error = error
            time.sleep(2)
    raise RuntimeError(f"Database initialization failed: {last_error}")


@app.on_event("startup")
def startup_event():
    initialize_database()


class CarCreate(BaseModel):
    car_id: int = Field(gt=0)
    brand: str = Field(min_length=1, max_length=100)
    model: str = Field(min_length=1, max_length=100)
    year: int = Field(ge=1900, le=2100)
    fuel_type: str = Field(min_length=1, max_length=50)
    transmission: str = Field(min_length=1, max_length=50)
    price: float = Field(ge=0)
    mileage: float = Field(ge=0)
    engine_cc: int = Field(ge=0)
    seating_capacity: int = Field(ge=1, le=100)
    service_cost: float = Field(ge=0)


class CarUpdate(BaseModel):
    brand: Optional[str] = Field(default=None, min_length=1, max_length=100)
    model: Optional[str] = Field(default=None, min_length=1, max_length=100)
    year: Optional[int] = Field(default=None, ge=1900, le=2100)
    fuel_type: Optional[str] = Field(default=None, min_length=1, max_length=50)
    transmission: Optional[str] = Field(default=None, min_length=1, max_length=50)
    price: Optional[float] = Field(default=None, ge=0)
    mileage: Optional[float] = Field(default=None, ge=0)
    engine_cc: Optional[int] = Field(default=None, ge=0)
    seating_capacity: Optional[int] = Field(default=None, ge=1, le=100)
    service_cost: Optional[float] = Field(default=None, ge=0)


def row_to_dict(cursor, row):
    return {description[0]: value for description, value in zip(cursor.description, row)}


@app.get("/")
def home():
    return {"message": "Car Showroom Inventory & Analytics API is running"}


@app.get("/cars")
def get_cars(
    brand: Optional[str] = None,
    fuel_type: Optional[str] = None,
    transmission: Optional[str] = None,
    min_price: Optional[float] = Query(default=None, ge=0),
    max_price: Optional[float] = Query(default=None, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    query = "SELECT * FROM cars WHERE 1=1"
    params = []
    if brand:
        query += " AND brand LIKE %s"
        params.append(f"%{brand}%")
    if fuel_type:
        query += " AND fuel_type = %s"
        params.append(fuel_type)
    if transmission:
        query += " AND transmission = %s"
        params.append(transmission)
    if min_price is not None:
        query += " AND price >= %s"
        params.append(min_price)
    if max_price is not None:
        query += " AND price <= %s"
        params.append(max_price)
    query += " ORDER BY car_id LIMIT %s OFFSET %s"
    params.extend([limit, offset])
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            result = [row_to_dict(cursor, row) for row in cursor.fetchall()]
            cursor.close()
            return result
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Could not retrieve cars") from error


@app.get("/cars/count")
def car_count():
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM cars")
        total = cursor.fetchone()[0]
        cursor.close()
        return {"total_cars": total}


@app.post("/cars", status_code=201)
def create_car(car: CarCreate):
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO cars
                (car_id, brand, model, year, fuel_type, transmission, price,
                 mileage, engine_cc, seating_capacity, service_cost)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, tuple(car.model_dump().values()))
            connection.commit()
            cursor.close()
        return {"message": "Car added successfully", "car_id": car.car_id}
    except mysql.connector.IntegrityError as error:
        raise HTTPException(status_code=409, detail="Car ID already exists") from error
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Could not add car") from error


@app.put("/cars/{car_id}")
def update_car(car_id: int, car: CarUpdate):
    updates = car.model_dump(exclude_unset=True, exclude_none=True)
    if not updates:
        raise HTTPException(status_code=400, detail="Provide at least one field to update")
    allowed = {
        "brand", "model", "year", "fuel_type", "transmission", "price",
        "mileage", "engine_cc", "seating_capacity", "service_cost"
    }
    if not set(updates).issubset(allowed):
        raise HTTPException(status_code=400, detail="Invalid update fields")
    set_clause = ", ".join(f"{column} = %s" for column in updates)
    values = list(updates.values()) + [car_id]
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(f"UPDATE cars SET {set_clause} WHERE car_id = %s", values)
            connection.commit()
            changed = cursor.rowcount
            cursor.close()
        if changed == 0:
            raise HTTPException(status_code=404, detail="Car not found or values unchanged")
        return {"message": "Car updated successfully", "car_id": car_id}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Could not update car") from error


@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM cars WHERE car_id = %s", (car_id,))
            connection.commit()
            deleted = cursor.rowcount
            cursor.close()
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Car not found")
        return {"message": "Car deleted successfully", "car_id": car_id}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Could not delete car") from error


@app.get("/analytics/summary")
def analytics_summary():
    with get_connection() as connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT COUNT(*) AS total_cars,
                   ROUND(AVG(price), 2) AS average_price,
                   MIN(price) AS minimum_price,
                   MAX(price) AS maximum_price,
                   ROUND(AVG(service_cost), 2) AS average_service_cost
            FROM cars
        """)
        result = cursor.fetchone()
        cursor.close()
        for key, value in result.items():
            if value is not None:
                result[key] = float(value) if key != "total_cars" else int(value)
        return result


@app.get("/analytics/brands")
def analytics_brands():
    with get_connection() as connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT brand, COUNT(*) AS car_count,
                   ROUND(AVG(price), 2) AS average_price
            FROM cars
            GROUP BY brand
            ORDER BY car_count DESC, brand
        """)
        results = cursor.fetchall()
        cursor.close()
        for row in results:
            row["average_price"] = float(row["average_price"] or 0)
        return results


@app.get("/analytics/fuel-types")
def analytics_fuel_types():
    with get_connection() as connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT fuel_type, COUNT(*) AS car_count,
                   ROUND(AVG(price), 2) AS average_price
            FROM cars
            GROUP BY fuel_type
            ORDER BY car_count DESC
        """)
        results = cursor.fetchall()
        cursor.close()
        for row in results:
            row["average_price"] = float(row["average_price"] or 0)
        return results


@app.get("/analytics/pandas")
def pandas_analytics():
    with get_connection() as connection:
        df = pd.read_sql(
            "SELECT brand, fuel_type, price, mileage, service_cost FROM cars",
            connection
        )
    if df.empty:
        return {"total_cars": 0, "average_price": 0, "top_brand_by_count": None}
    brand_counts = df["brand"].value_counts()
    return {
        "total_cars": int(len(df)),
        "average_price": round(float(df["price"].mean()), 2),
        "average_mileage": round(float(df["mileage"].mean()), 2),
        "average_service_cost": round(float(df["service_cost"].mean()), 2),
        "top_brand_by_count": str(brand_counts.index[0]),
        "top_brand_car_count": int(brand_counts.iloc[0]),
        "fuel_type_counts": {
            str(key): int(value) for key, value in df["fuel_type"].value_counts().items()
        },
    }
