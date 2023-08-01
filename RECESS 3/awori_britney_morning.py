#store multiple items in a single variable
#unchangeable but one can remove and add new items

setone = {"iphone", "Samsung", "Nokia"}
print(setone)

#Duplicates in sets
setone = {"iphone", "Samsung", "Nokia", "Nokia"}
print(setone)

#length of the set
setone = {"iphone", "Samsung", "Nokia"}
set_length = len(setone)
print("Length of the set:", set_length)


#datatype of set
setone = {"iphone", "Samsung", "Nokia"}
set_type = type(setone)
print("Data type of the set:", set_type)

#Accessing items in a set
setone = {"iphone", "Samsung","Nokia"}
for item in setone:
    print("Item:", item)


#Adding items to a set
setone = {"iphone", "Samsung","Nokia"}
setone.add("Tecno")
setone.add("Infinix")
print("Updated set:", setone)

#Adding two sets together
setone = {"iphone", "Samsung","Nokia"}
settwo = {"Owen","Saleem","David"}
combined_set = setone.union(settwo)
print("Combined set:", combined_set)