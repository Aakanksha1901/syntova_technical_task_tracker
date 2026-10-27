import mysql.connector
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Car Showroom Inventory API")


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",
        database="car_showroom_db"
    )


@app.get("/")
def home():
    return {"message": "Car Showroom Inventory API is running"}


# CREATE - Add a car
@app.post("/cars", status_code=201)
def create_car(
    car_id: int, brand: str, model: str, year: int,
    fuel_type: str, transmission: str, price: float,
    mileage: float, engine_cc: int, seating_capacity: int,
    service_cost: float
):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            INSERT INTO cars
            (car_id, brand, model, year, fuel_type, transmission,
             price, mileage, engine_cc, seating_capacity, service_cost)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            car_id, brand, model, year, fuel_type, transmission,
            price, mileage, engine_cc, seating_capacity, service_cost
        ))
        connection.commit()
        return {"message": "Car added successfully", "car_id": car_id}
    except mysql.connector.IntegrityError:
        raise HTTPException(status_code=409, detail="Car ID already exists")
    finally:
        cursor.close()
        connection.close()


# READ - Get all cars
@app.get("/cars")
def get_cars():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM cars LIMIT 100")
        return {"cars": cursor.fetchall()}
    finally:
        cursor.close()
        connection.close()


# READ - Count cars (keep before /cars/{car_id})
@app.get("/cars/count")
def count_cars():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM cars")
        return {"total_cars": cursor.fetchone()[0]}
    finally:
        cursor.close()
        connection.close()


# READ - Get one car by ID
@app.get("/cars/{car_id}")
def get_car(car_id: int):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM cars WHERE car_id = %s", (car_id,))
        car = cursor.fetchone()
        if car is None:
            raise HTTPException(status_code=404, detail="Car not found")
        return {"car": car}
    finally:
        cursor.close()
        connection.close()


# UPDATE - Update a car (provide all fields)
@app.put("/cars/{car_id}")
def update_car(
    car_id: int, brand: str, model: str, year: int,
    fuel_type: str, transmission: str, price: float,
    mileage: float, engine_cc: int, seating_capacity: int,
    service_cost: float
):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            UPDATE cars
            SET brand = %s, model = %s, year = %s, fuel_type = %s,
                transmission = %s, price = %s, mileage = %s,
                engine_cc = %s, seating_capacity = %s, service_cost = %s
            WHERE car_id = %s
        """, (
            brand, model, year, fuel_type, transmission, price,
            mileage, engine_cc, seating_capacity, service_cost, car_id
        ))
        connection.commit()
        if cursor.rowcount == 0:
            cursor.execute("SELECT car_id FROM cars WHERE car_id = %s", (car_id,))
            if cursor.fetchone() is None:
                raise HTTPException(status_code=404, detail="Car not found")
            return {"message": "No changes made"}
        return {"message": "Car updated successfully", "car_id": car_id}
    finally:
        cursor.close()
        connection.close()


# DELETE - Delete a car
@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM cars WHERE car_id = %s", (car_id,))
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Car not found")
        return {"message": "Car deleted successfully", "car_id": car_id}
    finally:
        cursor.close()
        connection.close()


# ANALYTICS - Inventory summary
@app.get("/analytics/summary")
def inventory_summary():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT COUNT(*), AVG(price), MIN(price), MAX(price),
                   AVG(service_cost)
            FROM cars
        """)
        row = cursor.fetchone()
        return {
            "total_cars": row[0],
            "average_price": row[1],
            "minimum_price": row[2],
            "maximum_price": row[3],
            "average_service_cost": row[4]
        }
    finally:
        cursor.close()
        connection.close()


# ANALYTICS - Cars by brand
@app.get("/analytics/brands")
def brand_summary():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT brand, COUNT(*) AS car_count, AVG(price) AS average_price
            FROM cars
            GROUP BY brand
            ORDER BY car_count DESC
        """)
        results = cursor.fetchall()
        return {
            "brands": [
                {"brand": row[0], "car_count": row[1], "average_price": row[2]}
                for row in results
            ]
        }
    finally:
        cursor.close()
        connection.close()


# ANALYTICS - Cars by fuel type
@app.get("/analytics/fuel-types")
def fuel_type_summary():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT fuel_type, COUNT(*) AS car_count, AVG(price) AS average_price
            FROM cars
            GROUP BY fuel_type
            ORDER BY car_count DESC
        """)
        results = cursor.fetchall()
        return {
            "fuel_types": [
                {"fuel_type": row[0], "car_count": row[1], "average_price": row[2]}
                for row in results
            ]
        }
    finally:
        cursor.close()
        connection.close()
