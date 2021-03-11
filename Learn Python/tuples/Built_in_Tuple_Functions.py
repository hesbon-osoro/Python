#Built-in Tuple Functions
web = ('HTML','CSS','Bootstrap','Javascript','jQuery','PHP')
lan = ('Java','Python','Swift')
machine = ['C','C++','Python','R']
alpha  = 'abcdefghi'
print("web:",web)
print("lan:",lan)
print("%s"%'\n*functions*'.title())
#cmp(tuple1, tuple2)
'''No longer available in Python 3.'''
#print("cmp(lan,web):",cmp(web,lan))

#len(tuple)
'''Gives the total length of the tuple.'''
print("len(web):",len(web))
print("len(lan):",len(lan))
#max(tuple)
'''Returns item from the tuple with max value. '''
print("max(web):",max(web))
print("max(lan):",max(lan))
#min(tuple)
'''Returns item from the tuple with min value.'''
print("min(web):",min(web))
print("min(lan):",min(lan))
#tuple(seq)
'''Converts a list into tuple. '''
print("machine:",machine)

print('alpha:',alpha)
print("tuple(alpha):",tuple(alpha))
print("tuple(machine):",tuple(machine))


