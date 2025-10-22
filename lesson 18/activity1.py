import random #importing module
playing = True #initialise
number = str(random.randint(10,20)) #random in-built function

print("I will generate a number from 10 to 20, and you will guess a number")
print("The game ends when you get to 1 hero")
#ilterate loop till the condition is true
while playing:
    guess = input("Give me your best guess")
    if number == guess:
        print("You win the game")
        print("The number was",number)

    else:
        print("Your guess isn't right, try again")
        print("The number was",number)
