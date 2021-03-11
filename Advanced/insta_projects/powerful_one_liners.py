#Swap two variables
a = 5
b = 10
print("a = ", a, " b = ", b)
a,b = b,a
print("a = ", a, "b = ", b)

#Factorial of a number
n = 5
import functools as ft
print("ft.reduce(lambda x,y:x*y, range(1,n+1)):",ft.reduce(lambda x,y:x*y, range(1,n+1)))

#List comprehension
# [x*x for x in range(11)]
print("[x*x for x in range(11)]:", [x*x for x in range(11)])

#Fibonacci Series
# print("lambda x:x if x<=1 else fib(x-1)+fib(x-2):",lambda x:x if x<=1 else fib(x-1)+fib(x-2))

#Subsets of a set
from itertools import combinations
print("list(combinations([1,2,3,4,5],3)):",list(combinations([1,2,3,4,5],3)))
print("list(combinations([1,2,3,4],2))",list(combinations([1,2,3,4],2)))
#Space separated input
# print("Type something: ", end='')
# print("list(input().split()):",list(input().split()))
