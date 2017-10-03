#In order to be able to find out what properties / attributes you have access to from a class / function, call the dir() function.

class Employee:
    FirstName = ""
    LastName = ""

    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
        

NewEmployee = Employee("Stephane", "van Gulick")

print(dir(NewEmployee))

import sys
print(sys.version)

print("NewEmployee with repr()")
print(repr(NewEmployee))

print("NewEmployee with repr()")
print(str(NewEmployee))