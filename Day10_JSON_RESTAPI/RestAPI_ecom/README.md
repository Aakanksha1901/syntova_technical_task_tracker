# E-commerce REST API

## Project Description

This project demonstrates JSON and REST API concepts using FastAPI.

The API uses e-commerce order data containing:

- Order Date
- Product
- Category
- Quantity
- Price

## REST API Methods

### GET
Fetch order data.

### POST
Create a new order.

### PUT
Completely update an order.

### PATCH
Partially update an order.

### DELETE
Delete an order.

## REST API Features

- CRUD operations
- Path parameters
- Query parameters
- Request body
- Request headers
- JSON
- Response status codes
- Validation
- Error handling
- Filtering
- Searching
- Sorting
- Pagination

## JSON Concepts

- JSON objects
- JSON arrays
- JSON data types
- Python dictionary to JSON
- JSON to Python dictionary
- json.load()
- json.dump()
- json.dumps()
- json.loads()

## API Documentation

FastAPI provides Swagger/OpenAPI automatically.

Open:

http://127.0.0.1:8000/docs

## Run the API

```bash
uvicorn main:app --reload