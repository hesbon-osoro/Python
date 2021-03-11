#Built-n List Functions & Methods
colors = ['Black','Green','Blue','Olive','Teal']
fruits = ['Orange','Mango','Pineapple','Apple']
str = 'Python programming is interesting'
print("colors:",colors)
print("fruits:",fruits)
#cmp(list1, list2)
'''No longer available in Python 3.'''
#print("cmp(colors,fruits):",cmp(colors,fruits))
print("%s"%'\n*functions*'.title())

#len(list)
'''Gives the total length of the list.'''
print("len(colors):",len(colors))
print("len(fruits):",len(fruits))
#max(list)
'''Returns item from the list with max value. '''
print("max(colors):",max(colors))
print("max(fruits):",max(fruits))
#min(list)
'''Returns item from the list with min value.'''
print("min(colors):",min(colors))
print("min(fruits):",min(fruits))
#list(seq)
'''Converts a tuple into list. '''
print("list(str):",list(str))
print("%s"%'\n*methods*'.title())
#list.append(obj)
'''Appends object obj to list'''
print('colors:',colors)
colors.append('Purple')
print("colors.append('Purple'):",colors)

# list.count(obj)
'''Returns count of how many times obj occurs in list'''
print("colors.count('Black'):",colors.count('Black'))
print("colors.count('Pink'):",colors.count('Pink'))

# list.extend(seq)
'''Appends the contents of seq to list'''
col = ['Red','Yellow','Grey']
print("colors:",colors)
print("col:",col)
colors.extend(col)
print("colors.extend(col):",colors)

# list.index(obj)
'''Returns the lowest index in list that obj appears'''
print("colors.index('Grey'):",colors.index('Grey'))
#print("colors.index('Maroon'):",colors.index('Maroon'))


# list.insert(index, obj)
'''Inserts object obj into list at offset index'''
colors.insert(3,'Maroon')
print("colors.insert(3,'Maroon'):",colors)

#list.pop(obj=list[-1])
'''Removes and returns last object or obj from list'''
print("colors.pop():",colors.pop())
print("colors:",colors)
print("colors.pop(3):",colors.pop(3))
print("colors:",colors)

# list.remove(obj)
'''Removes object obj from list'''
colors.remove('Olive')
print("colors.remove('Olive'):")
print("colors:",colors)

# list.reverse()
'''Reverses objects of list in place'''
colors.reverse()
print("colors.reverse():")
print("colors:",colors)

# list.sort([func])
'''Sorts objects of list, use compare func if given'''
print("colors:",colors)
colors.sort()
print("colors.sort(): ")
print("colors:",colors)
