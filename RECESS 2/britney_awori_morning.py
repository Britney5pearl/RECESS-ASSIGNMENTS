#DAY 4 OOP PYTHON
#Key Concepts
#CLASS
#This is a blue print for creating objects

#Example1: Car

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine strarted")

    def stop_engine(self):
        print("Engine stopped")

my_car = Car("toyota", "corolla", 2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()

#Example2: Bank account
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print("Account number:", self.account_number)
        print("Balance:", self.balance)
        
#Create a bank account object
my_account = BankAccount("123455679", 200000)

#Perform operations on the Bank Account object
my_account.display_balance()
my_account.deposit(5000)
my_account.withdraw(2000)
my_account.display_balance()
#Example 3: Rectangle 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2* (self.length + self.width)
    
#Create an object for recttangle
my_rectangle = Rectangle(12, 3)
print(my_rectangle.length)
print(my_rectangle.width)
#calculate and dispaly the area of the rectangle and perimeter
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())


#Example 4: unversity student
class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

    def display_details(self):
        print("Name:",self.name)
        print("Year:",self.year)
        print("Course:",self.course)

#Create a student object
my_student = Student("Pearl", 3, "Software engineering")

#Display student details
my_student.display_details()

# Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)
        print("I am", self.age, "years old")

# create a person object

my_person1 = Person("Sandra", 34)
my_person2 = Person("Angella", 27)

#  Access the Person object's attributes
print(my_person1.name)
print(my_person1.age)
print(my_person2.name)
print(my_person2.age)

# Invoke our object method
my_person1.greet()
my_person2.greet()

#Calculate the area and circumference of a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
    def calculate_circumference(self):
        return 2 * 3.14 * self.radius
#create a circle object

my_circle = Circle(20)
print(my_circle.radius)
print(my_circle.calculate_area())
print(my_circle.calculate_circumference())

#Exercise 1
#Calculate and display employee's bonuses(15%) of salary (employee1: 150000, employee2: 230000)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.15


# Creating employee instances
employee1 = Employee("John Doe", 150000)
employee2 = Employee("Jane Smith", 230000)

# Calculating and displaying bonuses
bonus1 = employee1.calculate_bonus()
bonus2 = employee2.calculate_bonus()

print(f"Employee: {employee1.name}, Salary: {employee1.salary}, Bonus: {bonus1}")
print(f"Employee: {employee2.name}, Salary: {employee2.salary}, Bonus: {bonus2}")

#Encapsulation
#Key main goal of encapsulation are
"""
1. To ride the implementation details of an object
2. To protect the object from changes
3. To protect the object from external changes
4. Code organisation and modularity
"""

#Example with a bank account
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance #encapsulates the balance attribute

    def deposit(self, amount):
        self._balance += amount #Encapsulates the deposit

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self._balance
    
#create a bank object
my_account = BankAccount("1234455668", 300000)

#Access the Bank object and modify encapsulated attributes indirectly
print(my_account._account_number)
print(my_account._balance)
my_account.deposit(5000)
print(my_account._balance)
my_account.withdraw(4000)
print(my_account._balance)

# Exercise 2: Convert temperature(37) from celcius to Fahrenheit
class TemperatureConverter:
    def __init__(self, temperature):
        self._temperature = temperature

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature

    def celsius_to_fahrenheit(self):
        return (self.get_temperature() * 9/5) + 32


# Creating a TemperatureConverter instance
converter = TemperatureConverter(37)

# Displaying the initial temperature in Celsius
print(f"Temperature in Celsius: {converter.get_temperature()}")

# Converting the temperature to Fahrenheit
fahrenheit_temp = converter.celsius_to_fahrenheit()

# Displaying the converted temperature in Fahrenheit
print(f"Temperature in Fahrenheit: {fahrenheit_temp}")


# Assignment1: Show encapsulation with employee information to give a pay incrementation (Salary with employee information to new salary)e.g from 850000 to 1000000
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def give_increment(self, increment_amount):
        current_salary = self.get_salary()
        new_salary = current_salary + increment_amount
        self.set_salary(new_salary)


# Creating an employee instance
employee = Employee("John Doe", 850000)

# Displaying the initial salary
print(f"Initial Salary: {employee.get_salary()}")

# Giving increment of 150000
employee.give_increment(150000)

# Displaying the new salary
print(f"New Salary: {employee.get_salary()}")

