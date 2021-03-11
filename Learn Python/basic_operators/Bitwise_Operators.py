#Bitwise Operators

a = 80
b = 12
print('a =',a,':',bin(a))
print('b =',b,':',bin(b))

# & binary AND
print(a,'&',b,'=',a&b,':',bin(a&b))
#  | binary OR
print(a,'|',b,'=',a|b,':',bin(a|b))
# ^ binary XOR
print(a,'^',b,'=',a^b,':',bin(a^b))
# ~ COMPLEMENT
print('~',b,'=',~b,':',bin(~b))
# << left shift
print(b,'<< 2 =',b<<2,':',bin(b<<2))
# >> right shifr
print(b,'>> 2 =',b>>2,':',bin(b>>2))