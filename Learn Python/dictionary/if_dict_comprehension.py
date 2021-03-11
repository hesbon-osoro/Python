# Python code to demonstrate dictionary
# comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)
