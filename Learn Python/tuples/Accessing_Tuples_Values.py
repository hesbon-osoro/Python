#Accessing Values in Tuples
units = ('Grams','Kilograms','Degrees','Metres','Amperes')
nums = (12,13,4.5,5.0)
print("%s"%'\n*accessing tuple values*'.title())
print("units:",units)
print("units[1]: %s"%units[1])
print("units[-2:]",units[-2:])
print("units[-2:1]:",units[-2:1]) #no output
print("units[1:-2]:",units[1:-2])
print("units[:-2]:",units[:-2])

print("%s"%'\n*updating tuples*'.title())
#units[2] = 'Kelvins' #TypeError: 'tuple' object does not support item assignment
print("units:",units)
#concatenation
print("units+nums:",units+nums)
print("%s"%'\n*deleting tuples*'.title())
print("nums before deletion:",nums)
print("After deletion the tuple does not exist any more\nAn exception is raised")
#del nums
#print("nums:",nums)
'''Note: An exception is raised. 
This is because after del tup, tuple does not exist any more.'''