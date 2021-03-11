#Python Lists
import math
languages = ['Python','Java','C#','C++','C','Perl','Ruby','Android','Swift']
nums = [0,1,2,3,4,5,6,7,8,9]
days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print("%s"%'***LISTS***'.rjust(round(len(months)+12)),'   ')
print("%s"%'\n*accessing list values*'.title())
print("%s"%languages[1:])
print("",languages[-len(languages)])
print("",languages[len(languages)-1])
print("",languages[-1:])
print("",languages[:-1])
print("",languages[-3:])
print("%s"%'\n*updating list values*'.title())
print("%s"%languages)
languages[2] = 'R'
print("%s"%languages)
print("%s"%'\n*deleting list values*'.title())
print("%s"%languages)
del languages[6]
print("%s"%languages)
