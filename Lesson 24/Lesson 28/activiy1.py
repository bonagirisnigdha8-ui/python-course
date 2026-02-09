#Class creation
class myclass:

    #private variable
    __privateVar = 27:

    #private method
    def __privMeth(self):
         print("I am inside my class")

         # Function to printvalue ofprivate variable
def hello(self):
  print("Private Variable value: ",myClass.__privateVar)

#Object creation and method call
foo = myclass()
foo.hello()
foo.__privMeth