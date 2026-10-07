import json


# READ JSON FILE
with open("data.json", "r") as file:

    data = json.load(file)


print("E-commerce Data:")
print(data)


# DISPLAY ORDERS
print("\nOrders:")

for order in data:

    print(
        order["product"],
        "-",
        order["category"],
        "-",
        order["price"]
    )

# ACCESS INDIVIDUAL VALUES
print("\nFirst Product:")
print(data[0]["product"])

print("\nFirst Product Price:")
print(data[0]["price"])


# PYTHON DICTIONARY → JSON
new_order = {

    "id": 6,
    "order_date": "2026-02-06",
    "product": "Tablet",
    "category": "Electronics",
    "quantity": 2,
    "price": 30000
}


json_data = json.dumps(
    new_order,
    indent=4
)


print("\nPython Dictionary → JSON:")
print(json_data)


# JSON - PYTHON DICTIONARY
python_data = json.loads(json_data)


print("\nJSON → Python Dictionary:")
print(python_data)

# ADD DATA TO JSON FILE
data.append(new_order)

with open("data.json", "w") as file:

    json.dump(
        data,
        file,
        indent=4
    )


print("\nNew order added to data.json")