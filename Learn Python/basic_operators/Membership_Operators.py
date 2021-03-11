#Membership Operators
my_test_list=[0,1,2,3,4,5,6,7,8,9]
test_no = 10
test_no_1 = 20
choice = ' in '
choice_1 = ' not in '
print('Given numbers: ',my_test_list)
print(test_no,'is',end='')
#testing by ternary operator
if(test_no in my_test_list):
    print(choice,end='')
else:
    print(choice_1,end='')
print('the given numbers')

print(test_no_1,'is',end='')
if(test_no_1 in my_test_list):
    print(choice,end='')
else:
    print(choice_1,end='')
print('the given numbers')

print(test_no_1,'/',test_no,':',test_no_1/test_no,'is',end='')
if(test_no_1/test_no in my_test_list):
    print(choice,end='')
else:
    print(choice_1,end='')
print('the given numbers')