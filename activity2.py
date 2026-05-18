# Import necessary libraries
from tkinter import *
from datetime import date

# Create window
root = Tk()
root.title('Getting Sratted with Widgets')
root.geometry('400x300')
# Add widgets
# Add lable
lbl = Label (text="Hello!", fg="white", bg="#DB56D4", height=1, 
             width=300)

# Add Label for getting name as input from user
# Use Entry Widget to create a text box for user to enter details
name_lbl = Label(text="Full Name", bg="#69117B")
name_entry = Entry()

# Functoin to display a Message
def display():
    # Read input given by user
    name = name_entry.get()
# Declaring a global variable
#to make it accessible anywhrer in the program
global message
message = "Welcome to the application! \nToday's date is: " greet = "Hello "+name+"\n"
# Display details in a text box
