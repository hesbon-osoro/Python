#Basic Tuple Operation
nums = (0,1,2,3,4)
num = (5,6,7,8,9)
print("nums:",nums)
print("num:",num)

#len(tup)
print("%s"%'\n*length*'.title())
print("len(nums):",len(nums))
print("lens(num):",len(num))

#concatenation
print("%s"%'\n*concatenation*'.title())
print("nums+num:",nums+num)

#repetition
print("%s"%'\n*repetition*'.title())
print("nums*3:",nums*3)

#membership
print("%s"%'\n*membership*'.title())
print("6 in nums:",6 in nums)
print("3 in nums:",3 in nums)

#iteration
print("%s"%'\n*iteration*'.title())
for n in nums+num:
    print(n, end=' ')