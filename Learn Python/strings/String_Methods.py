#String Methods
str = 'this is my sample string...wow!!!'
print("Initial str: ",str)
#capitalize()
'''Capitalizes first letter of string'''
print('str.capitalize(): ',str.capitalize())

#center(width, fillchar)
'''Returns a string padded with fillchar with the original string centered
to a total of width columns. '''
print("str.center(len(str)+6,'*'): ",str.center(len(str)+6,'*'))
print("str.center(len(str)+5,'*'): ",str.center(len(str)+5,'*'))

#count(str, beg= 0,end=len(string))
'''Counts how many times str occurs in string or in a substring of string 
if starting index beg and ending index end are given. '''
#sub = 's'
print("str.count('s',0,len(str)):",str.count('s',0,len(str)))
#sub = 'exam'
print("str.count('exam',0,len(str)):",str.count('exam',0,len(str)))
#sub = 'sam'
print("str.count('sam',0,len(str)):",str.count('sam',0,len(str)))
print("str.count('t',0,10):",str.count('t',0,10))

#decode(encoding='UTF-8',errors='strict')
'''Decodes the string using the codec registered for encoding. 
encoding defaults to the default string encoding. '''
import base64
"""print("str.encode('base64','strict'):",str.encode('base64','strict'))
print("str.decode('base64','strict'):",str.decode('base64','strict'))"""
enc_str = base64.b64encode(str.encode('utf-8','strict'))
print('Encoded String:',enc_str)
print('Decoded string:',base64.b64decode(enc_str.decode('utf-8','strict')))

#encode(encoding='UTF-8',errors='strict')
'''Returns encoded string version of string; on error, default is to raise 
a ValueError unless errors is given with 'ignore' or 'replace'. '''
print("base64.b64encode(str.encode('utf-8',errors='strict'):",
      base64.b64encode(str.encode('utf-8',errors='strict')))
print("base64.b64encode(str.encode('utf-8','strict'):",
      base64.b64encode(str.encode('utf-8','strict')))

# endswith(suffix, beg=0, end=len(string))
'''Determines if string or a substring of string (if starting index beg and
 ending index end are given) ends with suffix; 
returns true if so and false otherwise.'''
#suffix = '!!'
print("str.endswith('!!'):",str.endswith('!!'))
print("str.endswith(''):",str.endswith('',12))
print("str.endswith(' '):",str.endswith(' ',12))
print("str.endswith('is',7):",str.endswith('is',0,7))

#expandtabs(tabsize=8)
'''Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if
 tabsize not provided. '''
tab_str = 'this is a\ttabbed text'
print("Original string:",tab_str)
print("Default expanded tab:",tab_str.expandtabs())
print("Double expanded tab: ",tab_str.expandtabs(16))
print("Tripple expanded tab:",tab_str.expandtabs(24))

#find(str, beg=0 end=len(string))
'''Determine if str occurs in string or in a substring of string if starting 
index beg and ending index end are given returns index if found and -1 otherwise. '''
print("str.find('samp'):",str.find('samp'))
print("str.find('samp', 10):",str.find('samp', 10))
print("str.find('samp', 40)",str.find('samp', 40))

#index(str, beg=0, end=len(string))  
'''Same as find(), but raises an exception if str not found.'''
print("str.index('samp'):",str.index('samp'))
print("str.index('samp', 10):",str.index('samp', 10))
'''print("str.index('samp', 40):",str.index('samp', 40))'''

#isalnum()
'''Returns true if string has at least 1 character and all characters are 
alphanumeric and false otherwise. '''
test = 'year2020wallahi'
print('test string:',test)
print("test.isalnum():",test.isalnum())
test = '2020'
print('test string:',test)
print("test.isalnum():",test.isalnum())
test = 'year wallahi'
print('test string:',test)
print("test.isalnum():",test.isalnum())


#isalpha()  
'''Returns true if string has at least 1 character and all characters are
 alphabetic and false otherwise.'''
test = 'year2020wallahi'
print('test string:',test)
print("test.isalpha():",test.isalpha())
test = 'yearwallahi'
print('test string:',test)
print("test.isalpha():",test.isalpha())

#isdigit()
'''Returns true if the string contains only digits and false otherwise. '''
test = 'yearwallahi'
print('test string:',test)
print("test.isdigit():",test.isdigit())
test = '2020/8'
print('test string:',test)
print("test.isdigit():",test.isdigit())
test = '2020'
print('test string:',test)
print("test.isdigit():",test.isdigit())

#islower()  
'''Returns true if string has at least 1 cased character and all cased 
characters are in lowercase and false otherwise.'''
test = '2020'
print('test string:',test)
print("test.islower():",test.islower())
test = 'is this lowercase?'
print('test string:',test)
print("test.islower():",test.islower())
test = 'is ThIS lowercase?'
print('test string:',test)
print("test.islower():",test.islower())

#isnumeric()
'''Returns true if a unicode string contains only numeric characters and false otherwise. '''
test = 'is ThIS numeric?'
print('test string:',test)
print("test.isnumeric():",test.isnumeric())
test = '2020'
print('test string:',test)
print("test.isnumeric():",test.isnumeric())

#isspace()
'''Returns true if string contains only whitespace characters and false otherwise.'''
test = '2020'
print('test string:',test)
print("test.isspace():",test.isspace())
test = ''
print('test string:',test)
print("test.isspace():",test.isspace())
test = ' '
print('test string:',test)
print("test.isspace():",test.isspace())

#istitle()
'''Returns true if string is properly "titlecased" and false otherwise.'''
test = 'Is This A Title? '
print('test string:',test)
print("test.istitle():",test.istitle())
test = 'Is this a title? '
print('test string:',test)
print("test.istitle():",test.istitle())

#isupper()
'''Returns true if string has at least one cased character and all cased characters are 
in uppercase and false otherwise.'''
print('str:',str,'\nstr.isupper():',str.isupper())
print('str.upper:',str.upper(),'\nstr.upper().isupper():',str.upper().isupper())

#join(seq)
'''Merges (concatenates) the string representations of elements in sequence seq into a string,
 with separator string.'''
#type = '*'
family = ('Grace', 'Leshan','Lynne', 'Alice') #this is a sequence of strings
print("'*'.join(family):",'*'.join(family))

#len(string)
'''Returns the length of the string'''
print("Length of string:\n",family,"; len(family):",len(family))
print("Length of string:\n%s; len(str):"%str,len(str))

#ljust(width[, fillchar])
'''Returns a space-padded string with the original string left-justified to a total of width columns.'''
just = 'this is a justified string test'
print("just.ljust(50,'*'): %s"%just.ljust(50,'*'))

#lower()
'''Converts all uppercase letters in string to lowercase.'''
print('test: %s\ntest.lower(): %s'%(test,test.lower()))
#lstrip()
'''Removes all leading whitespace in string.'''
whi_str = '    whitespaced string'
print("whi_str: %s\nwhi_str.lstrip(): %s"%(whi_str,whi_str.lstrip()))
star_str = '**** star string ****'
print("star_str: %s\nstar_str.lstrip('*'): %s"%(star_str,star_str.lstrip('*')))
num_str = '1234 this is a numstring 1234'
print("num_str: %s\nnum_str.lstrip(int(num_str)): %s"%(num_str,num_str.lstrip('1234')))
#get a way of using a function to strip digits

#maketrans()
'''Returns a translation table to be used in translate function.'''
intab = 'aeiotbps'
outtab = '43107695'
upp_in_tab = 'AEIOTSBG'
upp_out_tab ='43107586'
username = 'outcast'
trantab = username.maketrans(intab,outtab)
print('intab:  %7s\nouttab: %7s\nusername: %7s'%(intab,outtab,username))
print("username.maketrans(intab,outtab): ",username.maketrans(intab,outtab))
print("username.translate(trantab): ",username.translate(trantab))
print("'hacker'.upper(): ",'hacker'.upper().translate('hacker'.upper().maketrans(upp_in_tab,upp_out_tab)))
print("'outcast'.upper(): ",'outcast'.upper().translate('outcast'.upper().maketrans(upp_in_tab,upp_out_tab)))
print("hacker: ",'hacker'.translate('hacker'.maketrans(intab,outtab)))
print("'blackhat'.upper(): ",'blackhat'.upper().translate('blackhat'.upper().maketrans(upp_in_tab,upp_out_tab)))

#max(str)
'''Returns the max alphabetical character from the string str.'''
print("max(test): "+max(test))
print("min(test): "+min(test))

#min(str)
'''Returns the min alphabetical character from the string str.'''
min_str = 'assdfdgncvxdertes'
print("min(min_str): "+min(min_str))
min_str = 'wazimu.com'
print("min(min_str): "+min(min_str))

#replace(old, new [, max])
'''Replaces all occurrences of old in string with new or at most max occurrences if max given.'''
tense = 'This is a text to be tested'
print("Present tense: tense :- "+tense)
print("Past tense: tense.replace(' is ', ' was '):- "+tense.replace(' is ',' was '))
print("Wrong correction: tense.replace('is','was'):- "+tense.replace('is','was'))
print("tense: %s\ntense.replace('is','was',1): %s"%(tense,tense.replace('is','was',1)))

#rfind(str, beg=0,end=len(string))
'''Same as find(), but search backwards in string.'''
r_str = 'lets find a string in reverse'
rev = 'reverse'
print("r_str:",r_str)
print("r_str.rfind('in'):",r_str.rfind('in'))
print("r_str.rfind('in',0,len(r_str)):",r_str.rfind('in',0,len(r_str)))
print("r_str.rfind('in',0,10):",r_str.rfind('in',0,10))
print("r_str.rfind('in',10,0):",r_str.rfind('in',10,0))
print("rev: ",rev)
print("rev.find('er'):",rev.find('er'))
print("rev.rfind('er'):",rev.rfind('er'))
print("rev[0:2]:",rev[0:2])
print("rev[-len(rev):]:",rev[-len(rev):])
print("rev[:-len(rev)]:",rev[:-len(rev)])
print("rev.rfind('er',-len(rev),6):",rev.rfind('er',-len(rev),6))
print("rev.find('er',-len(rev),6):",rev.find('er',-len(rev),6))
print("rev.rfind('er',len(rev),6):",rev.rfind('er',len(rev),6))
print("rev.find('er',len(rev),6):",rev.find('er',len(rev),6))


#rindex( str, beg=0, end=len(string))
'''Same as index(), but search backwards in string.'''
print("r_str.replace('string','index'):",r_str.replace('string','index'))
print("r_str.rindex('in'):",r_str.replace('string','index').rindex('in'))
'''print("r_str.replace('string','index').rindex('my'):",r_str.replace('string','index').rindex('my'))'''

#rjust(width,[, fillchar])
'''Returns a space-padded string with the original string right-justified to a total of width columns.'''
print("just: "+just)
print("just.rjust(len(just)+10,'*')): ",just.rjust(len(just)+10,'*'))

#rstrip()
'''Removes all trailing whitespace of string.'''
print("star_str:",star_str)
print("star_str.rstrip('*'):",star_str.rstrip('*'))


#split(str="", num=string.count(str))
'''Splits string according to delimiter str (space if not provided) and returns list of substrings; 
split into at most num substrings if given.'''
split = "let's do a split test"
print("split:",split)
print("split.split():",split.split())
print("split.split('i'):",split.split('l'))
print("split.split('s',2):",split.split('s',2))


#splitlines( num=string.count('\n'))
'''Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.'''
'''***syntax***
str.splitlines( num=string.count('\n'))'''
lines = "this is a \nstring \nwith \nsplitted lines"
print("lines:",lines)
print("split.replace('split','splitlines').splitlines():",split.replace('split','split\nlines').splitlines())
print("lines.splitlines():",lines.splitlines())
print("lines.splitlines():",lines.splitlines(1))


#startswith(str, beg=0,end=len(string))
'''Determines if string or a substring of string (if starting index beg and ending index end are given)
 starts with substring str; returns true if so and false otherwise.'''
print("split:",split)
print("split.startswith('let'):",split.startswith('let'))
print("split.startswith('do',6,12):",split.startswith('do',6,12))
print("split.startswith('let',3,12):",split.startswith('let',3,12))

#strip([chars])
'''Performs both lstrip() and rstrip() on string'''
print("star_str:",star_str)
print("star_str.strip('*'):",star_str.strip('*'))


#swapcase()
'''Inverts case for all letters in string.'''
print("test:",test)
print("test.swapcase():",test.swapcase())
print("star_str:",star_str)
print("star_str.swapcase():",star_str.swapcase())

#title()
'''Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.'''
print("star_str:",star_str)
print("star_str.title():",star_str.title())
print("star_str.capitalize():",star_str.capitalize())

#translate(table, deletechars="")
'''Translates string according to translation table str(256 chars), removing those in the del string.'''
alphas = 'aciolgs'
nums = '@<!0/9$'
message = 'Programming with Python is full of fun'
print("message:",message)
print("message.translate(message.maketrans(alphas,nums)):",message.translate(message.maketrans(alphas,nums)))

#upper()
'''Converts lowercase letters in string to uppercase.'''
print("star_str:",star_str)
print("star_str.upper():",star_str.upper())
print("star_str.title():",star_str.title())

#zfill (width)
'''Returns original string leftpadded with zeros to a total of width characters; 
intended for numbers, zfill() retains any sign given (less one zero).'''
print("message:",message)
print("message.zfill(50):",message.zfill(50))


#isdecimal()
'''Returns true if a unicode string contains only decimal characters and false otherwise.'''
dec = 'nodecimal'
print("dec:",dec.isdecimal())
dec = '12'
print("dec:",dec)
print("dec.isdecimal(): ",dec.isdecimal())
dec = '123 024'
print("dec:",dec)
print("dec.isdecimal(): ",dec.isdecimal())