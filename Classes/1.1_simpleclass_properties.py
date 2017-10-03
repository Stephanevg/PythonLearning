#Offical documentation -> https://docs.python.org/fr/2/tutorial/classes.html
class Employee:
    FirstName = ""
    LastName = ""

#Creating an isntance
NewEmployee = Employee()

#Assigning values
NewEmployee.FirstName = "Stephane"
NewEmployee.LastName = "van Gulick"

#Printing out
print("New employee infos:")
print(NewEmployee.FirstName)
print(NewEmployee.LastName)