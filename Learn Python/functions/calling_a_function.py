#Calling a function

print("*Calling a Function*")
print("""Defining a function gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code. 
Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt. Following is an example to call the printme() function- """)

#Function definition is here
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return

#Now you can call printme function
printme("This is first call to the user defined function!")
printme("Again second call to the same function")
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   print ("Values inside the function before change: ", mylist)
   mylist[2]=50
   print ("Values inside the function after change: ", mylist)

   return
   # Now you can call changeme function


mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)
print("\nThere is one more example where argument is being passed by reference and the reference is being overwritten inside the called function. ")

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4] # This would assi new reference in mylist
   print ("Values inside the function: ", mylist)
   return
print("""The parameter mylist is local to the function changeme. Changing mylist within the function does not affect mylist. The function accomplishes nothing and finally this would produce the following result- """)
# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
