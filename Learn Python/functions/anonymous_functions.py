#The Anonymous Functions

print("*The Anonymous Functions*")
print("""These functions are called anonymous because they are not declared in the standard manner by using the def keyword. You can use the lambda keyword to create small anonymous functions. """)
print("* Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.")
print("* An anonymous function cannot be a direct call to print because lambda requires an expression.")
print("* Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.")
print("* Although it appears that lambdas are a one-line version of a function, they are not equivalent to inline statements in C or C++, whose purpose is to stack allocation by passing function, during invocation for performance reasons.")
print("*\nSyntax*")
print("""The syntax of lambda function contains only a single statement, which is as follows- 
lambda [arg1 [,arg2,.....argn]]:expression""")
print("Following is an example to show how lambda form of function works-")

#Function definition is here
sum = lambda arg1,arg2: arg1+arg2
print("sum definition:\n sum = lambda arg1, arg2: arg1+arg2")
#Now you can call sum as a function
print("sum(10,-20):",sum(10,-20))
print("sum(20,20):",sum(20,20))
