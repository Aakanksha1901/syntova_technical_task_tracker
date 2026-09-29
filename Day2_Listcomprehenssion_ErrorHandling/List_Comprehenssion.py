# Basic List Comprehension
numbers = [1, 2, 3, 4, 5, 6 , 7, 8, 9 , 10]
squares = [x * x for x in numbers]

print(squares)


# With if Condition
# Get even - odd numbers:
numbers = [21 , 40 , 56 , 60 , 80 , 75 , 91, 85 ]

even = [x for x in numbers if x % 2 == 0]
odd =  [x for x in numbers if x % 2 == 1]
print("Even Numbers : ",even)
print("Odd Numbers :",odd)


# With if-else
numbers = [65 , 99 , 45 , 83 , 11 , 92 , 88 , 19  ]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)


#String List Comprehension
#Convert names to uppercase:
names = ["aakanksha", "sakshi", "neha"]

result = [name.upper() for name in names]

print("Names in Upper Case: ",result)

#String List Comprehension
#Convert names to uppercase:
names = ["AAKANKSHA", "SAKSHI", "NEHA"]
result = [name.lower() for name in names]

print("Names in Lower Case: ",result)

# Filtering Strings
names = ["Aakanksha", "Samruddhi","Pooja" ,"Sakshi", "Neha", "Roma"]
result = [name for name in names if len(name) > 5]

print(result)

# FILTER + TRANSFORM
numbers = [10 , 11 , 12 , 13 , 14 , 15]

# Filter even numbers then multiply them by 10
result = [x * 10 for x in numbers if x % 2 == 0]
print("Even numbers multiplied by 10:", result)


#LIST COMPREHENSION WITH FUNCTION
def cube(x):
    return x * x * x

numbers = [1, 2, 3, 4, 5]
result = [cube(x) for x in numbers]

print("Function:", result)


#  NESTED LIST COMPREHENSION
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Convert nested list into one list
result = [x for row in matrix for x in row]
print("Flattened list:", result)


#  NESTED LOOPS
numbers1 = [1, 2, 3]
numbers2 = [4, 5]

# combinations
result = [(x, y) for x in numbers1 for y in numbers2]
print("Combinations:", result)


#  MULTIPLE if CONDITIONS
numbers = range(1, 20)

# Get numbers that are:
#  Even and  Greater than 5
result = [
    x
    for x in numbers
    if x % 2 == 0
    if x > 6
]

print(" Multiple conditions:", result)


# MATRIX USING LIST COMPREHENSION
# Create a 3 x 3 matrix containing zeros
matrix = [[0 for j in range(3)] for i in range(3)]
print("Matrix:", matrix)


#  MULTIPLICATION TABLE / MATRIX
matrix = [
    [i * j for j in range(1, 4)]
    for i in range(2, 5)
]

print("Multiplication matrix:", matrix)


# NORMAL LOOP VS LIST COMPREHENSION
numbers = [1, 2, 3, 4, 5]

# Normal loop would be:
# result = []

# for x in numbers:
#     if x % 2 == 0:
#         result.append(x * 10)

# List comprehension:
result = [x * 10 for x in numbers if x % 2 == 0]

print(" Loop converted to comprehension:", result)

#  PASS / FAIL
marks = [80, 45, 30, 90, 35, 22 , 55 , 34 , 90 ]
result = [
    "Pass" if mark >= 40 else "Fail"
    for mark in marks
]

print(" Pass/Fail:", result)


#  POSITIVE / NEGATIVE
numbers = [-5, 10, -2, 8, -1, 7]

result = [
    "Positive" if x > 0 else "Negative"
    for x in numbers
]
print("Positive/Negative:", result)


# REMOVE EMPTY STRINGS
names = ["Aakanksha", "", "Sakshi", "", "Neha"]
result = [name for name in names if name != ""]

print(result)


# Example
products = [
    {"name": "Laptop", "price": 50000, "category": "Electronics"},
    {"name": "Shirt", "price": 1200, "category": "Clothing"},
    {"name": "Mobile", "price": 20000, "category": "Electronics"},
    {"name": "Shoes", "price": 2500, "category": "Clothing"}
]

product_names = [product["name"] for product in products]

print("Product names:", product_names)

electronics = [
    product["name"]
    for product in products
    if product["category"] == "Electronics"
]

print("Electronics:", electronics)