#lists is actually an array
#lists are zero based

myList = ["stephane","van Gulick"]
myLanguages = ["powershell","c++"]

'''
It is possible to do arythmetics on lists
'''

print("The start List -> \n")
print(myLanguages)
print("\n")

#removing elements
del myLanguages[1] #removing c++

#Adding elemnts to an existing lists
myLanguages.append("ASP.NET")

#Additions
fullList = myList + myLanguages

print("The Full List -> \n")
print(fullList)
print("\n")

#multiplications (or repetition)

exageratedlist = fullList * 5

print("The exagerateds List -> \n")
print(exageratedlist)

#Usefull helper methods

print("Is contained in Array")
item = 'powershell' 
item in myLanguages

#pop function allows to remove and return the last elemnt of list
print(myLanguages)
topLanguage = myLanguages.pop() #returns ASP.NET
print(topLanguage)

#reversing the list

numbers = [1,3,5,2,4]
print(numbers)

revertNumbers = numbers.reverse()

print(numbers)

#Sorting lists
sortedList = numbers.sort()
print(sortedList)

