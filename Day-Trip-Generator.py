import random



destination_list =["Las Vegas, NV", "Cleveland, OH", "Charlotte, NC", "Tampa, FL"]

transportation_list =["Private Bus", "Car Rental", "Cycling", "Uber"]

entertainment_list =["Casino", "Kayaking", "Sight Seeing ", "Theater"]

restaurant_list =["Little NY", "Little Italy", "Taco Bell", "Chilli's"]

# print(len(destination_list))
# print(len(transportation_list))
# print(len(entertainment_list))
# print(len(restaurant_list))
# print(destination_list)
# print(transportation_list)
# print(entertainment_list)
# print(restaurant_list)

def destination_picker():
    print( "Hello Everyone, and welcome to the random day generator! We have selected four wonderful locations at random that we know you'll simply adore. Lets begin shall we? ") 
    print("Your randomly selected destination is")

    while (True):
        destination = (random.choice(destination_list))
        print(destination)
        print("Will you be ok with that?") 
        choice = input("y or n: ")
        if choice == "y":
            print("Awesome your destination has been selected. ")
            return destination
        elif choice == "n":
            print("We are sorry. How about:")

print("")

def transporation_picker():
    print("Next we'll select a means for travel while there ")
    print("Your means of travel while there will be ")
    while(True):
        transportation = (random.choice(transportation_list)) 
        print(transportation)
        print("Will you be ok with that?") 
        choice = input("y or n: ")
        if choice == "y":
            print("Awesome your means of travel have been selected. ")
            return transportation
        elif choice == "n":
            print("We are sorry. How about:")

print("")

def entertainment_picker():
    print("Next we'll decide entertainment while there ")
    print("Your entertainment will be ")
    while(True):
        entertainment = (random.choice(entertainment_list)) 
        print(entertainment)
        print("Will you be ok with that?") 
        choice = input("y or n: ")
        if choice == "y":
            print("Awesome your entertainment has been selected. ")
            return entertainment
        elif choice == "n":
            print("We are sorry. How about:")

print("")

def dining_picker():
    print("Next we'll select your dining experience while there ")
    print("Your dining experience will be ")
    while(True):
        dine = (random.choice(restaurant_list)) 
        print(dine)
        print("Will you be ok with that?") 
        choice = input("y or n: ")
        if choice == "y":
            print("Awesome your dining experience has been selected. ")
            return dine
        elif choice == "n":
            print("We are sorry. How about:")

print("")

def summary(destination,transportation,entertainment, dine):
    print("Your day has been planned out to the fullest!")
    print("")
    print(f'We will start by arriving at {destination}')
    print("")
    print(f'Once there you will enjoy traveling the location by {transportation}')
    print("")
    print(f'You will spend the day doing {entertainment}')
    print("")
    print(f'Lastly we will end the day with dinner at your local {dine}')
    print("")
    print("Will you be ok with your perfectly planned out day? ")
    choice = (input("y or n? "))
    if choice == "y":
        print("We hope you enjoy your day!!! ")
        print("Have fun!!!")
    elif choice == "n":
        print("We are sorry lets try and plan this day out one more time ok. ")
        run_program()

def run_program():
    confirmed_destination = destination_picker()
    confirmed_transportation = transporation_picker()
    confirmed_entertainment = entertainment_picker()
    confirmed_dining = dining_picker()
    summary(confirmed_destination,confirmed_transportation, confirmed_entertainment, confirmed_dining)

run_program()