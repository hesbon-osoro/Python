#Mathematical Functions
#abs(x)
'''The absolute value of x: the (positive) distance between x and zero. '''
print ("abs(-45) : ", abs(-45)) 
print ("abs(100.12) : ", abs(100.12)) 

#ceil(x)
'''The ceiling of x: the smallest integer not less than x. '''
import math   # This will import math module 
print ("math.ceil(-45.17) : ", math.ceil(-45.17)) 
print ("math.ceil(100.12) : ", math.ceil(100.12)) 
print ("math.ceil(100.72) : ", math.ceil(100.72)) 
print ("math.ceil(math.pi) : ", math.ceil(math.pi)) 
#cmp(x,y)
'''
-1 if x < y, 0 if x == y, or 1 if x > y. Deprecated in Python 3;
 Instead use return (x>y)-(x<y). '''
 
#exp(x)
'''The exponential of x: e^x'''
#import math   # This will import math module 
print ("math.exp(-45.17) : ", math.exp(-45.17)) 
print ("math.exp(100.12) : ", math.exp(100.12)) 
print ("math.exp(100.72) : ", math.exp(100.72)) 
print ("math.exp(math.pi) : ", math.exp(math.pi))
#fabs(x)
'''The absolute value of x. '''
 #import math   # This will import math module 
print ("math.fabs(-45.17) : ", math.fabs(-45.17)) 
print ("math.fabs(100.12) : ", math.fabs(100.12)) 
print ("math.fabs(100.72) : ", math.fabs(100.72)) 
print ("math.fabs(math.pi) : ", math.fabs(math.pi)) 
#floor(x)
'''The floor of x: the largest integer not greater than x. '''
print ("math.floor(-45.17) : ", math.floor(-45.17)) 
print ("math.floor(100.12) : ", math.floor(100.12)) 
print ("math.floor(100.72) : ", math.floor(100.72)) 
print ("math.floor(math.pi) : ", math.floor(math.pi)) 
#log(x)
'''The natural logarithm of x, for x> 0.'''
print ("math.log(100.12) : ", math.log(100.12)) 
print ("math.log(100.72) : ", math.log(100.72)) 
print ("math.log(math.pi) : ", math.log(math.pi))
#log10(x)
'''The base-10 logarithm of x for x> 0.'''
print ("math.log10(100.12) : ", math.log10(100.12)) 
print ("math.log10(100.72) : ", math.log10(100.72)) 
print ("math.log10(119) : ", math.log10(119)) 
print ("math.log10(math.pi) : ", math.log10(math.pi))
#max(x1,x2,...)
'''The largest of its arguments: the value closest to positive infinity.'''
print ("max(80, 100, 1000) : ", max(80, 100, 1000)) 
print ("max(-20, 100, 400) : ", max(-20, 100, 400)) 
print ("max(-80, -20, -10) : ", max(-80, -20, -10)) 
print ("max(0, 100, -400) : ", max(0, 100, -400)) 
#min(x1,x2)
'''The smallest of its arguments: the value closest to negative infinity. '''
print ("min(80, 100, 1000) : ", min(80, 100, 1000)) 
print ("min(-20, 100, 400) : ", min(-20, 100, 400)) 
print ("min(-80, -20, -10) : ", min(-80, -20, -10)) 
print ("min(0, 100, -400) : ", min(0, 100, -400))
#modf(x)
'''The fractional and integer parts of x in a two-item tuple. 
 Both parts have the same sign as x. The integer part is returned as a float. '''
print ("math.modf(100.12) : ", math.modf(100.12)) 
print ("math.modf(100.72) : ", math.modf(100.72)) 
print ("math.modf(119) : ", math.modf(119)) 
print ("math.modf(math.pi) : ", math.modf(math.pi))  
#pow(x,y)
'''The value of x**y. '''
print ("math.pow(100, 2) : ", math.pow(100, 2)) 
print ("math.pow(100, -2) : ", math.pow(100, -2)) 
print ("math.pow(2, 4) : ", math.pow(2, 4)) 
print ("math.pow(3, 0) : ", math.pow(3, 0)) 
#round(x,[,n])
'''x rounded to n digits from the decimal point.
 Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is - 1.0. '''
print ("round(70.23456) : ", round(70.23456)) 
print ("round(56.659,1) : ", round(56.659,1)) 
print ("round(80.264, 2) : ", round(80.264, 2)) 
print ("round(100.000056, 3) : ", round(100.0000456, 3))
print ("round(-100.000056, 3) : ", round(-100.000056, 3)) 
#sqrt(x)
'''The square root of x for x > 0.'''
print ("math.sqrt(100) : ", math.sqrt(100)) 
print ("math.sqrt(7) : ", math.sqrt(7)) 
print ("math.sqrt(math.pi) : ", math.sqrt(math.pi)) 