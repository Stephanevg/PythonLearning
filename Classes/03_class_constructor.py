#A simple class constructor would be as followed. The 'self' (lower case) is important. Self will give the instance of the class 
#the possibility to reference itself.

class Employee:
    FirstName = ""
    LastName = ""

    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
        

NewEmployee = Employee("Stephane", "van Gulick")

print("Name ->", NewEmployee.FirstName , "LastName -> ", NewEmployee.LastName)
