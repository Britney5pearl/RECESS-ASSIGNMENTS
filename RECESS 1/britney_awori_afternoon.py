#Individual Assignment
#Exercise1 (Lists)
#1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names[1])  # Output: Bob

#2. Write a python program to change the value of the first item to a new value
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names[0] = "Frank"
print(names)  # Output: ['Frank', 'Bob', 'Charlie', 'David', 'Eve']

#3. Write a python program to add a sixth item to the list
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.append("Fiona")
print(names)  # Output: ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fiona']

#4. Write a python program to add “Bathel” as the 3rd item in your list
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.insert(2, "Bathel")
print(names)  # Output: ['Alice', 'Bob', 'Bathel', 'Charlie', 'David', 'Eve']

#5. Write a python program to remove the 4th item from the list
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
del names[3]
print(names)  # Output: ['Alice', 'Bob', 'Charlie', 'Eve']

#6. Use negative indexing to print the last item in your list
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names[-1])  # Output: Eve

#7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[2:5])  # Output: [3, 4, 5]

#8. Write a list of countries and make a copy of it.
countries = ["USA", "Canada", "Germany", "Japan", "France"]
countries_copy = countries.copy()
print(countries_copy)

#9. Write a python program to loop through the list of countries
countries = ["USA", "Canada", "Germany", "Japan", "France"]
for country in countries:
    print(country)

#10. Write a list of animal names and sort them in both descending and ascending order.
animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Monkey"]
ascending_order = sorted(animals)
descending_order = sorted(animals, reverse=True)

print(ascending_order)   # Output: ['Elephant', 'Giraffe', 'Lion', 'Monkey', 'Tiger']
print(descending_order)  # Output: ['Tiger', 'Monkey', 'Lion', 'Giraffe', 'Elephant']

#11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them.
animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Monkey"]
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]

print(animals_with_a)  # Output: ['Elephant', 'Giraffe']


#12. Write two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["John", "Alice", "Robert"]
last_names = ["Doe", "Smith", "Johnson"]

full_names = [first + " " + last for first, last in zip(first_names, last_names)]
print(full_names)  # Output: ['John Doe', 'Alice Smith', 'Robert Johnson']

#Exercise2 (Tuples)
#1. Consider the tuple below;x = ("samsung”, “iphone”, “tecno”, “redmi”)
#Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[1]
print(favorite_brand)
# Output: iphone
#2. Use negative indexing to print the 2nd last item in your tuple. 
x = ("samsung", "iphone", "tecno", "redmi")
second_last_item = x[-2]
print(second_last_item)

#3. Using the phones list above, write a python program to update “iphone” to “itel”
x = ("samsung", "iphone", "tecno", "redmi")
x = list(x)
x[x.index("iphone")] = "itel"
x = tuple(x)
print(x)

#4. Write a python program to add “Huawei” to your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
x = x + ("Huawei",)
print(x)

#5. Write a python program to loop through the tuple above.
x = ("samsung", "iphone", "tecno", "redmi")
for item in x:
    print(item)

#6. Write a python program to remove/delete the first item in your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
x = x[1:]
print(x)

#7. Using the tuple() constructor, create a tuple of the cities in Uganda.
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])
print(uganda_cities)

#8. Write a python program to unpack your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
brand1, brand2, brand3, brand4 = x
print(brand1)
print(brand2)
print(brand3)
print(brand4)

#9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
x = ("samsung", "iphone", "tecno", "redmi")
cities = x[1:4]
print(cities)

#10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("John", "Alice", "Robert")
last_names = ("Doe", "Smith", "Johnson")
full_names = first_names + last_names
print(full_names)

#11. Create a tuple of colors and multiply it by 3.
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)

#12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_of_8 = thistuple.count(8)
print(count_of_8)

#Exercise3 (Sets)
#1. Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["coffee", "tea", "juice"])
print(beverages)

#2. Use the correct method to add 2 more items to the beverages set.
beverages.add("water")
beverages.add("soda")
print(beverages)

#3. Given the set below;
# mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
#Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")

#4. Write a python program to remove “kettle” from the set above.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
mySet.remove("kettle")
print(mySet)

#5. Write a python program to loop through the set above.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)

#6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)
print(mySet)

#7. Write two sets, one containing your ages and the other your first names. Join the two sets.
ages = {25, 30, 35}
first_names = {"John", "Alice", "Robert"}
joined_set = ages.union(first_names)
print(joined_set)

#Exercise4 (Strings)
#1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
num = 10
text = "Hello"
concatenated = str(num) + text
print(concatenated)

#2. Consider the example below;
# txt = “ Hello, Uganda! ”
#Output the string without spaces at the beginning, in the middle and at the end.
txt = " Hello, Uganda! "
without_spaces = txt.strip()
print(without_spaces)

#3. Write a python program to convert the value of ‘txt’ to uppercase.
txt = " Hello, Uganda! "
uppercase_txt = txt.upper()
print(uppercase_txt)

#4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
txt = " Hello, Uganda! "
replaced_txt = txt.replace('U', 'V')
print(replaced_txt)

#5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.
y = "I am proudly Ugandan"
y ="I am proudly Ugandan"
range_of_chars = y[1:4]
print(range_of_chars)

#6. The piece of code below will give an error when output;
#x = “All “Data Scientists” are cool!” 
#Write a python program to correct it.
x = 'All "Data Scientists" are cool!'
print(x)

#Exercise5 (Dictionaries)
#1. With reference to the dictionary below, write a python program to print the value of the shoe size. 
#Add this dictionary to your .py file
#Shoes = {“brand” : “Nick”,“color” : “black”,“size” : 40}
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

print(Shoes["size"])


#2. Write a python program to change the value “Nick” to “Adidas”
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

Shoes["brand"] = "Adidas"
print(Shoes)

#3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

Shoes["type"] = "sneakers"
print(Shoes)

#4. Write a python program to return a list of all the keys in the dictionary above.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

keys_list = list(Shoes.keys())
print(keys_list)

#5. Write a python program to return a list of all the values in the dictionary above.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

values_list = list(Shoes.values())
print(values_list)

#6. Check if the key “size” exists in the dictionary above.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

if "size" in Shoes:
    print("The key 'size' exists in the dictionary")
else:
    print("The key 'size' does not exist in the dictionary")

#7. Write a python program to loop through the dictionary above.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

for key, value in Shoes.items():
    print(key, ":", value)

#8. Write a python program to remove “color” from the dictionary.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

del Shoes["color"]
print(Shoes)

#9. Write a python program to empty the dictionary above.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

Shoes.clear()
print(Shoes)

#10. Write a dictionary of your choice and make a copy of it.
# Original dictionary
original_dict = {
    "name": "John",
    "age": 30,
    "country": "USA"
}

# Making a copy of the original dictionary
copy_dict = dict(original_dict)

# Printing both dictionaries
print("Original Dictionary:", original_dict)
print("Copy Dictionary:", copy_dict)

#11. Write a python program to show nested dictionaries.
# Nested dictionary
student_records = {
    "John": {
        "age": 20,
        "grade": "A",
        "subjects": ["Math", "Science", "English"]
    },
    "Alice": {
        "age": 18,
        "grade": "B",
        "subjects": ["History", "Geography", "French"]
    },
    "David": {
        "age": 19,
        "grade": "A+",
        "subjects": ["Physics", "Chemistry", "Biology"]
    }
}
print(student_records)

