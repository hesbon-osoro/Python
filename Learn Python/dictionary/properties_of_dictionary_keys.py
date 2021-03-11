#Properties of Dictionary Keys

print("%s"%'\n*Properties of Dictionary Keys*'.title())
print("%s"%'\n**notes**'.upper())
print("""Dictionary values have no restrictions.\n
 They can be any arbitrary Python object, 
 either standard objects or user-defined objects. 
However, same is not true for the keys. 
    """)
print("There are two important points to remember about dictionary keys-")
print("""*(a) More than one entry per key is not allowed.*\n
 This means no duplicate key is allowed. When duplicate keys are encountered during assignment, 
the last assignment wins. For example-
    """)
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print('dict:',dict)
print ("dict['Name']: ", dict['Name'])
print("""*(b) Keys must be immutable.*
 This means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed.
  Following is a simple example- 
    """)
print("View Source Code!")
#dict = {['Name']: 'Zara', 'Age': 7}
#print ("dict['Name']: ", dict['Name'])
#TypeError: list objects are unhashable