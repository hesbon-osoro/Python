#Accessing Values in Dictionary

catalogue = {'Name':'Python 3', 'Type': 'Programming Book','File':'PDF','Size':'2,991,500 bytes',
             'Pages':'512','Price':'0.0','Site':'http://www.tutorialspoint.com'}
keyboard = {'nums':'0123456789','alphas':'abcdefghijklmnopqrstuvwxyz',
              'spec_char':'!@#$%^&*()'}
print("catalogue: %s"%catalogue)
print("%s"%'\n*accessing dictionary values*'.title())
print("catalogue.keys():",catalogue.keys())
print("catalogue.values():",catalogue.values())
print("catalogue['Name']:",catalogue['Name'])
print("catalogue['Type']:",catalogue['Type'])
print("catalogue['File']:",catalogue['File'])
print("catalogue['Size']:",catalogue['Size'])
print("catalogue['Pages']:",catalogue['Pages'])
print("catalogue['Price']:",catalogue['Price'])
print("catalogue['Site']:",catalogue['Site'])

#Updating Dictionary
print("%s"%'\n*updating dictionary values*'.title())
print("catalogue['Site']:",catalogue['Site'])
catalogue['Site'] = 'http://www.tutorialspoint.com/python/'
print("catalogue['Site']:",catalogue['Site'])

#Delete Dictionary Elements
print("%s"%'\n*deleting dictionary values*'.title())
print("keyboard:",keyboard)
del keyboard['spec_char']
print("del keyboard['spec_char']")
print("keyboard:",keyboard)
keyboard.clear() #empties a dictionary
print("keyboard.clear()")
print("keyboard",keyboard)
#del keyboard
#an exception is raised
#print("keyboard:",keyboard)



