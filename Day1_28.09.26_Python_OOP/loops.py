# Loops

#  FOR LOOP 
for i in range(1, 6):
    print(i)

# FOR LOOP WITH LIST 
cities = ["Kolhapur", "Pune", "Sangli", "Satara"]
for city in cities:
    print(city)


# RANGE() 
for i in range(0, 10, 2):
    print(i)


# WHILE LOOP 
i = 2

while i <= 5:
    print(i)
    i += 1

# BREAK 
for i in range(1, 10):

    if i == 6:
        break

    print(i)


#  CONTINUE 
for i in range(1, 10):

    if i == 6:
        continue

    print(i)


# PASS
for i in range(1, 6):

    if i == 3:
        pass

    print(i)

#  SUM USING FOR LOOP
total = 0
for i in range(1, 11):
    total += i

print("Total:", total)

#  TABLE USING LOOP 
number = 5
for i in range(1, 11):
    print(number, "x", i, "=", number * i)


#  WHILE LOOP EXAMPLE 

count = 10
while count > 0:
    print("Count:", count)
    count -= 1
