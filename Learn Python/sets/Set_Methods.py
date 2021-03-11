nums = {0,1,2,3,4,5}
numss = {3,4,5,6,7,8,9}
print("%s"%'***sets***'.upper())
print("nums:",nums)
print("numss:",numss)
#Set Methods
print("%s"%'*set methods*'.title())
#Union
print("nums.union(numss):",nums.union(numss))
print("nums.union(numss):",numss.union(nums))
#Intersection
print("nums.intersection(numss):",nums.intersection(numss))
print("numss.intersection(nums):",numss.intersection(nums))
#Difference
print("nums.difference(numss):",nums.difference(numss))
print("numss.difference(nums):",numss.difference(nums))
#Symmetrical Difference
print("nums.symmetric_difference(numss):",nums.symmetric_difference(numss))
print("numss.symmetric_difference(nums):",numss.symmetric_difference(nums))
#Subset
print("nums.issubset(numss):",nums.issubset(numss))
print("numss.issubset(nums):",numss.issubset(nums))
print("{1,2,3}.issubset(nums):",{1,2,3}.issubset(nums))
#Superset
print("nums.issuperset(numss):",nums.issuperset(numss))
print("numss.issuperset(nums):",numss.issuperset(nums))
print("{0,1,2,3,4,5,6,7,8,9}.issuperset(nums):",{0,1,2,3,4,5,6,7,8,9}.issuperset(nums))
#Disjoint

print("nums.isdisjoint(numss):",nums.isdisjoint(numss))
print("numss.isdisjoint(nums):",numss.isdisjoint(nums))
print("{1,2,0}.isdisjoint(numss):",{1,2,0}.isdisjoint(numss))
print("len({1,2,0}&nums)==0:",len({1,2,0}&numss)==0) #less efficient
print("{1,2,0}&numss==set():",{1,2,0}&numss==set()) #even less efficient


