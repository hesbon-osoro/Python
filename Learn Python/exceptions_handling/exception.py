#What is an exception
print('*What is an Exception*')
print("""An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. An exception is a Python object that represents an error. 
When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and quits.""")

print("""Handling an Exception If you have some suspicious code that may raise an exception, you can defend your program by placing the suspicious code in a try: block. After the try: block, include an except: statement, followed by a block of code which handles the problem as elegantly as possible.

Syntax 
Here is simple syntax of try....except...else blocks- 
try: 
   You do your operations here 
   ...................... 
   except ExceptionI: 
   If there is ExceptionI, then execute this block. 
    except ExceptionII: 
   If there is ExceptionII, then execute this block. 
   ...................... 
    else: 
   If there is no exception then execute this block. """)
print("""Here are few important points about the above-mentioned syntax- 
    * A single try statement can have multiple except statements. This is useful when the try block contains statements that may throw different types of exceptions.  
    * You can also provide a generic except clause, which handles any exception.  
    * After the except clause(s), you can include an else-clause. The code in the else- block executes if the code in the try: block does not raise an exception.  
    * The else-block is a good place for code that does not need the try: block's protection. """)

print("\nExample")
print("This example opens a file, writes content in the file and comes out gracefully because there is no problem at all. ")
print("""try:
    fh = open('testfile','w')
    fh.write('This is my test file for exception handling!')
except IOError:
    print("Error: can't find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()
    """)
try:
    fh = open('testfile','w')
    fh.write('This is my test file for exception handling!')
except IOError:
    print("Error: can't find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()
print("\nExample")
print("This example tries to open a file where you do not have the write permission, so it raises an exception- ")
print("""try:
    fh = open('testfile0','r')
except IOError:
    print("Error: can't find or read data")
else:
    print('Written content in the file successfully')""")
print()
try:
    fh = open('testfile0','r')
except IOError:
    print("Error: can't find or read data")
else:
    print('Written content in the file successfully')

print("\nThe except Clause with No Exceptions ")
print("""You can also use the except statement with no exceptions defined as follows- 
try: 
   You do your operations here 
   ...................... 
except: 
   If there is any exception, then execute this block. 
   ...................... 
else: 
   If there is no exception then execute this block.  

This kind of a try-except statement catches all the exceptions that occur. Using this kind of try-except statement is not considered a good programming practice though, because it catches all exceptions but does not make the programmer identify the root cause of the problem that may occur. """)

print("The except Clause with Multiple Exceptions")
print("""You can also use the same except statement to handle multiple exceptions as follows- 
try: 
   You do your operations here 
   ...................... 
except(Exception1[, Exception2[,...ExceptionN]]]): 
   If there is any exception from the given exception list,  
   then execute this block. 
   ......................
else: 
   If there is no exception then execute this block. """)

print("The except Clause with Multiple Exceptions")
print("""You can also use the same except statement to handle multiple exceptions as follows- 
try: 
   You do your operations here 
   ...................... 
except(Exception1[, Exception2[,...ExceptionN]]]): 
   If there is any exception from the given exception list,  
   then execute this block. 
   ...................... 
else: 
   If there is no exception then execute this block.  """)

print("\nThe try-finally Clause")
print("""You can use a finally: block along with a try: block. The finally: block is a place to put any code that must execute, whether the try-block raised an exception or not. The syntax of the try-finally statement is this- 
try: 
   You do your operations here; 
   ...................... 
   Due to any exception, this may be skipped. 
finally: 
   This would always be executed. 
   ...................... 
*Note: You can provide except clause(s), or a finally clause, but not both. You cannot use else clause as well along with a finally clause. """)
print("""try:
    fh=open('testfile1','w')
    fh.write("This is my test file for exception handling!")
finally:
    print("Error: can't find file or read data")
    fh.close()\n""")

try:
    fh=open('testfile1','w')
    fh.write("This is my test file for exception handling!")
finally:
    print("Error: can't find file or read data")
    fh.close()
#but this code opens file and writes into it but displays the exception error!!!

print("\nSame example can be written more cleanly as follows-\n")
print("""try:
    fh = open('testfile3','w')
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can't find file or read data")
""")
try:
    fh = open('testfile3','w')
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can't find file or read data")
print()
print("""When an exception is thrown in the try block, the execution immediately passes to the finally block. After all the statements in the finally block are executed, the exception is raised again and is handled in the except statements if present in the next higher layer of the try-except statement. """)
print()
print("Argument of an Exception")
print("""An exception can have an argument, which is a value that gives additional information about the problem. The contents of the argument vary by exception. You capture an exception's argument by supplying a variable in the except clause as follows- 

try: 
   You do your operations here 
   ...................... 
except ExceptionType as Argument: 
   You can print value of Argument here...

If you write the code to handle a single exception, you can have a variable follow the name of the exception in the except statement. If you are trapping multiple exceptions, you can have a variable follow the tuple of the exception. 
This variable receives the value of the exception mostly containing the cause of the exception. The variable can receive a single value or multiple values in the form of a tuple. This tuple usually contains the error string, the error number, and an error location. """)

print("\nExample\nFollowing is an example for a single exception- ")
#define a function here
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument does not contain numbers\n",Argument)

print("""def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument does not contain numbers\\n",Argument)\n""")
#call above function here
print("\ntemp_convert('xyz'):",temp_convert('xyz'))
print("temp_convert('abc')")
temp_convert('abc')
print("temp_convert('xyz'):",temp_convert(100))
print("temp_convert('400'):")
temp_convert(400)
print("\n*Raising an Exception*")
print("""You can raise exceptions in several ways by using the raise statement. The general syntax for the raise statement is as follows- 

Syntax 
    raise [Exception [, args [, traceback]]] 
Here, Exception is the type of exception (for example, NameError) and argument is a value for the exception argument. The argument is optional; if not supplied, the exception argument is None. 
The final argument, traceback, is also optional (and rarely used in practice), and if present, is the traceback object used for the exception. 

Example 
An exception can be a string, a class or an object. Most of the exceptions that the Python core raises are classes, with an argument that is an instance of the class. Defining new exceptions is quite easy and can be done as follows- 
def functionName( level ): 
    if level <1: 
        raise Exception(level) 
        # The code below to this would not be executed 
        # if we raise the exception 
    return level 
*Note: In order to catch an exception, an "except" clause must refer to the same exception thrown either as a class object or a simple string. For example, to capture the above exception, we must write the except clause as follows- 
try: 
   Business Logic here... 
except Exception as e: 
   Exception handling here using e.args...
else: 
   Rest of the code here... """)
print("\nThe following example illustrates the use of raising an exception-\n")
print("""def functionName(level):
    if level<1:
        raise Exception(level)
        #the code below to this would not be executed
        #if we raise the exception
    return level
try:
    l=functionName(-10)
    print("level=",l)
except Exception as e:
    print("error in level argument",e.args[0])\n""")
def functionName(level):
    if level<1:
        raise Exception(level)
        #the code below to this would not be executed
        #if we raise the exception
    return level
try:
    l=functionName(-10)
    print("level=",l)
except Exception as e:
    print("error in level argument",e.args[0])

print("\n*User-Defined Exceptions*")
print("""Python also allows you to create your own exceptions by deriving classes from the standard built-in exceptions. 
Here is an example related to RuntimeError. Here, a class is created that is subclassed from RuntimeError. This is useful when you need to display more specific information when an exception is caught. 
In the try block, the user-defined exception is raised and caught in the except block. The variable e is used to create an instance of the class Networkerror. 
class Networkerror(RuntimeError): 
   def __init__(self, arg): 
      self.args = arg 
So once you have defined the above class, you can raise the exception as follows- 
try: 
   raise Networkerror("Bad hostname") 
except Networkerror,e: 
   print e.args""")