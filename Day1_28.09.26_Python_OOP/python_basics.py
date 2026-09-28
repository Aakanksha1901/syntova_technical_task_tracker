#  PYTHON BASICS
#  VARIABLES 
name = "Aakanksha"
age = 25
salary = 45000.50
is_student = True

print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Student:", is_student)


#  DATA TYPES 
print(type(name))        # str
print(type(age))         # int
print(type(salary))      # float
print(type(is_student))  # bool


#  TYPE CONVERSION 
number = "100"

print(type(number))

number = int(number)

print(number)
print(type(number))

price = 250
price = float(price)

print(price)
print(type(price))

age = 25
age_text = str(age)

print(age_text)
print(type(age_text))


# INPUT / OUTPUT

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello", user_name)
print("Your age is", user_age)

print(f"My name is {user_name} and I am {user_age} years old.")

# ARITHMETIC OPERATORS 

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)
print("Power:", a ** 2)
print("Floor Division:", a // b)

# ASSIGNMENT OPERATORS 

number = 10

number += 5
print("After += :", number)

number -= 2
print("After -= :", number)

number *= 2
print("After *= :", number)

number /= 2
print("After /= :", number)


# COMPARISON OPERATORS 
x = 10
y = 20

print(x == y)
print(x != y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)

# LOGICAL OPERATORS
age = 25
salary = 45000

print(age >= 18 and salary >= 30000)
print(age >= 30 or salary >= 30000)
print(not False)

#  MEMBERSHIP OPERATORS 
skills = ["Python", "SQL", "Excel"]

print("Python" in skills)
print("Java" not in skills)

# ]IDENTITY OPERATORS 
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)
