try:
    num1 = int(input("Enter a number: ")) #4
    num2 = int(input("Enter a number: ")) #0
    result = num1/num2 #4/0
    print("Result is: ", result)
    print("Result is: ", result1)

except ZeroDivisionError :
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter numerical value")
except NameError as ex:
    print("the exception is " ,ex)

except:
    print("Some error occurred")
finally:
    print("I will execute you no matter what happenes")