# create class
class parrot:

    #class attribute
    species = "bird"

    #instance attribute
    def__init__(self, name, age): 
    self.name = name
    self.age = age 

    #instantiate the parrot class
    blu = parrot("Blu",10)
    Woo = parrot("Woo",10)

#access the calss attributes
print("Blu is a {}".format(blu.species))
print("woo is also a {}".format(Woo.species))

#access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(Woo.name, Woo.age))
