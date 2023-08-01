#Inheritance

class Animal:
   def __init__(self, name):
    self.name = name 
   
        
   def eat(self):
       print(f"{self.name} is eating...")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking...Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name}is meowing...")


# Create Animal Objects
animal = Animal("Generic Animal")
dog = Dog("Spot")
cat = Cat("Fluffy")

# Invoke Call Eat Method
animal.eat()
dog.eat()
dog.bark()
cat.eat()
cat.meow()


#Example2: Demonstrating inheritance
class Vehicle:
    def _init_(self, brand, color):
        self.brand = brand
        self.color = color
        
    def display_info(self):
        print("Brand:", self.brand)
        print("Color:", self.color)

    def move(self):
        print("Moving the vehicle...")

class Car(Vehicle):
    def __init__(self, brand, color, num_wheels):
        super()._init_(brand, color)
        self.num_wheels = num_wheels

    def display_info(self):
         super().display_info() 
         print("Number of Wheels:", self.num_wheels) 

         def honk(self):
             print("Honking the horn...")


# Create a Car object
my_car = Car("Toyota", "Red", 4)

# Access and modify the car attributes
print("Brand:", my_car.brand)  #Output: Brand: Toyota
my_car.color = "Gray"

# Invoke the car methods
my_car.display_info()
my_car.move()

# Exercise1
# Demonstrate using inheritance to calculate area and perimeter respectively (Shape: Circle)
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Create a circle object
circle = Circle(5)

# Calculate and print the area of the circle
area = circle.area()
print("Area of the circle:", area)

# Calculate and print the perimeter of the circle
perimeter = circle.perimeter()
print("Perimeter of the circle:", perimeter)

# Example3
# Multiple Inheritance
class Animal:
    def _init_(self, name):
        self.name = name

        def eat(self):
            print(f"{self.name} is eating...")

class Flyable:
    def fly(self):
        print(f"{self.name} is flying...")     

class Bird(Animal, Flyable):
    def __init__(self, name, species, wings):
        super()._init_(name)
        self.species = species

    def eat(self):
        print(f"{self.name} the {self.species} is eating.")        

    def display_info(self):
        super().display_info()
        print(f"Species: {self.species}")    
        print(f"Name: {self.name}") 


 # Create a Bird object
my_bird = Bird("Pigeon", "bird", 2) 

# Invoke the Bird methods
my_bird.eat()
my_bird.fly()


# Method Overriding

class Animal:
    def make_sound(self):
        print("Animal is making a sound!")

class Dog(Animal):
    def make_sound(self):
        print("Dog is barking!")

class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing!")

def make_animal_sound(animal):
    animal.make_sound()

# Create a object
animal = Animal()
dog = Dog()
cat = Cat()

# Calling make_animal_sound function
make_animal_sound(animal)  # Output: Animal is making a sound!
make_animal_sound(dog)  # Output: Dog is barking!
make_animal_sound(cat)  # Output: Cat is meowing!

# Polymorphism allows you to write code that works with different objects

# Methods Overriding occurs when a derived class, subclass, {child class}, provides its own
# Implementation of a method that is already defined in its base class, super class
# Method Overloading allows a class to have multiple methods with the same name but different parameters

# Example4
class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

        def calculate_area(self):
            return 3.14 * self.radius**2

        def calculate_circumference(self):
            return 2 * 3.14 * self.radius
        

# Create shape Objects
rectangle = Rectangle(5, 5)
circle = Circle(15)      


# Calculate Display Area
print("Rectangle area:", rectangle.calculate_area())   
print("Circle area:", circle.calculate_area())   


# Overloading functions
class calculator:
    def add(self, x, y):
        return x + y
    
    def add(self, x, y, c):
        return x + y + c

# Abstraction
# Allow you to focus on essential features and hide them from unnecessary details

# Example5: Demonstrate abstractions

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Starting the car...")

        def stop(self):
            print("Stopping the car...")


class Truck(Vehicle):
    def start(self):
        print("Starting the truck...")  

    def stop(self):
        print("Stopping the truck...")    

# Create Vehicle Objects
car = Car()
truck = Truck() 


# Start the Vehicle
car.start()
truck.start()

# Stop the truck
truck.stop()
car.stop()



# Exercise2: Demonstrate abstraction using calculating area of a circle and rectangle
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create a circle object
circle = Circle(5)

# Calculate and print the area of the circle
circle_area = circle.area()
print("Area of the circle:", circle_area)

# Create a rectangle object
rectangle = Rectangle(3, 4)

# Calculate and print the area of the rectangle
rectangle_area = rectangle.area()
print("Area of the rectangle:", rectangle_area)

# How to name your file when sending to my email jeff.geoff.cis@gmail.com
# Accepted Format: firstname_surname_morning.py | firstname_surname_afternoon.py

#Assignment 1: Create a receipt printing program with GUI interface,
# a more advanced detail earns you more points.
import tkinter as tk

def print_receipt():
    # Clear previous receipt
    receipt_text.config(state=tk.NORMAL)
    receipt_text.delete("1.0", tk.END)

    # Get input values
    try:
        customer_name = name_entry.get().strip()
        item = item_entry.get().strip()
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
    except ValueError:
        receipt_text.insert(tk.END, "Invalid input. Please enter valid values.")
        receipt_text.config(state=tk.DISABLED)
        return

    # Calculate total
    total = price * quantity

    # Generate receipt string with formatting
    receipt_text.insert(tk.END, f"{'-' * 30}\n")
    receipt_text.insert(tk.END, f"{'Receipt':^30}\n")
    receipt_text.insert(tk.END, f"{'-' * 30}\n\n")
    receipt_text.insert(tk.END, f"{'Customer Name:':<15}{customer_name:<15}\n\n")
    receipt_text.insert(tk.END, f"{'Item:':<15}{item:<15}\n")
    receipt_text.insert(tk.END, f"{'Price:':<15}${price:.2f}\n")
    receipt_text.insert(tk.END, f"{'Quantity:':<15}{quantity:<15}\n")
    receipt_text.insert(tk.END, f"{'Total:':<15}${total:.2f}\n")

    receipt_text.config(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("Receipt Printing Program")

# Create labels and entry fields for input
name_label = tk.Label(window, text="Customer Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

item_label = tk.Label(window, text="Item:")
item_label.pack()
item_entry = tk.Entry(window)
item_entry.pack()

price_label = tk.Label(window, text="Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

# Create a button to print the receipt
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.pack()

# Create a text widget to display the receipt
receipt_text = tk.Text(window, height=15, width=40)
receipt_text.pack()

# Set text widget to read-only
receipt_text.config(state=tk.DISABLED)

# Start the main event loop
window.mainloop()
