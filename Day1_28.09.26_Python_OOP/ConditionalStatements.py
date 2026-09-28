# CONDITIONAL STATEMENTS
#  IF 
age = 25
if age >= 18:
    print("Aakanksha is an adult")

# IF ELSE 
marks = 72

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# IF ELIF ELSE 
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# EVEN / ODD 
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#  POSITIVE / NEGATIVE / ZERO 

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#  LARGER OF TWO NUMBERS 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is larger")
elif b > a:
    print("Second number is larger")
else:
    print("Both numbers are equal")

# NESTED IF 
age = int(input("Enter a Age: "))
has_id = True

if age >= 18:
    print("Age is valid")

    if has_id:
        print("ID is available")
    else:
        print("ID is not available")

else:
    print("Age is below 18")


# CONDITIONAL EXPRESSION
marks = 78
result = "Pass" if marks >= 40 else "Fail"
print(result)

# another conditional expression
number = 15
message = "Positive" if number > 0 else "Negative or Zero"
print(message)
