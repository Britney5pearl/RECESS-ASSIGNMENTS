#print('True')#code block is only executed if condition 1 is True
#elif condition2:
#print('True')#code block is only executed if condition2 is True
#else:
#print('False')
#Example 1
age = 20
if age < 18:
  print ("You are under age")
if age >= 18 and age <= 70:
   print ("You are an adult")
else:
 print ("Your a senior citizen")
age = 20
if age < 18:
    print('You are under age')
elif age >= 18 and age <=70:
    print('You are an adult')
else:
        print('You are a senior citizen')

#Loops
#Loops (for, while)
cars= ["Jeep", "Nissan", "BMW", "Vitz"]
for car in cars:
    print(car)
    #Example 2
    # fruits
    fruits = ["strawberries", "watermelon", "mango", "apple"]
    for fruit in fruits:
        print(fruit)
        #while loop
        #while condition is true: It will execute while condition is True:
        x = 0
        while x < 5:
            print(x)
            x += 1
            #Example 3
            days =["Monday", "Tuesday", "Wednesday"]
            # Convert the set of days to a list
            day_list = list(days)
            # Get the length of the day list
            length = len(day_list)
            # Initialize the index variable
            index = 0
            while index < length:
                # Access the current day
                 current_day = day_list[index]
            print(current_day)
            index += 1
#Break and continue statements
#Break statement
for number in range(1,10):
    if number == 5:
        break
        print(number)
#Continue statement
for number in range(1,10):
    if number == 5:
        continue
        print(number)
#Example 4
animals = ["cow", "goat", "pig","sheep"]
for animal in animals:
    if animal == "cow":
        continue
    if animal =="pig":
        break
        print(animal)
        #Exception handling (try, except, finally)
        try:
            x = 10/0
        except ZeroDivisionError:
                print('Error: Division by Zero')
                #cannot divide by zero
        finally:
         print('This is always executed')
                #complete execution
                #Example 5
def divide_numbers(a, b):
        try:
                        result = a / b
                        print("Division result:", result)
        except ZeroDivisionError:
         print("Error: Division by zero is allowed.")
        except TypeError:
         print("Error: Invalid types for division.")
        finally:
         print("Division operation completed.") 
# Test cases
divide_numbers(10,2) # Valid division
divide_numbers(10,0) # Division by zero error
divide_numbers (10,"2") # Type error
#Example 6
#Dict is a dictionary{}
emotion = {
    'happy': "I'm glad to hear that you are happy",
    'sad': "I'm sorry to hear that you are sad",
    'Angry': "take a deep breath and try to stay alive",
    'fearful':"I understand that fear can be chllenging",
    'disgusted': "that's unfortunate to feel disgusted",
 } 
 #Prompt the user to enter their emotions
user_emotion = input("How are you feeling today?")
 #convert the user input to enter their emotions
user_emotion = user_emotion.lower()
if user_emotion in emotion:
    print(emotion[user_emotion]) 
else:
    print("I'm sorry i don't understand your emotion.")
 #exercise 1
 #write a program to ask students about their mental health
 #Prompt students on a scale of 1 to 10 to rate their mental health                                   
def get_mental_health_rating():
    rating = None
    while rating is None:
        try:
            rating = int(input("On a scale of 1 to 10, rate your mental health: "))
            if not (1 <= rating <= 10):
                print("Please enter a rating between 1 and 10.")
                rating = None
        except ValueError:
            print("Invalid input. Please enter a number.")

    return rating


def ask_about_mental_health():
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")

    response = input("How are you feeling today? ")

    print(f"Thank you for sharing, {name}.")

    rating = get_mental_health_rating()
    print(f"Your mental health rating is: {rating}")


ask_about_mental_health()



