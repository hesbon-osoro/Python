#Opening and Closing Files
print("*Opening and Closing Files*")
print("""Until now, you have been reading and writing to the standard input and output. Now, we will see how to use actual data files. 
Python provides basic functions and methods necessary to manipulate files by default. You can do most of the file manipulation using a file object. """)
print("*The open Function*")
print("""Before you can read or write a file, you have to open it using Python's built-in open() function. This function creates a file object, which would be utilized to call other support methods associated with it. 
Syntax 
    file object = open(file_name [, access_mode][, buffering]) 
Here are parameter details- """)
print("* file_name: The file_name argument is a string value that contains the name of the file that you want to access. ")
print("* access_mode: The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc. A complete list of possible values is given below in the table. This is an optional parameter and the default file access mode is read (r). ")
print("* buffering: If the buffering value is set to 0, no buffering takes place. If the buffering value is 1, line buffering is performed while accessing a file. If you specify the buffering value as an integer greater than 1, then buffering action is performed with the indicated buffer size. If negative, the buffer size is the system default (default behavior).")
print("\nHere is a list of the different modes of opening a file- ")
print("*Modes\tDescription*")
print("r\tOpens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode. ")
print("rb\tOpens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.")
print("r+\tOpens a file for both reading and writing. The file pointer placed at the beginning of the file.")
print("rb+\tOpens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file. ")
print("w\tOpens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. ")
print("wb\tOpens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. ")
print("w+\tOpens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.")
print("wb+\tOpens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.")
print("a\tOpens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing. ")
print("ab\tOpens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.")
print("a+\tOpens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing. ")
print("ab+\tOpens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing. ")

print("\n*The file Object Attributes*")
print("""Once a file is opened and you have one file object, you can get various information related to that file. 
Here is a list of all the attributes related to a file object- """)
print("*Attribute\t\tDescription*")
print("file.closed\t\tReturns true if file is closed, false otherwise. ")
print("file.mode \t\tReturns access mode with which file was opened. ")
print("file.name \t\tReturns name of the file. ")
print("\n*Note:* softspace attribute is not supported in Python 3.x")
print("Example")
#Opening a file
fo = open('foo.txt','wb')
print("fo  = open('foo.txt','wb')")
print("fo.name:",fo.name)
print('fo.mode:',fo.mode)
print('fo.mode:',fo.closed)
fo.close()
print('fo.close()')
print('fo.closed:',fo.closed)
print("*The close() Method*")
print("""The close() method of a file object flushes any unwritten information and closes the file object, after which no more writing can be done. 
Python automatically closes a file when the reference object of a file is reassigned to another file. It is a good practice to use the close() method to close a file. 
Syntax 
    fileObject.close();""")

print("*Reading and Writing Files *")
print("The file object provides a set of access methods to make our lives easier. We would see how to use read() and write() methods to read and write files. ")
print("*The write() Method*")
print("""The write() method writes any string to an open file. It is important to note that Python strings can have binary data and not just text. 
The write() method does not add a newline character ('\\n') to the end of the string- 
Syntax 
    fileObject.write(string); 
Here, passed parameter is the content to be written into the opened file. """)

print("Example")
fo = open('foo1.txt','w')
fo.write("Python is a great language.\nYeah its great!!\n")
#Close opened file
fo.close()
print("""fo = open('foo1.txt','w')
fo.write("Python is a great language.\\nYeah its great!!\\n")
#Close opened file
fo.close()
""")
print("""The above method would create foo.txt file and would write given content in that file and finally it would close that file. If you would open this file, it would have the following content- 
    Python is a great language. 
    Yeah its great!!""")
print("\n*The read() Method*")
print("""The read() method reads a string from an open file. It is important to note that Python strings can have binary data apart from the text data. 
Syntax 
    fileObject.read([count]); 
Here, passed parameter is the number of bytes to be read from the opened file. This method starts reading from the beginning of the file and if count is missing, then it tries to read as much as possible, maybe until the end of file""")
print("Example")
fo = open('foo1.txt','r+')
#str = fo.read()
print("fo = open('foo1.txt','r+')")
print('fo.read():',fo.read())
fo = open('foo1.txt','r+')
print("fo = open('foo1.txt','r+')")
print('fo.read(20):',fo.read(20))
fo.close()