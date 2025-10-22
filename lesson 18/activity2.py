import random

options = ["rock", "paper", "scissors"]

user_choice = input("Choose rock, paper scissors: ")

computer_choice = random.choice(options)

print("You chose",user_choice)
print("computer chose",computer_choice)

if user_choice == computer_choice:
    print("It is a tie")
elif user_choice == "rock" and computer_choice =="scissors" :
    print("rock smashes scissors! You win!")
elif user_choice == "paper" and computer_choice =="rock" :
    print("paper smashes rock! You win!")
elif user_choice == "scissors" and computer_choice =="paper" :
    print("scissors cut paper! You win!")
else:
    print("You lose :(")   