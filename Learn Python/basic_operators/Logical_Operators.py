#Logical Operators
a = 5
b = 12
print('a =',a,':',bin(a))
print('b =',b,':',bin(b))
print('Basically it checks for zeros')
print('If there is no zeros')
print('For AND, it returns the second variable')

# and Logical AND
print(a,'and',b,'=',a and b)

# or Logical OR
print('For OR, it returns the first variable')
print(a,'or',b,'=',a or b)

# not Logical NOT
print('Logical NOT is the reversal of the logical state of its operanda')
print('not(',a,'and',b,')=',not(a and b))
print('not(',a,'or',b,')=',not(a or b))