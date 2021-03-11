#Scope of Variables
print("***Scope of Variables***")
print("""All variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable. 
The scope of a variable determines the portion of the program where you can access a particular identifier. There are two basic scopes of variables in Python-""")
print("*Global Variables*")
print("*Local Variables*")
print()
print("*Global vs Local variables*")
print("""Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.
This means that local variables can be accessed only inside the function in which they are declared, whereas global variables can be accessed throughout the program body by all functions. When you call a function, the variables declared inside it are brought into scope. Following is a simple example- """)

total = 0 #This is a global variable
#Function definition is here
def sum(arg1, arg2):
    "Add both the parameters and return them"
    total = arg1+arg2; #Here total is local variable
    print("Inside the function local total :",total)
    return total
#Now you can call sum function
print("sum(10,20)")
sum(10,20)
print("Outside the function global total :",total)

