#Examples of arithmetic operators
#Addition
x = 60 + 30
print(x)

#subtraction
y = 50 - 25
print(y)

#Multiplication
z = 60 * 45
print(z)

#division
a = 70 / 5
print(a)

#divide
b = 70 // 5
print(b)

# modulus
c = 300 % 3
print(c)

#exponentiation
d = 8 ** 9
print(d)

#Examples of comparison operators
#comparison operators
a = 30
b = 10

# Greater than
if a > b:
    print('a is greater than b')
    print(a > b)

# Less than
if a < b:
    print('a is less than b')
    print(a < b)

# greater than or equal to
if a >= b:
    print('a is greater than or equal to b')
    print(a >= b)

# less than or equal to
if a <= b:
    print('a is less than or equal to b')
    print(a <= b)

#equal to
if a == b:
    print('a is equal to b')
    print(a == b)

#Not equal to
if a != b:
    print('a is not equal to b')
    print(a != b)

# less than or equal to
print(a <= b)

# equal to
print( a == b)

#Examples of logical operators
#Logical operators
r = True
p = False

#Logical AND
print(r and p)
#Logical OR
print(r or p)
#Logical NOT
print(not r)
print(not p)

# Examples of Assignment operator
#compound assignment operator
w = 6

#Add and assign
w += 6
print(w)

#Subtract and assign
x = 20
x -= 9
print(x)

#multiply and assign
v  = 35
v  *= 3
print(v)

# divide and assign
h = 25
h /= 5
print(h)

#modulus and assign
l = 13
l %= 6
print(l)

#exponentation and assign
m = 1
m **= 9
print(m)

#Examples of membership assignment operators
cars =['Jeep', 'Telsa', 'BMW', 'Roll Royce']
if 'Jeep' in cars:
    print('Jeep is in the list')
    print('Telsa' in cars)
    print('Toyota' in cars)

#identity operators
x = 40
y = 40
#is operator
print(x is y)
print(x is not y)
print( x == y)
print( x != y)
print( x < y)
print( x <= y)

#List
# is not operator
z = [1,2,3,4,5,6,7]
w = [1,2,3,4,5,6,7]
print(z is not w)

#Bitwise opeartors
"""
They are used to perform operations on individual bits in of binary numbers.
Bitwise AND ("&"): Performs a bitwise AND operation between the corresponding bits of two integers
Bitwise OR ("|"): Performs a bitwise OR operation between the corresponding bits of two integers
Bitwise XOR("^"): Performs a bitwise XOR operation
Bitwise NOT("-"): Performs a bitwise NOT operation between the corresponding bits of two integers
Bitwise left shift ("<<"): Performs a bitwise left shift operation 
Bitwise right shift(">>"): Performs a bitwise right shift operation 
"""
#Examples of Bitwise operations
a = 10
b = 20

#Bitwise AND operation
result_and = a & b
print(result_and)

#Bitwise OR operation
result_or = a | b
print(result_or)

#Bitwise XOR operation
result_xor = a ^ b
print(result_xor)

#Bitwise NOT operation
result_not = a - b
print(result_not)

#Bitwise left shift
result_leftshift = a << b
print(result_leftshift)

#Bitwise right shift
result_rightshift = a >> b
print(result_rightshift)

#Example
#Create a simple calculator function to calculate(add, subtract, multiply and divide)
def add(a, b):
  return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def main():
    print('Pearl simple calculator')
    number1 = float(input("Enter your first number:"))
    number2 = float(input("Enter your second number:"))
    operator = input("Enter the operator (+, -, *, /):")

    if operator == '+':
        result = add(number1, number2)
    elif operator == '-':
        result = subtract(number1, number2)
    elif operator == '*':
        result = multiply(number1, number2)
    elif operator == '/':
        result = divide(number1, number2)
    else:
        print('Invalid operator')
        return
    print("the result is", result)

if __name__ == '__main__':
    main()
#Assignment: create a simple calculator program with a GUI interface.
#Make your title of the calculator program with window with your name
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Awori Britney simple calculator")

# Create the entry widget
entry = tk.Entry(window, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
button_1 = tk.Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))

# Create the operator buttons
button_add = tk.Button(window, text="+", padx=20, pady=10, command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=20, pady=10, command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=20, pady=10, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=20, pady=10, command=lambda: button_click("/"))

button_equal = tk.Button(window, text="=", padx=20, pady=10, command=button_equal)
button_clear = tk.Button(window, text="Clear", padx=10, pady=10, command=button_clear)

# Add buttons to the window
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=0)

# Start the GUI event loop
window.mainloop()








