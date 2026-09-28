# Class and Object
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

#multiple objects
class MyClass:
    x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# empty class using pass
class Employee:
    pass
p1 = Employee()

# __init__() Constructor
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Employee("Aakanksha", 22)

print(p1.name)
print(p1.age)

# default values in __init__()
class Employee:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
p1 = Employee("Aakanksha")
p2 = Employee("Amit", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

# multiple parameters
class Employee:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Employee("Aakanksha", 22, "Kolhapur", "India")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

#  self
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

p1 = Employee("Aakanksha", 22)
p1.greet()

# accessing properties using self
class Laptop:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(self.year, self.brand, self.model)


laptop1 = Laptop("Dell", "Inspiron 15", 2024)

laptop1.display_info()


# calling one method from another using self
class Employee:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")

p1 = Employee("Aakanksha")
p1.welcome()


# Instance Properties
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Employee("Aakanksha", 22)

print(p1.name)
print(p1.age)

# modifying instance properties
p1.age = 23

print(p1.age)

# adding new properties to an object
p1.city = "Kolhapur"

print(p1.city)

# deleting an instance property
del p1.city

# print(p1.city)

# Instance Methods

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()

print(calc.add(5, 3))
print(calc.multiply(4, 7))

# method accessing and modifying properties

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

    def celebrate_birthday(self):
        self.age += 1
        print("Happy birthday! You are now", self.age)

p1 = Employee("Aakanksha", 22)

print(p1.get_info())

p1.celebrate_birthday()
p1.celebrate_birthday()

# multiple methods

class ShoppingCart:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def show_items(self):
        print("ShoppingCart:", self.name)

        for item in self.items:
            print(item)

cart = ShoppingCart("My Cart")

cart.add_item("Laptop")
cart.add_item("Mouse")

cart.show_items()

cart.remove_item("Laptop")

cart.show_items()


# 6. Class Variable vs Instance Variable

class Employee:
    species = "Human"

    def __init__(self, name):
        self.name = name

p1 = Employee("Aakanksha")
p2 = Employee("Amit")

print(p1.name)
print(p2.name)

print(p1.species)
print(p2.species)


# modifying class variable

Employee.species = "Human Being"

print(p1.species)
print(p2.species)


# 7. Class Methods

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

print(Student.school)

Student.change_school("XYZ School")

print(Student.school)


# 8. Static Methods

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(Calculator.add(5, 3))
print(Calculator.multiply(4, 5))


# 9. __str__() Method

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Employee("Aakanksha", 22)

print(p1)


# 10. Deleting Objects and Methods

class Employee:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello")

p1 = Employee("Aakanksha")

del p1

# print(p1)


# deleting a method from a class

class Employee:
    def greet(self):
        print("Hello")

del Employee.greet

# p1 = Employee()
# p1.greet()


# 11. Encapsulation - Public Variable

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Aakanksha", 85)

s1.display()

print(s1.name)
print(s1.marks)


# 12. Protected Variable

class Employee:
    def __init__(self, salary):
        self._salary = salary

    def show_salary(self):
        print("Salary:", self._salary)

emp = Employee(50000)

emp.show_salary()

print(emp._salary)


# 13. Private Variable

class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

account = Wallet(10000)

account.show_balance()

# print(account.__balance)


# 14. Getter and Setter

class Employee:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

p = Employee(25)

print(p.get_age())

p.set_age(30)

print(p.get_age())


# 15. Encapsulation with Validation

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

s = Student("Aakanksha", 70)

print(s.get_marks())

s.set_marks(95)

print(s.get_marks())


# 16. Private Method

class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        return isinstance(num, (int, float))

    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

calc = Calculator()

calc.add(10)
calc.add(5)

print(calc.result)

# calc.__validate(5)


# 17. Encapsulation - Bank Account

class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

acc = Wallet(5000)

acc.deposit(1000)
acc.withdraw(2000)

print(acc.get_balance())


# 18. Inheritance

# parent class

class Employee:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)


# child class

class Student(Employee):
    def study(self):
        print(self.name, "is studying")

s = Student("Aakanksha")

s.greet()
s.study()


# 19. Inheritance with Constructor

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)


class Student(Employee):
    pass

s = Student("Aakanksha", 22)

s.show_info()


#  Single Inheritance

class Device:

    def start(self):
        print("Device started")


class Laptop(Device):

    def work(self):
        print("Laptop is working")


laptop = Laptop()

laptop.start()
laptop.work()


#  Multilevel Inheritance

class Grandparent:
    def show_grandparent(self):
        print("Grandparent")


class Parent(Grandparent):
    def show_parent(self):
        print("Parent")


class Child(Parent):
    def show_child(self):
        print("Child")


c = Child()

c.show_grandparent()
c.show_parent()
c.show_child()

#  Hierarchical Inheritance

class Device:

    def start(self):
        print("Device started")


class Laptop(Device):

    def work(self):
        print("Laptop is working")


class Mobile(Device):

    def call(self):
        print("Mobile is calling")


laptop = Laptop()
mobile = Mobile()

laptop.start()
laptop.work()

mobile.start()
mobile.call()

#  Multiple Inheritance

class Father:
    def father_skill(self):
        print("Gardening and Driving")


class Mother:
    def mother_skill(self):
        print("Cooking and Painting")


class Child(Father, Mother):
    pass


c = Child()

c.father_skill()
c.mother_skill()


# calling both parent methods explicitly

class Father:
    def skills(self):
        print("Gardening, Driving")


class Mother:
    def skills(self):
        print("Cooking, Painting")


class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)


c = Child()

c.skills()


# super()

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Student(Employee):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show(self):
        super().show()
        print("Course:", self.course)


s = Student("Aakanksha", "Data Science")

s.show()


# super() with parent method

class Employee:
    def show(self):
        print("I am a person")


class Student(Employee):
    def show(self):
        super().show()
        print("I am a student")


s = Student()

s.show()

#  Method Overriding

class Flower:
    def smell(self):
        print("Flower has a pleasant smell")


class Rose(Flower):
    def smell(self):
        print("Rose has a sweet smell")


class Lily(Flower):
    def smell(self):
        print("Lily has a fresh smell")


rose = Rose()
lily = Lily()

rose.smell()
lily.smell()

#  Polymorphism

# 26. Polymorphism

class Apple:

    def taste(self):
        print("Apple is sweet!")


class Mango:

    def taste(self):
        print("Mango is juicy!")


class Orange:

    def taste(self):
        print("Orange is sour!")


apple = Apple()
mango = Mango()
orange = Orange()

for fruit in (apple, mango, orange):
    fruit.taste()


# Polymorphism with Inheritance

# 27. Polymorphism with Inheritance

class Vehicle:

    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Car is driving")


class Boat(Vehicle):
    def move(self):
        print("Boat is sailing")


class Plane(Vehicle):
    def move(self):
        print("Plane is flying")


vehicles = [Car(), Boat(), Plane()]

for vehicle in vehicles:
    vehicle.move()


# Polymorphism with Different Objects

class India:
    def capital(self):
        print("New Delhi")


class USA:
    def capital(self):
        print("Washington D.C.")


countries = [India(), USA()]

for country in countries:
    country.capital()


# 29. Duck Typing

class Laptop:
    def code(self):
        print("Coding in Python")


class Mobile:
    def code(self):
        print("Coding in App")


def developer(device):
    device.code()


laptop = Laptop()
mobile = Mobile()

developer(laptop)
developer(mobile)


# 30. Polymorphism with Function

class Bird:
    def fly(self):
        print("Bird can fly")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")


class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")


birds = [Sparrow(), Ostrich()]

for bird in birds:
    bird.fly()


#  Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle")


class Triangle(Shape):
    def area(self):
        print("Area of Triangle")


shapes = [Rectangle(), Triangle()]

for shape in shapes:
    shape.area()


#  Abstraction with Real Example

from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTime(Employee):
    def calculate_salary(self):
        return 50000

class PartTime(Employee):
    def calculate_salary(self):
        return 20000

class Intern(Employee):
    def calculate_salary(self):
        return 10000

employees = [FullTime(), PartTime(), Intern()]

for employee in employees:
    print("Salary:", employee.calculate_salary())


# isinstance()
class Fruit:
    pass

class Bike(Fruit):
    pass

dog = Bike()

print(isinstance(dog, Bike))
print(isinstance(dog, Fruit))
print(isinstance(dog, object))

#  __str__() Special Method
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p = Employee("Aakanksha", 22)

print(p)

# __len__() Special Method
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["Aakanksha", "Amit", "Rahul"])

print(len(team))

#__add__() Special Method
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

# Property Decorator
class Employee:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Invalid age")


p = Employee(22)
print(p.age)
p.age = 25
print(p.age)


#  Real-World OOP Example
class Wallet:

    wallet_type = "Digital Wallet"

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Wallet Holder: {self.name}, Balance: {self.__balance}"


wallet = Wallet("Aakanksha", 5000)

wallet.deposit(1000)
wallet.withdraw(2000)

print(wallet.get_balance())
print(wallet)