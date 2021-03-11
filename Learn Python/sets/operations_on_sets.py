#Operations on Sets
alpha = {'a','b','c','d','e'}
char = {'c','d','e','f','g','h','i'}
alp = {'a','b','c','d','e','f','g','h','i','j','k','l',
       'm','n','o','p','r','s','t','u','v','w','x','y','z'}
print("%s"%'***sets***'.upper())
print("alpha:",alpha)
print("char:",char)
print("alp:",alp)
print("%s"%'*operations on sets*'.title())
#Intersection
print("alpha & char:",alpha&char)
#Union
print("alpha | char:",alpha|char)
#Difference
print("alpha-char:",alpha-char)
#Symmetric Difference
print("alpha ^ char:",alpha^char)
#Superset check
print("alpha>=char:",alpha>=char)
print("alp>=alpha:",alp>=char)
#Subset check
print("alpha<=char:",alpha<=char)
print("alpha<=alp:",alpha<=alp)
#Existence check
print("'a' in alp:",'a' in alp)
print("'z' in alpha:",'z' in alpha)
print("1 in {1,2,3,4}:",1 in {1,2,3,4})
print("5 not in {1,2,3,4}:",5 not in {1,2,3,4})
#Add
print("alpha:",alpha)
alpha.add('f')
alpha.add('g')
print("alpha.add('f')\nalpha.add('g')")
print("alpha:",alpha)
alpha.discard('a') #alpha.discard('z') return no error if element not found
print("alpha.discard('a')")
print("alpha:",alpha)
alpha.remove('b') #alpha.remove('z') KeyError!
print("alpha.remove('b')")
print("alpha:",alpha)
alpha.update('h','i','j','k')
print("alpha.update('h','i','j','k')")
print("alpha:",alpha)
print()
#print("\n%20s\t%17s\t%s"%('method','in-place operation','in-place method'))
method = ('*method'.title(),'union','intersection','difference','symmetric_difference')
in_pl = ('in-place operation'.title(),'s|=t','s&=t','s-=t','s^=t')
in_pl_meth = ('in-place method*'.title(),'update','intersection_update','difference_update','symmetric_difference_update')

for i in range(5):
    print("%20s\t%17s\t%s\n"%(method[i].ljust(20,' '),in_pl[i].ljust(17,' '),in_pl_meth[i]))

print()
meth = ('Method','a.intesection(b)','a.union(b)','a.difference(b)','a.symmetric_difference(b)','a.issubset(b)','a.issuperset(b)')
oper = ('Operator','a&b','a|b','a-b','a^b','a<=b','a>=b')
for i in range(7):
    print("%s\t%s\n"%(meth[i].ljust(24,' '),oper[i]))

