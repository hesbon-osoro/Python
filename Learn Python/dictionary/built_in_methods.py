#Built-in Dictionary Functions & Methods
#Methods
catalogue = {'Name':'Python 3', 'Type': 'Programming Book','File':'PDF','Size':'2,991,500 bytes',
             'Pages':'512','Price':0.0,'Site':'http://www.tutorialspoint.com'}
keyboard = {'nums':'0123456789','alphas':'abcdefghijklmnopqrstuvwxyz',
              'spec_char':'!@#$%^&*()'}
dict_p = {'lang':'Python','dev':'Guido van Rossum','lab':'NRIMCS'}
dict_copy = dict_p.copy()
print("catalogue:",catalogue)
print("keyboard:",keyboard)
print("%s"%'*methods*'.title())

#dict.clear()
#Removes all elements of dictionary dict.
print("dict_p:",dict_p)
print("len(dict_p):",len(dict_p))
dict_p.clear()
print("dict_p.clear()")
print("dict_p:",dict_p)
print("len(dict_p):",len(dict_p))

#dict.copy()
#Returns a shallow copy of dictionary dict.
print("dict_copy = dict_p.copy()")
print("dict_copy:",dict_copy)

#dict.fromkeys()
#Create a new dictionary with keys from seq and values set to value.
seq = ('name','age','sex')
print('seq:',seq)
dummy = dict.fromkeys(seq)
print("dummy = dict.fromkeys()")
print("dummy:",dummy)
dummy = dummy.fromkeys(seq,10)
print("dummy = dummy.fromkeys(seq,10)")
print('dummy:',dummy)
dummy['name'] = 'Chunk'
dummy['age'] = 10
dummy['sex'] = 'Male'
print("dummy['name'] = 'Chunk'")
print("dummy['age'] = 10 ")
print("dummy['sex'] = 'Male'")

print("dummy:",dummy)

#dict.get(key, default=None)
#For key key, returns value or default if key not in dictionary.
print("catalogue.get('Name'):",catalogue.get('Name'))
print("catalogue.get('Name','NA'):",catalogue.get('Name','NA'))
print("catalogue.get('Age','NA'):",catalogue.get('Age','NA'))
#dict.has_key(key)
#Removed, use the in operation instead.
#print("dummy.has_key('name'):",dummy.has_key('name'))
print("'name' in dummy:",'name' in dummy)
print("'value' in dummy:",'value' in dummy)

#dict.items()
#Returns a list of dict's (key, value) tuple pairs.
print("catalogue.items():",catalogue.items())
print("keyboard.items():",keyboard.items())


#dict.keys()
#Returns list of dictionary dict's keys.
print("catalogue.keys():",catalogue.keys())
print("keyboard.keys():",keyboard.keys())

#dict.setdefault(key, default=None)
#Similar to get(), but will set dict[key]=default if key is not already in dict.
web = ('html','css','bootstrap','js')
print("web:",web)
print("type(web):",type(web))
web_dict = dict.fromkeys(web)
print("web_dict = dict.fromkeys(web)")
print("web_dict:",web_dict)
print("web_dict.setdefault('jQuery','Querying'):",web_dict.setdefault('jQuery','Querying'))
print(web_dict)

#dict.update(dict2)
#Adds dictionary dict2's key-values pairs to dict.
web_dict.update({'js':'dom manipulation'})
web_dict.update({'html':'markup'})
web_dict.update({'css':'styling'})
web_dict.update({'php':'database'})
web_dict.update({'bootstrap':'beautifying'})

print("web_dict.update({'js':'dom manipulation'})")
print("web_dict.update({'html':'markup'})")
print("web_dict.update({'css':'styling'})")
print("web_dict.update({'php':'database'})")
print("web_dict.update({'bootstrap':'beautifying'})")
print(web_dict)

#dict.values()
#Returns list of dictionary dict's values.
print("catalogue.values():",catalogue.values())
print("keyboard.values():",keyboard.values())
print("dummy.values():",dummy.values())
print("web_dict.values():",web_dict.values())

