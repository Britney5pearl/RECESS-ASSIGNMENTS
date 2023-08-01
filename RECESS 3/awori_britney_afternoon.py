#Floats, strings,int, decimal, char, booleans
print('*********TYPE OF********')
w = 40 #int type
print(type(w))
z = "Hello world" #string type
print(type(z))
y = 1j #complex type
print(type(y))
print("****************")

#LISTS
#They are used to store multiple items in a single variable.
#Lists are ordered, changable, and allows duplicate values.
print("******** LISTS********")
Afternoon = ["Pearl","Katwebaze","Aaron","Pearl","Jayden","Gabriel"]
print(Afternoon)
#List length
print(len(Afternoon))
#List type
print(type(Afternoon))

#print List items using index
print("Pearl","Katwebaze","Aaron","Pearl","Jayden","Gabriel")
print(Afternoon[0])
print(Afternoon[ 2])
print(Afternoon[3])
print(Afternoon[-3])

#Accessing a range of items, gets from the startIndex to minus one of the last index
print("**************")
print(Afternoon[3:8])
print(Afternoon[:2])
print(Afternoon[1:])

#print List items using a loop
print("**************")
for g in Afternoon:
 print(g)

#appending
Afternoon.append("Aidan")
print(Afternoon)

#remove a particular item
Afternoon.remove("Aaron")
print(Afternoon)

#Add list items using the insert method
Afternoon.insert(4,"Hellen")
print(Afternoon)

#Remove a particular item using index
Afternoon.pop(1)
print(Afternoon)

#TUPLES
#They are used to store items in a single variable.
#They are ordered and unchangeable.
print("****** TUPLES ******")
days = ("Monday", "Tuesday","Wednesday")
print(days)

#Allow for duplicate values
days = ("Monday", "Monday", "Tuesday", "Wednesday", "Wednesday")
print(days)

#Exercise use the len() with this tuple example
print("****** Tuple length ******")
print(len(days))

#Tuple showing different data types
Tuple1 = ("Jumanji", "Missing", "Extraction")
Tuple2 = (600, 400, 550)
print(Tuple1)
print(Tuple2)
print(type(Tuple1))

#Exercise how to access TUPLES
print(Tuple2[2])
print(Tuple2[-1])

#Add items to a tuple
days = ("Monday", "Tuesday", "Wednesday")
print(days)
y =list(days)
y.append("Friday")
days = tuple(y)
print(days)

#second method to add items
extra_day = ("Thursday",)
days+=extra_day
print(days)