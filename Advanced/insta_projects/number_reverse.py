number = 12345
remainder = []
print("original number: ",number)
while number != 0:
    remainder.append(number % 10)
    number //= 10

reverse = "".join(map(str, remainder))
print("""reverse = "".join(map(str, remainder))""")
print("number reverse:",reverse)