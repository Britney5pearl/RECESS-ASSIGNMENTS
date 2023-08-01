#Value pairs
#Dictionaries are ordered, changeable but do nor allow duplicates
#Dicts can have items of any data type
mydict = {
    "phone":"iphone",
    "iphonemodel":"iphone15",
    "year":2023
}
print(mydict)
#length of a dictionary
print(len(mydict))
#datatype
print(type(mydict))
#Access dictionary items
z = mydict["year"]
print(z)
y = mydict.get("iphonemodel")
print(y)
#Keys
w = mydict.keys()
print(w)
#numbers
#integers, floats, complex
w = 10 #int
r = 3.9 #float
s = 2j #complex
print(type(w))
print(type(r))
print(type(s))
#integer
a = 2
b = 2345678
c = -2344
print(type(a))
print(type(b))
print(type(c))
#Floats
x = 2.34
y = 2.7889900
z = -34.7899
print(type(x))
print(type(y))
print(type(z))
#complex numbers
h = 5 + 12j
t = 7j
m = -6j
print(type(h))
print(type(t))
print(type(m))
#type conversions
w = 10 #int
r = 3.9 #float
s = 2j #complex
#convert from int to complex
d = complex(w)
print(d)
print(type(d))
#convert from int to float
#convert from float to complex
#Strings
#print("Afternoon")
#print('Afternoon')
#Assign string to a variable
w = "Afternoon"
#print(w)
#Multiline strings
q = """I am offering BSSE 
Currently doing recess"""
print(q)
#strings as arrays
a = "Afternoon"
print(a[0])
#How to modify strings
b = "Afternoon"
print(b.lower())
print(b.upper())
#Remove white space
c = "Afternoon"
print(c.strip())
#String concatenation
d = "Afternoon"
e = "class"
w = c + d
print(w)
#Booleans
#These evaluate to a true or false
print(20 < 10)
print(30 == 40)
print(30 > 10)
print(bool(15))
r = "Livingstone"
z = 30
print(bool(r))
print(bool(z))
#Exercise One:use the values() method to return a list of all values in the dictionary
mydict2 = {
    "name":"Pearl",
    "age":21,
    "year":2023
}
x = list(mydict2.values())
print(x)
#Exercise Two:to check if a key does exist in your dictionary
mydict2 = {
     "name":"Pearl",
    "age":21,
    "year":2023
}
key_to_check ="name"
if key_to_check in mydict2:
    print("Key exists!")
else:
    print("Key does not exist!")
#Exercise Three:Give an example on how to change dictionary items, how to update
student = {
    'name': 'John',
    'age': 20,
    'grade': 'A'
}

# Changing an existing item
student['age'] = 21
print(student)  # Output: {'name': 'John', 'age': 21, 'grade': 'A'}

# Updating multiple items using another dictionary
update_info = {
    'age': 22,
    'grade': 'B'
}

student.update(update_info)
print(student)  # Output: {'name': 'John', 'age': 22, 'grade': 'B', 'major': 'Computer Science'}

#Exercise Four:Give an example on how to add dictionary items, how to remove dictionary items
student = {
    'name': 'Anderson',
    'age': 20,
    'grade': 'B'
}

# Adding a new item
student['major'] = 'Law'
print(student)  # Output: {'name': 'Anderson', 'age': 20, 'grade': 'B', 'major': 'Law'}

# Removing an item
del student['grade']
print(student)  # Output: {'name': 'Anderson', 'age': 20, 'major': 'Law'}

#Exercise Five:Give an example on how you can loop through a dictionary and also how to nest dictionaries
# Looping through a dictionary
student = {
    'name': 'Drake',
    'age': 25,
    'grade': 'A'
}

for key, value in student.items():
    print(key, ":", value)

# Nesting dictionaries
students = {
    'student1': {
        'name': 'Drake',
        'age': 25,
        'grade': 'A'
    },
    'student2': {
        'name': 'Jane',
        'age': 21,
        'grade': 'B'
    }
}

for student_key, student_info in students.items():
    print(student_key)
    for key, value in student_info.items():
        print(key, ":", value)
    print()
#Exercise six:Give an example on how to determine the length of a string using the len() function.
text = "Hello, World!"
length = len(text)
print("The length of the string is:", length)

#Exercise seven:ive an example on how to iterate through each character in a string using a for loop.
text = "Hello, World!"

for character in text:
    print(character)

#Exercise eight:Give an example on how to slice a string to extract specific portions of it.
text = "Hello, World!"

# Extracting a substring
substring = text[7:12]
print(substring)  # Output: World

# Extracting from the beginning
start = text[:5]
print(start)  # Output: Hello

# Extracting until the end
end = text[7:]
print(end)  # Output: World!

# Skipping characters
skipped = text[::2]
print(skipped)  # Output: Hlo ol!

#Exercise nine:Give an example on how to perform arithmetic operations with numbers and print the results.
# Addition
num1 = 5
num2 = 3
sum_result = num1 + num2
print("Sum:", sum_result)  # Output: Sum: 8

# Subtraction
num3 = 10
num4 = 4
subtraction_result = num3 - num4
print("Subtraction:", subtraction_result)  # Output: Subtraction: 6

# Multiplication
num5 = 6
num6 = 7
multiplication_result = num5 * num6
print("Multiplication:", multiplication_result)  # Output: Multiplication: 42

# Division
num7 = 15
num8 = 2
division_result = num7 / num8
print("Division:", division_result)  # Output: Division: 7.5

# Floor Division
floor_division_result = num7 // num8
print("Floor Division:", floor_division_result)  # Output: Floor Division: 7

# Modulo
modulo_result = num7 % num8
print("Modulo:", modulo_result)  # Output: Modulo: 1

# Exponentiation
exponentiation_result = num2 ** num1
print("Exponentiation:", exponentiation_result)  # Output: Exponentiation: 243

#Exercise ten:Give an example on how to use boolean values and conditions to control program flow.     
# Boolean values and conditions
is_student = True
is_registered = False

# If statement
if is_student:
    print("You are a student!")

# If-else statement
if is_registered:
    print("You are registered.")
else:
    print("You are not registered.")

# If-elif-else statement
age = 17

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

   