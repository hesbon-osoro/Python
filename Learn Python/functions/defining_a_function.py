#Defining a function
print("%s"%'Defining a Function'.title())
print("You can define functions to provide the required functionality. Here are simple rules to define a function in Python. ")
print("* Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ). ")
print("* Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses. ")
print("* The first statement of a function can be an optional statement - the documentation string of the function or docstring. ")
print("* The code block within every function starts with a colon (:) and is indented. ")
print("The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.")

print("\n*Syntax*")
print("""def functionname( parameters ): 
   "function_docstring" 
   function_suite 
   return [expression] """)

print("By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.")
print("\nExample :view source code:)")
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return