string = input("Please enter your own word: ")
char = input("please enter your character: ")
i = 0
count = 0
while(i < len(string)): #string operation

    if (string[i] == char): #condition 1
        count = count + 1
    i = i + 1

        #Display the result
print("The total Number of times",char,"has occured = ",count)