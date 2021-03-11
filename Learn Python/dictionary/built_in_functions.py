#Built-in Dictionary Functions & Methods
#Functions
catalogue = {'Name':'Python 3', 'Type': 'Programming Book','File':'PDF','Size':'2,991,500 bytes',
             'Pages':'512','Price':0.0,'Site':'http://www.tutorialspoint.com'}
keyboard = {'nums':'0123456789','alphas':'abcdefghijklmnopqrstuvwxyz',
              'spec_char':'!@#$%^&*()'}
print("catalogue:",catalogue)
print("keyboard:",keyboard)
print("%s"%'*functions*'.title())
#cmp(dict1, dict2)
#No longer available in Python 3.

#len(dict)
'''Gives the total length of the dictionary. 
This would be equal to the number of items in the dictionary. '''
print("len(catalogue):",len(catalogue))
print("len(keyboard):",len(keyboard))

#str(dict)
'''Produces a printable string representation of a dictionary.'''
print("str(catalogue):",str(catalogue))
print("str(keyboard):",str(keyboard))

#type(variable)
'''Returns the type of the passed variable. If passed variable is dictionary,
 then it would return a dictionary type.'''
print("type(catalogue):",type(catalogue))
print("type(keyboard):",type(keyboard))
print("type('hi'):",type('hi'))
print("type([1,2,3])):",type([1,2,3]))
print("type(123):",type(123))
print("type({1,0,2,3}):",type({1,0,2,3}))
print("type(.5):",type(.5))
print("type(1+3j):",type(1+3j))
print("type((123,456)):",type((123,456)))
