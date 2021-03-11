#Modules
print("***Modules***")
print("""A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference. 
Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.""")
print("*Example*")
print("The Python code for a module named aname normally resides in a file namedaname.py. Here is an example of a simple module, support.py- ")
print("""def print_func( par ): 
   print ("Hello : ", par) 
   return """)
def print_func(par):
    print ("Hello : ",par)
    return
print_func('Wazimu')
print("print_func('Wazimu')")
print_func(14)
print("print_func(14)")

print("*The import Statement*")
print("""The import Statement You can use any Python source file as a module by executing an import statement in some other Python source file. The import has the following syntax- 
import module1[, module2[,... moduleN] 
When the interpreter encounters an import statement, it imports the module if the module is present in the search path. A search path is a list of directories that the interpreter searches before importing a module. For example, to import the module hello.py, you need to put the following command at the top of the script- """)
#Import module
#import support
print("import support")
#Now you can call defined function that module as follows
#support.print_func('Python') #The function raises an error due to missing paranthesis
print("support.print_func('Python')")
print("The above code wont execute in python 3")
print("""
A module is loaded only once, regardless of the number of times it is imported. This prevents the module execution from happening repeatedly, if multiple imports occur. """)

print("\n*The from...import Statement *")
print("""Python's from statement lets you import specific attributes from a module into the current namespace. The from...import has the following syntax- 
from modname import name1[, name2[, ... nameN]] 
For example, to import the function fibonacci from the module fib, use the following statement-""")


#Fibonacci numbers module
def fib(n): #return Fibonacci series up to n
    result = []
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result
#from modules import fib
#fib(100)
"""import this file in a terminal or cmd then run the two commented lines"""
print("fib(100):",fib(100))

print("""\nThis statement does not import the entire module fib into the current namespace; it just introduces the item fibonacci from the module fib into the global symbol table of the importing module. """)

print("\n*The from...import * Statement: *")
print("""It is also possible to import all the names from a module into the current namespace by using the following import statement- 
  from modname import * 
This provides an easy way to import all the items from a module into the current namespace; however, this statement should be used sparingly.""")

print("*Executing Modules as Scripts*")
print("""Within a module, the module’s name (as a string) is available as the value of the global variable __name__. The code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__".  """)

#Redefinition of Fibonacci numbers module
def fib2(n):
    res = []
    a,b=0,1
    while b<n:
        res.append(b)
        a,b=b,a+b
    return res
if __name__ == "__main__":
    f=fib2(200)
    print("f=fib2(200)")
    print("f:",f)

print("\n*Locating Modules*")
print("When you import a module, the Python interpreter searches for the module in the following sequences-")
print("* The current directory.")
print("* If the module is not found, Python then searches each directory in the shell variable PYTHONPATH. ")
print("* If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python3/.")

print("""The module search path is stored in the system module sys as the sys.path variable. The sys.path variable contains the current directory, PYTHONPATH, and the installation- dependent default.""")

print("\n*The PYTHONPATH Variable *")
print("""The PYTHONPATH is an environment variable, consisting of a list of directories. The syntax of PYTHONPATH is the same as that of the shell variable PATH.
Here is a typical PYTHONPATH from a Windows system- 
  set PYTHONPATH=c:\python34\lib; 
And here is a typical PYTHONPATH from a UNIX system- 
  set PYTHONPATH=/usr/local/lib/python """)

print("\n*Namespaces and Scoping *")
print("""Variables are names (identifiers) that map to objects. A namespace is a dictionary of variable names (keys) and their corresponding objects (values). """)
print("* A Python statement can access variables in a local namespace and in the global namespace. If a local and a global variable have the same name, the local variable shadows the global variable. ")
print("* Each function has its own local namespace. Class methods follow the same scoping rule as ordinary functions. ")
print("* Python makes educated guesses on whether variables are local or global. It assumes that any variable assigned a value in a function is local. ")
print("* Therefore, in order to assign a value to a global variable within a function, you must first use the global statement. ")
print("* The statement global VarName tells Python that VarName is a global variable. Python stops searching the local namespace for the variable.")

print("""\nFor example, we define a variable Money in the global namespace. Within the function Money, we assign Money a value, therefore Python assumes Money as a local variable.  
However, we accessed the value of the local variable Money before setting it, so an UnboundLocalError is the result. Uncommenting the global statement fixes the problem. """)

money = 2000
def add_money():
    #if we ignore the next line, error occurs
    global money #UnnboundLocalError: local variable 'money' reference before assignment
    money = money + 500
    #money += 500 #works without using the 'global' keyword
    return
print(money)
add_money()
print(money)
print("*The dir() Function")
print("""The dir() built-in function returns a sorted list of strings containing the names defined by a module. 
The list contains the names of all the modules, variables and functions that are defined in a module. Following is a simple example-""")
import  math
print("import math")
print("dir(math):",dir(math))
print("\nHere, the special string variable __name__ is the module's name, and __file__is the filename from which the module was loaded. ")
import modules
print("import modules")
print("dir(modules):",dir(modules))
print("\n*The globals() and locals() Functions*")
print("The globals() and locals() functions can be used to return the names in the global and local namespaces depending on the location from where they are called. ")
print("* If locals() is called from within a function, it will return all the names that can be accessed locally from that function. ")
print("* If globals() is called from within a function, it will return all the names that can be accessed globally from that function. ")
print("\nThe return type of both these functions is dictionary. Therefore, names can be extracted using the keys() function. ")

#Sample function
def my_func(var1):
    n,m=10,100
    print("locals():",locals())
    print("globals():",globals())
    print("locals().keys():", locals().keys())
    print("globals().keys():", globals().keys())
    print("locals().values():", locals().values())
    print("globals().values():", globals().values())
my_func("Sample function")
print()
print("*The reload() Function*")
print("""When a module is imported into a script, the code in the top-level portion of a module is executed only once. 
Therefore, if you want to reexecute the top-level code in a module, you can use the reload() function. The reload() function imports a previously imported module again. The syntax of the reload() function is this- 
   reload(module_name)
Here, module_name is the name of the module you want to reload and not the string containing the module name. For example, to reload hello module, do the following- 
   reload(hello)""")

print("*Packages in Python *")
print("""A package is a hierarchical file directory structure that defines a single Python application environment that consists of modules and subpackages and sub-subpackages, and so on. 
Consider a file Pots.py available in Phone directory. This file has the following line of source code-""")
print("""def Pots(): 
   print ("I'm Pots Phone")   
Similarly, we have other two files having different functions with the same name as above. They are − 
* Phone/Isdn.py file having function Isdn()  Phone/G3.py file having function G3() 
Now, create one more file __init__.py in the Phone directory- 
* Phone/__init__.py 
To make all of your functions available when you have imported Phone, you need to put explicit import statements in __init__.py as follows- 
from Pots import Pots 
from Isdn import Isdn 
from G3 import G3 
After you add these lines to __init__.py, you have all of these classes available when you import the Phone package. 
#!/usr/bin/python3 
# Now import your Phone Package. 
import Phone 
Phone.Pots() 
Phone.Isdn() 
Phone.G3() """)

print("\nIn the above example, we have taken example of a single function in each file, but you can keep multiple functions in your files. You can also define different Python classes in those files and then you can create your packages out of those classes. ")