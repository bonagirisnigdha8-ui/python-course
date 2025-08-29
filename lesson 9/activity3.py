print("Select your ride: ")
print("1. Bike")
print("2. Car")
# take input of number 1 or 2
# select your ride
choice = int(input("Enter your choice: "))
#User entering option 1
if( choice == 1): #condition 1 outer if statement
    print("what type of bike?")
    print("1. Scooty/n")
    print("2. Scooter/n")

#Condition for selecting the type of bike
choice2=int(input("Enter your choice2: "))
if choice2==1: #inner if statement
     print("you have a selected scooty")
else:
     print("you have a selected scooter")