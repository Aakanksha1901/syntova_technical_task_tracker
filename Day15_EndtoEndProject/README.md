## Car Showroom Inventory & Analytics API
## Project Overview
The Car Showroom Inventory & Analytics API is a Python-based REST API built with FastAPI and MySQL. It manages car inventory records and provides endpoints to retrieve car details, perform CRUD operations, and analyze inventory data.

The project uses a CSV dataset containing car details. Python and Pandas are used to inspect the dataset, MySQL stores the records, SQL queries support analytics, and FastAPI exposes the functionality through API endpoints.
Project Objectives
- Inspect and clean the car dataset.
- Create a MySQL database and cars table using Python.
- Import car records from a CSV file into MySQL.
- Implement Create, Read, Update, and Delete (CRUD) operations.
- Provide inventory, brand-wise, and fuel-type analytics.
- Test API endpoints using Swagger UI.
Technologies Used
- Python
- Pandas
- MySQL
- MySQL Connector/Python
- FastAPI
- Uvicorn
- SQL
- Swagger UI
Dataset
Dataset file: data/car_dataset_india.csv

The dataset contains car specifications and pricing details, including Car ID, Brand, Model, Year, Fuel Type, Transmission, Price, Mileage, Engine Capacity, Seating Capacity, and Service Cost.

The dataset check reported 10,000 rows, no missing values, and no duplicate rows at the time of checking.
Project Structure
Day15_EndtoEndProject/
├── data/
│   └── car_dataset_india.csv
├── create_database.py
├── data_check.py
├── car_showroom_analytics.sql
├── main.py
├── requirements.txt
└── README.md
Setup and Execution
1. Install requirements
Run from the project directory:
pip install -r requirements.txt
2. Configure MySQL
Make sure MySQL Server is running. Update the connection settings in create_database.py and main.py to match your local MySQL credentials.

Database name: car_showroom_db
3. Check the dataset
python data_check.py
This script displays dataset information, checks missing values and duplicates, removes duplicate rows, and saves the resulting data back to data/car_dataset_india.csv. Keep a backup if you need to preserve the original CSV.
4. Create the database and import data
python create_database.py
This script creates the database if it does not exist, creates the cars table if it does not exist, and imports the CSV records.

Important: Run this import script for initial setup. Running it again may cause duplicate-key errors because car_id is the primary key and existing records are inserted again.
5. Run SQL analytics
Open car_showroom_analytics.sql in MySQL Workbench and execute the queries after the database and table have been created. The script includes inventory queries and sample JOIN practice using a customers table.
6. Start FastAPI
uvicorn main:app --reload
API base URL: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

Stop the server with Ctrl+C.
API Endpoints
Method	Endpoint	Description
GET	/	Check whether the API is running
POST	/cars	Add a car
GET	/cars	Retrieve up to 100 cars
GET	/cars/count	Count car records
GET	/cars/{car_id}	Retrieve a car by ID
PUT	/cars/{car_id}	Update a car's editable fields
DELETE	/cars/{car_id}	Delete a car
GET	/analytics/summary	Total cars, average/minimum/maximum price, and average service cost
GET	/analytics/brands	Car counts and average prices by brand
GET	/analytics/fuel-types	Car counts and average prices by fuel type


The POST and PUT endpoints accept fields as query parameters in Swagger UI. The PUT endpoint expects all editable car fields.
Testing
Use http://127.0.0.1:8000/docs to test the endpoints.
1. Call GET /cars/count.
2. Call GET /cars and GET /cars/{car_id}.
3. Use POST /cars with a new, unused ID to create a test car.
4. Use GET /cars/{car_id} to confirm it exists.
5. Use PUT /cars/{car_id} to update the test car.
6. Use DELETE /cars/{car_id} to remove it.
7. Call GET /cars/count again to confirm the count returns to its previous value.
8. Test the three analytics endpoints.
Use a new test ID and avoid modifying or deleting existing dataset records.
