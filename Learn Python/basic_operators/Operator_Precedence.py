#Operator Precedence
a = 10
b = 12
c = 5
d = 4

print('a:%d b:%d c:%d d:%d'%(a,b,c,d))
print('(%d+%d)*%d/%d = %.2f'%(a,b,c,d,(a+b)*c/d))
print('((%d+%d)*%d)/%d  = %.2f'%(a,b,c,d,((a+b)*c)/d))
print('(%d+%d)*(%d/%d) = %.2f'%(a,b,c,d,(a+b)*(c/d)))
print('%d+(%d*%d)/%d = %.2f'%(a,b,c,d,a+(b+c)/d))