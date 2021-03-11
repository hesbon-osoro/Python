#Assertions in Python
print('*Assertions in Python*')
print("""An assertion is a sanity-check that you can turn on or turn off when you are done with your testing of the program. 
    * The easiest way to think of an assertion is to liken it to a raise-if statement (or to be more accurate, a raise-if-not statement). An expression is tested, and if the result comes up false, an exception is raised.  
    * Assertions are carried out by the assert statement, the newest keyword to Python, introduced in version 1.5.  
    * Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output. 
""")


#The assert statement
print('*The assert statement*')
print("""When it encounters an assert statement, Python evaluates the accompanying expression, which is hopefully true. If the expression is false, Python raises anAssertionError exception. 
The syntax for assert is − 
    assert Expression[, Arguments] 
If the assertion fails, Python uses ArgumentExpression as the argument for the AssertionError. AssertionError exceptions can be caught and handled like any other exception, using the try-except statement. If they are not handled, they will terminate the program and produce a traceback. 

Example
Here is a function that converts a given temperature from degrees Kelvin to degrees Fahrenheit. Since 0° K is as cold as it gets, the function bails out if it sees a negative temperature − 

""")

#defining the function
def kelvinToFahrenheit(temp):
    assert (temp>=0),"Colder than absolute zero!"
    return ((temp-273)*1.8)+32
print("""def kelvinToFahrenheit(temp):
    assert (temp>=0),"Colder than absolute zero!"
    return ((temp-273)*1.8)+32\n""")
#calling the function
print("kelvinToFahrenheit(0):",kelvinToFahrenheit(0))
print("kelvinToFahrenheit(273):",kelvinToFahrenheit(273))
print("kelvinToFahrenheit(35.2):",kelvinToFahrenheit(35.2))
print("int(kelvinToFahrenheit(35.2)):",int(kelvinToFahrenheit(35.2)))
print("kelvinToFahrenheit(100):")
kelvinToFahrenheit(100)
#print("kelvinToFahrenheit(-2):",kelvinToFahrenheit(-2))
#AssertionError: Colder than absolute zero!