# Python Error Handling and Debugging

# Exception Handling in python.
# Exception handling in Python allows you to gracefully handle errors and exceptions that might occur during the execution of your code. 
# This prevents your program from crashing and gives you the opportunity to handle errors in a controlled manner. 
# Python provides the try, except, else, and finally blocks to implement exception handling.

# Here are some detailed code examples demonstrating different aspects of exception handling:
# Example1: Handling Specific Exceptions:
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Unsupported types for division.")
    except Exception as e:
        print("Error:", str(e))
        # You can use the 'as' keyword to capture the exception object and handle it further.

# Example usage:
print(divide_numbers(10, 2))   # Output: 5.0
print(divide_numbers(10, 0))   # Output: Error: Cannot divide by zero.
print(divide_numbers(10, "2")) # Output: Error: unsupported operand type(s) for /: 'int' and 'str'

# Example2: Handling Multiple Exceptions:
def divide_numbers(c, d):
    try:
        result = c / d
        return result
    except Exception as e:
        print("Error:", str(e))

# Example usage:
print(divide_numbers(20, 5))   # Output: 4.0
print(divide_numbers(40, 0))   # Output: Error: division by zero
print(divide_numbers(30, "5")) # Output: Error: unsupported operand type(s) for /: 'int' and 'str'

# Example3: Using the else block:
# The else block is executed only if no exception occurs within the try block.
def divide_numbers(h , m):
    try:
        result = h / m
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print("Error:", str(e))
    else:
        print("Division result:", result)

# Example usage:
divide_numbers(12, 2)   # Output: Division result: 6.0
divide_numbers(15, 0)   # Output: Error: Cannot divide by zero.
divide_numbers(50, "8") # Output: Error: unsupported operand type(s) for /: 'int' and 'str'

# Example4: Using the finally block:
# The finally block is executed no matter what, whether an exception occurs or not.
def divide_numbers(j, k):
    try:
        result = j / k
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print("Error:", str(e))
    finally:
        print("Finally block executed.")

# Example usage:
divide_numbers(45, 5)   # Output: Finally block executed. Division result: 9.0
divide_numbers(90, 0)   # Output: Error: Cannot divide by zero. Finally block executed.
divide_numbers(15, "2") # Output: Error: unsupported operand type(s) for /: 'int' and 'str'. Finally block executed.

# File Handling in python
# File handling in Python allows you to read from and write to files on your computer.
#Here are some code examples to demonstrate different aspects of file handling in Python:

# Example1: Opening and Reading a File:
# Open a file in read mode
file = open("output.txt", "r")

# Read the contents of the file
content = file.read()

# Print the contents
print(content)

# Close the file
file.close()

# Example2: Writing to a File
# Open a file in write mode
file = open("output.txt", "w")

# Write content to the file
file.write("Hello, World!\n")
file.write("This is a sample file.")

# Close the file
file.close()

# Example3: Appending to a File
# Open a file in append mode
file = open("output.txt", "a")

# Append content to the file
file.write("\nThis is additional text.")

# Close the file
file.close()

# Example4: Using 'with' Statement
# Open a file using the with statement
with open("example.txt", "r") as file:
    # Read the contents of the file
    content = file.read()

# Print the contents
print(content)

# In this example, we use the with statement to automatically handle the opening and closing of the file.
# with statement ensures that the file is properly closed even if an exception occurs.
# Inside the with block, we read the contents of the file and store them in the content variable.
# Finally, we print the contents.




