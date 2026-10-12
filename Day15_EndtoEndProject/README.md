# Car Showroom Inventory & Analytics API

## Project Overview

The Car Showroom Inventory & Analytics API is a Python-based REST API developed using FastAPI and MySQL. It manages car inventory records and provides endpoints for retrieving car details, counting inventory, and analyzing car data using Pandas.

The project uses Docker Compose to run the API and MySQL database as separate services.

## Technologies Used

- Python
- FastAPI
- MySQL
- Pandas
- Docker
- Docker Compose
- REST API
- CSV Dataset

## Project Structure

```text
Day15_Car_Showroom_MySQL_API/
│
├── data/
│   └── car_dataset_india.csv
│
├── main.py
├── data_check.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

## Dataset

The project uses `car_dataset_india.csv`, which contains car specifications and pricing information.

The dataset includes fields such as:

- Car ID
- Brand
- Model
- Year
- Fuel Type
- Transmission
- Price
- Mileage
- Engine Capacity
- Seating Capacity
- Service Cost

## Features

- REST API development using FastAPI
- Car inventory management
- CRUD operations for car records
- MySQL database integration
- Dataset analysis using Pandas
- Inventory summary and brand-based analysis
- Fuel-type analysis
- Interactive API documentation using Swagger UI
- Containerization using Docker
- Multi-service setup using Docker Compose

## Installation and Execution

### 1. Clone or open the project

Open the project folder in VS Code.

### 2. Install dependencies locally (optional)

```bash
pip install -r requirements.txt
```

### 3. Start the application using Docker Compose

Ensure Docker Desktop is running, then execute:

```bash
docker compose up --build
```

### 4. Access the API

Base URL:

```text
http://localhost:8000
```

Swagger UI documentation:

```text
http://localhost:8000/docs
```

### 5. Stop the application

```bash
docker compose down
```

To remove the containers and the stored database volume:

```bash
docker compose down -v
```

**Warning:** The `-v` option deletes the persisted MySQL database data.

## API Documentation

The available endpoints depend on the implementation in `main.py`. Open Swagger UI at `/docs` after starting the application to view and test the registered endpoints.

## Learning Outcomes

- Building REST APIs with FastAPI
- Connecting Python applications to MySQL
- Working with CSV datasets using Pandas
- Implementing inventory CRUD operations
- Using Dockerfiles and Docker Compose
- Testing APIs through Swagger UI

## Conclusion

This project demonstrates an end-to-end backend application that combines REST API development, relational database integration, data analysis, and containerization for a car showroom inventory management use case.
