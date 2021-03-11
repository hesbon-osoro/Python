
#Set of Sets
nums = {0,1,2,3,4,5,6,7,8,9}
alpha = {'a','b','c','d','e','f','g'}
print("***SETS***")
print("nums:",nums)
print("alpha:",alpha)
#print("{alpha,nums}",{alpha,nums}) #unhashable
print("{frozenset(nums),frozenset(alpha)}:\n",{frozenset(nums),frozenset(alpha)})