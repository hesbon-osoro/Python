#The Return Statement
print("""The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None. 
All the examples given above are not returning any value. You can return a value from a function as follows- """)

#Function definition is here
def sum(arg1,arg2):
    "Add both the parameters and return them."
    total = arg1+arg2
    print("Inside the function :",total)
    return total
#Now you can call sum function
total = sum(10,20)
print("total = sum(10,20)")
print("Outside the function, total: ",total)