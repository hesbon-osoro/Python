#Files I/O
print("***FILES I/O***")
print("This chapter covers all the basic I/O functions available in Python 3. For more functions, please refer to the standard Python documentation. ")
print("\n*Printing to the Screen*")
print("""The simplest way to produce output is using the print statement where you can pass zero or more expressions separated by commas. This function converts the expressions you pass into a string and writes the result to standard output as follows- 
#!/usr/bin/python3 
print ("Python is really a great language,", "isn't it?") """)
print ("Python is really a great language,", "isn't it?")
print("\n*Reading Keyboard Input*")
print("""Python 2 has two built-in functions to read data from standard input, which by default comes from the keyboard. These functions are input() and raw_input() 
In Python 3, raw_input() function is deprecated. Moreover, input() functions read data from keyboard as string, irrespective of whether it is enclosed with quotes ('' or "" ) or not.""")
print("\n*The input Function*")
print("The *input([prompt])* function is equivalent to raw_input, except that it assumes that the input is a valid Python expression and returns the evaluated result to you. ")
x = input('something:') #entered data treated as string with or without ''
print('something:',x)