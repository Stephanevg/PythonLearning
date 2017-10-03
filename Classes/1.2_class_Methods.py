#https://docs.python.org/fr/2/tutorial/classes.html#method-objects

class Employee:
    FirstName = ""
    LastName = ""

    def ShowInfos(self):
        print("The employee name is ->", self.FirstName, "and his last name is ->", self.LastName)

#Creating an isntance
NewEmployee = Employee()

#Assigning values
NewEmployee.FirstName = "Stephane"
NewEmployee.LastName = "van Gulick"

NewEmployee.ShowInfos();