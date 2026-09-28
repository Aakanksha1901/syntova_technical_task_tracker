# CREATE AND CALL A FUNCTION
def my_function():
    print("Hello!! from a function")
my_function()

# FUNCTION WITH ONE PARAMETER
def greet(name):
    print("Hello", name)

greet("Aakanksha")

#  FUNCTION WITH MULTIPLE PARAMETERS
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)

# FUNCTION with RETURNS 
def get_greeting():
    return "Hello from a function"

print(get_greeting())

# RETURN VALUE
def add_numbers(a, b):
    print("Sum =", a + b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add_numbers(num1, num2)

#  DEFAULT PARAMETER VALUE
def greet_default(name="Guest"):
    print("Hello", name)


greet_default()
greet_default("Aakanksha")

# KEYWORD ARGUMENTS

def flower_details(flower, color):
    print("I have a", flower)
    print(flower, "with", color, "petals is my favourite")


flower_details(flower="Lily", color="white")


# LIST AS AN ARGUMENT

def print_fruits(fruits):

    for fruit in fruits:
        print(fruit)


my_fruits = ["apple", "banana", "cherry"]

print_fruits(my_fruits)


# DICTIONARY AS AN ARGUMENT

def print_person(person):

    print("Name:", person["name"])
    print("Age:", person["age"])


my_person = {
    "name": "Aakanksha",
    "age": 25
}

print_person(my_person)


#  FUNCTION THAT RETURNS A LIST

def get_fruits():
    return ["apple", "banana", "cherry"]

fruits = get_fruits()

print(fruits[0])
print(fruits[1])
print(fruits[2])

#  FUNCTION THAT RETURNS A TUPLE

def get_coordinates():
    return (40, 20)


x, y = get_coordinates()

print("x:", x)
print("y:", y)


#  *args

def my_args(*args):

    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)


my_args("Aakanksha", "Python", "SQL")


#  SUM USING *args

def total(*numbers):

    result = 0

    for num in numbers:
        result += num

    return result


print(total(1, 2, 3))
print(total(10, 20, 30, 40))
print(total(5))


#  MULTIPLICATION USING *args

def multiply_all(*numbers):

    result = 1

    for num in numbers:
        result *= num

    return result


print(multiply_all(1, 2, 3, 4, 5))


#  MAXIMUM USING *args

def find_max(*numbers):

    if len(numbers) == 0:
        return None

    max_num = numbers[0]

    for num in numbers:

        if num > max_num:
            max_num = num

    return max_num

print(find_max(3, 7, 2, 9, 1))


#  MINIMUM USING *args
def find_min(*numbers):

    if len(numbers) == 0:
        return None

    min_num = numbers[0]

    for num in numbers:

        if num < min_num:
            min_num = num

    return min_num

print(find_min(3, 7, 2, 9, 1))


#  * UNPACKING
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

result = add_three(*numbers)

print(result)

#  ** DICTIONARY UNPACKING

def greet_person(fname, lname):
    print("Hello", fname, lname)

person = {
    "fname": "Aakanksha",
    "lname": "Pednekar"
}

greet_person(**person)

#  FUNCTION AS AN ARGUMENT
def square(x):
    return x * x


def apply(fun, value):
    return fun(value)

print(apply(square, 5))

#  FUNCTION AS AN ARGUMENT - ADD

def add_number(num):
    return 10 + num

def apply_number(fun, value):
    return fun(value)

print(apply_number(add_number, 6))

#  FUNCTION AS AN ARGUMENT - ADD AND MULTIPLY

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def calculate(fun, x, y):
    return fun(x, y)

print(calculate(add_numbers, 5, 6))
print(calculate(multiply_numbers, 5, 6))

#  FUNCTION AS AN ARGUMENT - UPPERCASE

def upper(text):
    return text.upper()

def apply_upper(fun, value):
    return fun(value)

print(apply_upper(upper, "apple"))

#  CALCULATOR USING FUNCTIONS

def add_calc(x, y):
    return x + y

def difference_calc(x, y):
    return x - y

def multiply_calc(x, y):
    return x * y

def divide_calc(x, y):
    return x / y

def operate(fun, a, b):
    return fun(a, b)

print(operate(add_calc, 20, 5))
print(operate(difference_calc, 10, 5))
print(operate(multiply_calc, 20, 4))
print(operate(divide_calc, 40, 5))


#  FUNCTION INSIDE FUNCTION

def outer():

    print("Outer")

    def inner():
        print("Inner")

    inner()


outer()

#  EVEN OR ODD

def check_even_odd(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_odd(7))

# MAXIMUM OF TWO NUMBERS

def find_max_two(a, b):

    if a > b:
        return a
    else:
        return b


print(find_max_two(10, 25))

#  CELSIUS TO FAHRENHEIT

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

print(celsius_to_fahrenheit(25))

#  POSITIVE, NEGATIVE OR ZERO

def check_number(num):

    if num > 0:
        return "Positive"

    elif num < 0:
        return "Negative"

    else:
        return "Zero"

print(check_number(-3))

#  REVERSE A STRING
# ============================================================

def reverse_string(text):
    return text[::-1]


print(reverse_string("Python"))


#  FACTORIAL USING RECURSION
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

# FIBONACCI USING RECURSION
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))