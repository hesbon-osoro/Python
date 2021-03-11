# Python program to demonstrate list comprehension in Python

# below list contains square of all odd numbers from
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print (odd_square)

# for understanding, above generation is same as,
odd_square = []
for x in range(1, 11):
	if x % 2 == 1:
		odd_square.append(x**2)
print (odd_square)

# below list contains power of 2 from 1 to 8
power_of_2 = [2 ** x for x in range(1, 9)]
print (power_of_2)

# below list contains prime and non-prime in range 1 to 50
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print (primes)

# list for lowering the characters
print ([x.lower() for x in ["A","B","C"]] )

# list which extracts number
string = "my phone number is : 11122 !!"

print("\nExtracted digits")
numbers = [x for x in string if x.isdigit()]
print (numbers)

# A list of list for multiplication table
a = 5
table = [[a, b, a * b] for b in range(1, 11)]

print("\nMultiplication Table")
for i in table:
	print (i)
