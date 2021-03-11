#Exceptions Handling
print('***Exceptions Handling***')
print("""Python provides two very important features to handle any unexpected error in your Python programs and to add debugging capabilities in them- 
    * Exception Handling.    
    * Assertions. 
*Standard Exceptions* 
Here is a list of Standard Exceptions available in Python. """)
print('EXCEPTION NAME\t\t\tDESCRIPTION ')

print('Exception \t\tBase class for all exceptions ')
print('StopIteration \t\tRaised when the next() method of an iterator does not point to any object.')
print('SystemExit \t\tRaised by the sys.exit() function. ')
print('StandardError \t\tBase class for all built-in exceptions except StopIteration and SystemExit. ')
print('ArithmeticError \t\tBase class for all errors that occur for numeric calculation. ')
print('OverflowError \t\tRaised when a calculation exceeds maximum limit for a numeric type. ')
print('FloatingPointError \t\tRaised when a floating point calculation fails. ')
print('ZeroDivisonError \t\tRaised when division or modulo by zero takes place for all numeric types. ')
print('AssertionError \t\tRaised in case of failure of the Assert statement. ')
print('AttributeError \t\tRaised in case of failure of attribute reference or assignment.')
print('EOFError \t\tRaised when there is no input from either the raw_input() or input() function and the end of file is reached. ')
print('ImportError \t\tRaised when an import statement fails. ')
print('KeyboardInterrupt \t\tRaised when the user interrupts program execution, usually by pressing Ctrl+c. ')
print('LookupError \t\tBase class for all lookup errors. ')
print('IndexError \t\tRaised when an index is not found in a sequence. ')
print('KeyError \t\tRaised when the specified key is not found in the dictionary. ')
print('NameError \t\tRaised when an identifier is not found in the local or global namespace.')
print('UnboundLocalError \t\tRaised when trying to access a local variable in a function or method but no value has been assigned to it. ')
print('EnvironmentError \t\tBase class for all exceptions that occur outside the Python environment. ')
print('IOError \t\tRaised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.')
print('OSError \t\tRaised for operating system-related errors. ')
print('SyntaxError \t\tRaised when there is an error in Python syntax. ')
print('IndentationError \t\tRaised when indentation is not specified properly. ')
print('SystemError \t\tRaised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit. ')
print('SystemExit \t\tRaised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.')
print('TypeError \t\tRaised when an operation or function is attempted that is invalid for the specified data type. ')
print('ValueError \t\tRaised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.')
print('RuntimeError \t\tRaised when a generated error does not fall into any category.')
print('NotImplementedError \t\tRaised when an abstract method that needs to be implemented in an inherited class is not actually implemented. ')

print('\n*Assertions in Python*')
print("""
An assertion is a sanity-check that you can turn on or turn off when you are done with your testing of the program. 
    * The easiest way to think of an assertion is to liken it to a raise-if statement (or to be more accurate, a raise-if-not statement). An expression is tested, and if the result comes up false, an exception is raised.  
    * Assertions are carried out by the assert statement, the newest keyword to Python, introduced in version 1.5.  
    * Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output. 
""")