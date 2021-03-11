import functools

# filtering odd numbers
lst = filter(lambda x : x % 2 == 1, range(1, 20))
print (list(lst))

# filtering odd square which are divisible by 5
lst = filter(lambda x : x % 5 == 0,
	[x ** 2 for x in range(1, 11) if x % 2 == 1])
print (list(lst))

# filtering negative numbers
lst = filter((lambda x: x < 0), range(-5,5))
print (list(lst))

# implementing max() function, using
print (functools.reduce(lambda a,b: a if (a > b) else b, [7, 12, 45, 100, 15]))
