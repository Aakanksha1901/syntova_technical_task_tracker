#  DATA STRUCTURES
# List, Tuple, Set, Dictionary and Strings
# Indexing, Slicing and Iteration


# LIST
# Create a list
flowers = ["Rose", "Lily", "Lotus"]
print(flowers)

# Access items
print(flowers[0])
print(flowers[-1])

# Slicing
print(flowers[0:2])

# Modify an item
flowers[1] = "Jasmine"
print(flowers)

# Add item using append()
flowers.append("Sunflower")
print(flowers)

# Add item using insert()
flowers.insert(1, "Marigold")
print(flowers)

# Add multiple items using extend()
more_flowers = ["Tulip", "Daisy"]
flowers.extend(more_flowers)
print(flowers)

# Remove item using remove()
flowers.remove("Lotus")
print(flowers)

# Remove item using pop()
flowers.pop()
print(flowers)


# Other list functions
print(len(flowers))
print(flowers.count("Rose"))
print(flowers.index("Rose"))

# Sort
flowers.sort()
print(flowers)

# Reverse
flowers.reverse()
print(flowers)

# Iterate over list
for flower in flowers:
    print(flower)

# Check item using if
if "Rose" in flowers:
    print("Rose is present")

# TUPLE

# Create a tuple
numbers = (10, 20, 30, 40, 50)
print(numbers)

# Access items
print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:4])

# Length
print(len(numbers))

# Count
print(numbers.count(20))

# Index
print(numbers.index(30))

# Iterate over tuple
for number in numbers:
    print(number)

# Check item
if 40 in numbers:
    print("40 is present")

# Tuple cannot be modified directly
# numbers[0] = 100

# Convert tuple into list to modify
number_list = list(numbers)
number_list[0] = 100
numbers = tuple(number_list)
print(numbers)

# Add item to tuple using list conversion
number_list = list(numbers)
number_list.append(60)
numbers = tuple(number_list)
print(numbers)


# SET

# Create a set
fruits = {"Apple", "Mango", "Orange"}
print(fruits)

# Duplicate values are ignored
fruits = {"Apple", "Mango", "Apple", "Orange"}
print(fruits)


# Length
print(len(fruits))


# Add item
fruits.add("Banana")
print(fruits)

# Add multiple items
more_fruits = {"Grapes", "Papaya"}
fruits.update(more_fruits)
print(fruits)

# Remove item using remove()
fruits.remove("Orange")
print(fruits)

# Remove item using discard()
fruits.discard("Papaya")
print(fruits)


# Pop an item
item = fruits.pop()
print("Removed:", item)
print(fruits)

# Check item
if "Apple" in fruits:
    print("Apple is present")


# Iterate over set
for fruit in fruits:
    print(fruit)


# Set operations
set1 = {"Apple", "Mango", "Orange"}
set2 = {"Mango", "Banana", "Grapes"}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))


#DICTIONARY

# Create a dictionary
student = {
    "name": "Aakanksha",
    "age": 25,
    "city": "Kolhapur"
}

print(student)

# Access value
print(student["name"])
print(student["city"])


# Add new key-value pair
student["course"] = "Python"
print(student)

# Modify value
student["age"] = 26
print(student)

# Update using update()
student.update({"city": "Pune"})
print(student)

# Get keys
print(student.keys())
print(student.values())

# Get both keys and values
print(student.items())

# using pop()
student.pop("course")
print(student)

# Remove using popitem()
student.popitem()
print(student)


# Iterate through keys
for key in student.keys():
    print(key)


# Iterate through values
for value in student.values():
    print(value)


# Iterate through both key and value
for key, value in student.items():
    print(key, value)


# Check key
if "name" in student:
    print("Name key is present")


# Nested dictionary
students = {
    "student1": {
        "name": "Aakanksha",
        "marks": 85
    },
    "student2": {
        "name": "Neha",
        "marks": 78
    }
}

print(students["student1"]["name"])


#  STRINGS

# Create a string

text = "Python Programming"

print(text)

# Indexing
print(text[0])
print(text[-1])

# Slicing

print(text[0:6])
print(text[7:18])
print(text[:6])
print(text[7:])


# String methods

print(text.upper())
print(text.lower())
print(text.replace("Python", "Data"))
print(text.split())
print(text.count("m"))
print(text.startswith("Python"))
print(text.endswith("ing"))
print(text.find("Program"))


# Iterate over string
for char in text:
    print(char)

# Check character using if
if "Python" in text:
    print("Python is present")


# String is immutable
#text[0] = "J"
