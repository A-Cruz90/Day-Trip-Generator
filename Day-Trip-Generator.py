import random
from subprocess import CompletedProcess
from turtle import right





destination_list =["Las Vegas, NV", "Cleveland, OH", "Charlotte, NC", "Tampa, FL"]

transportation_list =["Private Bus", "Car Rental", "Cycling", "Uber"]

entertainment_list =["Busch Gardens", "Kings Landing", "Sight Seeing ", "Theater"]

restaurant_list =["Little NY", "Little Italy", "Taco Bell", "Chilli's"]





# print(len(destination_list))
# print(len(transportation_list))
# print(random.choice(transportation_list))
# print(len(entertainment_list))
# print(random.choice(entertainment_list))
# print(len(restaurant_list))
# print(random.choice(restaurant_list))

# print(destination_list)
# print(transportation_list)
# print(entertainment_list)
# print(restaurant_list)


print( "Hello Everyone, and welcome to the random day generator! We have selected four wonderful locations at random that we know you'll simply adore. Lets begin shall we? ") 
print("Your randomly selected destination is")

while (True):
    destination = (random.choice(destination_list))
    print(destination)
    print("Will you be ok with that?") 
    choice = input("y or n: ")
    if choice == "y":
        print("Awesome your destination has been selected. ")
        break
    elif choice == "n":
        print("We are sorry. How about:")


print("Next we'll select a means for travel while there ")
print("Your means of travel while there will be ")
while(True):
    trasportation = (random.choice(transportation_list)) 
    print(trasportation)
    print("Will you be ok with that?") 
    choice = input("y or n: ")
    if choice == "y":
        print("Awesome your means of travel have been selected. ")
        break
    elif choice == "n":
        print("We are sorry. How about:")



print("Next we'll decide entertainment while there ")
print("Your enetertainment will be ")
while(True):
    entertainment = (random.choice(entertainment_list)) 
    print(entertainment)
    print("Will you be ok with that?") 
    choice = input("y or n: ")
    if choice == "y":
        print("Awesome your entertainment has been selected. ")
        break
    elif choice == "n":
        print("We are sorry. How about:")




print("Next we'll select your dining experience while there ")
print("Your dining experience will be ")
while(True):
    dine = (random.choice(restaurant_list)) 
    print(dine)
    print("Will you be ok with that?") 
    choice = input("y or n: ")
    if choice == "y":
        print("Awesome your dining experience has been selected. ")
        break
    elif choice == "n":
        print("We are sorry. How about:")

        


print("Your day has been planned out to the fullest!")
print("We will start by arriving at")
print(destination)
print("Once there you'll enjoy traveling the location by ")
print(trasportation)
print("You'll spend the day doing ")
print(entertainment)
print("Lastly we'll end the day with dinner at your local ")
print(dine)

print("We hope you enjoy your day ")
print("Will you be ok with your perfectly planned out day? ")
choice = (input("y or n? "))
if choice == "y":
    print("Have fun!!!")
elif choice == "n":
    print("We are sorry lets try and plan this day out one more time ok. ")
