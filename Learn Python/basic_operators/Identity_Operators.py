#Identiry Operators
a = 5
b = 5
choice_0 = ''
choice_1 = ' not '
choice_2 = ' do not '
print('a =',a,':',id(a))
print('b =',b,':',id(b))
print(a,'is',end='')
if(a is b):
    print(choice_0,end=' ')
else:
    print(choice_1,end='')
print(b)
#conclusion
print(a,end='')
if(a is b):
    print(choice_0,end='')
else:
    print(choice_2,end='')
print(' have same identity as',b)
a = 8
print('a =',a,':',id(a))
print('b =',b,':',id(b))
print(a,'is',end='')
if(a is b):
    print(choice_0,end='')
else:
    print(choice_1,end='')
print(b)
#conclusion
print(a,end='')
if(a is b):
    print(choice_0,end='')
else:
    print(choice_2,end='')
print(' have same identity as',b)