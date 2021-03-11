#Function Arguments
print("You can call a function by using the following types of formal arguments- ")
print("* Required arguments ")
print("* Keyword arguments ")
print("* Default arguments ")
print("* Variable-length arguments ")

print("\n*Required Arguments*")
print("""Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments in the function call should match exactly with the function definition. 
To call the function printme(), you definitely need to pass one argument, otherwise it gives a syntax error as follows-""")

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return
# Now you can call printme function
#printme()
print("calling the function as *printme()* raises an error")
print("\n*Keyword Arguments*")
print("""Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name. 
This allows you to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters. You can also make keyword calls to the printme() function in the following ways- """)

print("calling the function by keyword such as *printme(str = 'My string')* is valid")
printme(str="My string")
print("The following example gives a clearer picture. Note that the order of parameters does not matter.")

print("when defining: def *printinfo(name, age):*...")
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return
# Now you can call printinfo function
printinfo( age=50, name="miki" )
print("when calling the function: *printinfo(age=50,name='miki')*")

print("*Default Arguments*")
print("""A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument. The following example gives an idea on default arguments, it prints default age if it is not passed.""")
# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print("Age ", age)
   return
   # Now you can call printinfo function


printinfo(age=50, name="miki")
printinfo(name="miki")
printme("when calling the function: *printinfo(age=50, name='miki')*")
printme("when calling by default arguments *printinfo(name='miki')*")

print("*Variable-length Arguments*")
print("""You may need to process a function for more arguments than you specified while defining the function. These arguments are called *variable-length* arguments and are not named in the function definition, unlike required and default arguments. 
Syntax for a function with non-keyword variable arguments is given below- """)
print("""def functionname([formal_args,] *var_args_tuple ): 
   "function_docstring" 
   function_suite 
   return [expression] """)

print("""An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments. This tuple remains empty if no additional arguments are specified during the function call. Following is a simple example-""")
#Function definition is here
def printin(arg1,*vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for i in vartuple:
        print(i)
    return
#Now you can call printin function
print("printin(10)")
printin(10)
print("printin(70,60,50)")
printin(70,60,50)
