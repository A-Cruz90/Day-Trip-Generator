import random




destination_list =["San Juan, PR", "Tokyo, Japan", "Charlotte, NC", "Tampa, FL"]

transportation_list =["Plane", "Car", "Train", "Boat"]

entertainment_list =["Busch Gardens", "Kings Landing", "Touring Fort", "Theater"]

restaurant_list =["Olive Garden", "Capognas Dugout", "Taco Bell", "Chilli's"]





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
    d = (random.choice(destination_list))
    print(d)
    print("Will you be ok with that?") 
    input = input("y or n: ")
    if input == "y":
        print("Awesome your destination has been selected. ")
        break
    elif input == "n":
        print("We are sorry. How about:")










        





