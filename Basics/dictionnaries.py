#To declare a dictionnary:
#Dicitonnaries are also know as "maps" or "Dict" in phyton
dictionnary = {'Name':'Stephane','LastName':'van Gulick','Age':'cant remember!'}

#reading values
print("Name ->", dictionnary['Name'])
print("LastName ->", dictionnary['LastName'])
print( "Age ->", dictionnary['Age'])

#settings values using =

dictionnary['Age'] = 'intemporal!'
dictionnary['Name'] = 'Jean Claude'

#Adding a new entry to the dictionnary (also using =)

dictionnary['prefLanguage'] = 'PowerShell'

#reading values
print("Name ->", dictionnary['Name'])
print("LastName ->", dictionnary['LastName'])
print( "Age ->", dictionnary['Age'])
print( "preffered language ->", dictionnary['prefLanguage'])

#deleting an element

del dictionnary['prefLanguage'];

dictionnary.clear(); # removes all entries from the dictionnary.

del dictionnary; #Deletes the entiere dictionnary.


#Read information from dictionnaries

print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})

