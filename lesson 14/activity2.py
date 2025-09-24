def add (P,Q):
    return P+Q

def subtract (P,Q):
    return P-Q

def multiply (P,Q):
    return P*Q

def divide (P,Q):
    return P/Q
#Now we will take inputs from user
print("Please select operation")
print("+. Add")
print("-. Subtract")
print("*. Multiply")
print("/. divide")

choice = input("Please enter choice (+,-,*,/)")

num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another number: "))

if choice == '+':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == '-':
    print(num_1, "+", num_2, "=", subtract(num_1, num_2))
elif choice == '*':
    print(num_1, "+", num_2, "=", multiply(num_1, num_2))
elif choice == '/':
    print(num_1, "+", num_2, "=", divide(num_1, num_2))
else:
    print("This is an invalid input")
