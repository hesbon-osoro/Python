#Sets versus multisets

alpha_set = {'a','b','b','d','c','e','e'}
alpha_list = ['a','b','b','d','c','e','e']
print("alpha_set:",alpha_set)
print("alpha_list:",alpha_list)

from collections import Counter
print("Counter(alpha_list):",Counter(alpha_list))
print("Counter(alpha_set): ",Counter(alpha_set))
