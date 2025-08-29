
medical_cause=input("Did you have a medical cause yes or no: ")

atten = int(input("enter the attendance of the student: "))

#checking the user input predicting output accordingly

if medical_cause == 'yes':
    print("You are allowed")
else:
    if atten>=75: #checking the condition 2 
        print("Allowed")
    else:
        print("Not allowed")