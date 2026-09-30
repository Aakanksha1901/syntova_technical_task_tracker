# THEORY:

# Asynchronous programming allows a program to work on other tasks  while waiting for an operation such as an API, database, network or file operation.

# Synchronous:
# Task 1 -> wait -> finish -> Task 2
#
# Asynchronous:
# Task 1 -> waiting
# Task 2 -> can run while Task 1 is waiting
#
# asyncio is Python's built-in library for asynchronous programming.

import asyncio


# Basic Async Function - async def creates an asynchronous function

# An async function is created using async def.
# asyncio.run() is used to execute an async function.
async def welcome():
    print("Welcome to the shopping application")

asyncio.run(welcome())


# await - waits for an asynchronous operation to complete

# await is used inside an async function.
# It waits for an asynchronous operation to complete.
# While waiting, the event loop can handle other tasks.
async def load_employee():
    print("Loading employee information")
    await asyncio.sleep(2)
    print("Employee information loaded")

asyncio.run(load_employee())


# asyncio.sleep() - provides a non-blocking wait

# THEORY:
# asyncio.sleep() pauses the current async task without
# blocking the entire event loop.

# It can simulate waiting for:
# API response
# Database response
# Network operation
# File operation

async def process_payment():
    print("Payment processing started")
    await asyncio.sleep(3)
    print("Payment processing completed")

asyncio.run(process_payment())


# Async Function with Parameters - async functions can accept parameters and return data
async def get_employee(employee_id):
    await asyncio.sleep(1)

    return {
        "id": employee_id,
        "name": "Sneha",
        "department": "Finance"
    }

async def main_employee():
    employee = await get_employee(205)
    print("Employee:", employee)

asyncio.run(main_employee())


#  Async Function Returning Data - async functions can return lists, dictionaries, and other values
async def get_orders():
    await asyncio.sleep(2)
    return [2500, 1750, 3200, 1450]

async def main_orders():
    orders = await get_orders()
    total = sum(orders)

    print("Orders:", orders)
    print("Total Sales:", total)

asyncio.run(main_orders())


#  Sequential Execution - async tasks can execute one after another
async def employee_task():
    print("Employee task started")
    await asyncio.sleep(2)
    print("Employee task completed")


async def shopping_task():
    print("Shopping task started")
    await asyncio.sleep(2)
    print("Shopping task completed")


async def main_sequential():
    await employee_task()
    await shopping_task()

asyncio.run(main_sequential())


#  asyncio.gather() - runs multiple independent async operations concurrently
async def check_inventory():
    print("Checking inventory")
    await asyncio.sleep(2)
    print("Inventory checked")
    return "Inventory available"


async def check_delivery():
    print("Checking delivery")
    await asyncio.sleep(2)
    print("Delivery checked")
    return "Delivery available"


async def main_gather():
    inventory, delivery = await asyncio.gather(
        check_inventory(),
        check_delivery()
    )

    print(inventory)
    print(delivery)

asyncio.run(main_gather())


#  Multiple Async Operations - multiple independent operations can run concurrently
async def fetch_customers():
    await asyncio.sleep(2)
    return ["Aakanksha", "Raj", "Sakshi"]


async def fetch_products():
    await asyncio.sleep(2)
    return ["Headphones", "Smartwatch", "Backpack"]


async def fetch_orders():
    await asyncio.sleep(2)
    return [501, 502, 503]


async def main_data():
    customers, products, orders = await asyncio.gather(
        fetch_customers(),
        fetch_products(),
        fetch_orders()
    )

    print("Customers:", customers)
    print("Products:", products)
    print("Orders:", orders)

asyncio.run(main_data())


#  asyncio.create_task() - schedules an async operation to run as a task
async def calculate_salary():
    await asyncio.sleep(3)
    return "Salary calculated"


async def generate_attendance():
    await asyncio.sleep(1)
    return "Attendance report generated"


async def main_tasks():
    salary_task = asyncio.create_task(calculate_salary())
    attendance_task = asyncio.create_task(generate_attendance())

    salary_result = await salary_task
    attendance_result = await attendance_task

    print(salary_result)
    print(attendance_result)

asyncio.run(main_tasks())


#  Event Loop - manages and schedules asynchronous tasks
async def payment_api():
    await asyncio.sleep(2)
    return "Payment API response"


async def delivery_api():
    await asyncio.sleep(4)
    return "Delivery API response"


async def main_event_loop():
    results = await asyncio.gather(
        payment_api(),
        delivery_api()
    )

    print("API Results:", results)

asyncio.run(main_event_loop())


#  Async Error Handling - try and except handle errors in async functions
async def process_order():
    await asyncio.sleep(1)
    raise ValueError("Order amount is invalid")


async def main_error():
    try:
        await process_order()

    except ValueError as error:
        print("Error:", error)

asyncio.run(main_error())


#  try-except-finally - finally runs whether an error occurs or not
async def connect_database():
    print("Connecting to employee database...")
    await asyncio.sleep(2)

    raise ConnectionError("Unable to connect to database")


async def main_database():
    try:
        await connect_database()

    except ConnectionError as error:
        print("Error:", error)

    finally:
        print("Database connection process completed")

asyncio.run(main_database())


#  Error Handling with gather() - exceptions from concurrent tasks can be handled
async def get_customer_data():
    await asyncio.sleep(1)
    return "Customer data received"


async def get_payment_data():
    await asyncio.sleep(1)
    raise ValueError("Payment information is invalid")


async def main_gather_error():
    try:
        customer, payment = await asyncio.gather(
            get_customer_data(),
            get_payment_data()
        )

        print(customer)
        print(payment)

    except ValueError as error:
        print("Error:", error)

asyncio.run(main_gather_error())


#  asyncio.wait_for() - sets a maximum time for an async operation
async def delivery_status():
    print("Checking delivery status")
    await asyncio.sleep(6)
    print("Delivery status received")


async def main_timeout():
    try:
        await asyncio.wait_for(
            delivery_status(),
            timeout=3
        )

    except asyncio.TimeoutError:
        print("Delivery API took too long")

asyncio.run(main_timeout())



#  Async Loop - an async function can process multiple items using a loop
async def display_products():
    products = [
        "Tablet",
        "Bluetooth Speaker",
        "Running Shoes",
        "Water Bottle",
        "Keyboard"
    ]

    for product in products:
        print("Processing:", product)
        await asyncio.sleep(0.5)

asyncio.run(display_products())


#  Concurrent Data Processing - tasks can process multiple independent items concurrently
async def process_category(category):
    await asyncio.sleep(1)
    return f"{category} processed"


async def main_processing():
    categories = [
        "Electronics",
        "Clothing",
        "Books",
        "Home Decor"
    ]

    tasks = [
        asyncio.create_task(process_category(category))
        for category in categories
    ]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

asyncio.run(main_processing())

# Real world Use Case - 

# Weather Details
async def get_weather(city):
    print(f"Getting weather for {city}...")

    # Pretend this is an API request
    await asyncio.sleep(2)

    weather = {
        "Mumbai": {"temperature": 30, "condition": "Cloudy"},
        "Pune": {"temperature": 27, "condition": "Sunny"},
        "Delhi": {"temperature": 32, "condition": "Clear"},
        "Bangalore": {"temperature": 24, "condition": "Rainy"}
    }

    details = weather[city]

    print(
        f"Weather received for {city}: "
        f"{details['temperature']}°C, {details['condition']}"
    )

async def main():
    await asyncio.gather(
        get_weather("Mumbai"),
        get_weather("Pune"),
        get_weather("Delhi"),
        get_weather("Bangalore")
    )

asyncio.run(main())


# Shopping Website
async def get_price(website):
    print(f"Checking {website}...")

    # Pretend this is an API request
    await asyncio.sleep(2)

    prices = {
        "Website 1": 18999,
        "Website 2": 19499,
        "Website 3": 18499
    }

    price = prices[website]

    print(f"Price received from {website}: ₹{price}")


async def main():
    await asyncio.gather(
        get_price("Website 1"),
        get_price("Website 2"),
        get_price("Website 3")
    )


asyncio.run(main())