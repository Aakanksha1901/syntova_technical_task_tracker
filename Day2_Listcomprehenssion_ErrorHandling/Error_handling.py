# ERROR HANDLING
# Basic try-except
try:
    age = int("25")
    print("Age:", age)

except ValueError:
    print("Invalid age")


# Handling ValueError
try:
    age = int("twenty")
    print(age)

except ValueError:
    print("Please enter a valid age")


# Handling ZeroDivisionError
try:
    percentage = 500 / 0
    print(percentage)

except ZeroDivisionError:
    print("Cannot divide by zero")


# Handling multiple exceptions
try:
    quantity = int("abc")
    price = 100 / quantity
    print(price)

except ValueError:
    print("Please enter a valid quantity")

except ZeroDivisionError:
    print("Quantity cannot be zero")


# Getting the actual error message
try:
    result = 50 / 0

except ZeroDivisionError as error:
    print("Error:", error)


# try-except-else-finally
# else runs when there is no error
try:
    age = int("21")

except ValueError:
    print("Invalid age")

else:
    print("Age entered successfully:", age)


# finally always runs
try:
    number = int("500")

except ValueError:
    print("Invalid number")

finally:
    print("Input operation completed")


# Complete try-except-else-finally
try:
    price = int("500")
    quantity = int("2")

    total = price * quantity

except ValueError:
    print("Invalid input")

except TypeError:
    print("Invalid data type")

else:
    print("Total price:", total)

finally:
    print("Calculation finished")


# KeyError
product = {
    "name": "Laptop",
    "price": 50000
}

try:
    category = product["category"]

except KeyError:
    print("Category is missing")


# IndexError
cities = ["Pune", "Mumbai", "Nashik"]

try:
    print(cities[5])

except IndexError:
    print("City index does not exist")


# TypeError
try:
    total = 100 + "200"

except TypeError:
    print("Cannot add integer and string")


# ERROR HANDLING WITH FUNCTIONS
# Safe division function
def calculate_average(total, count):

    try:
        return total / count

    except ZeroDivisionError:
        return "Count cannot be zero"

    except TypeError:
        return "Invalid data type"
print("Average:", calculate_average(500, 5))
print("Average:", calculate_average(500, 0))


#  float conversion
def convert_to_float(value):

    try:
        return float(value)

    except ValueError:
        return "Invalid decimal number"

print("Conversion:", convert_to_float("25.5"))
print("Conversion:", convert_to_float("hello"))


# raise
# Using raise for validation
def check_age(age):

    if age < 18:
        raise ValueError("Age must be 18 or above")

    return age

print("Age:", check_age(20))

# with try-except
def check_age(age):

    if age < 18:
        raise ValueError("Age must be 18 or above")

    return age


try:
    print("Age:", check_age(25))
    print("Age:", check_age(16))

except ValueError as error:
    print("Error:", error)

# ERROR HANDLING WITH LIST OF DICTIONARIES
# Safely access product price
products_with_missing_data = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mobile"},
    {"name": "Tablet", "price": 25000}
]


def get_price(product):

    try:
        return product["price"]

    except KeyError:
        return None


for product in products_with_missing_data:

    price = get_price(product)

    if price is not None:
        print(product["name"], "Price:", price)

    else:
        print(product["name"], "Price not available")