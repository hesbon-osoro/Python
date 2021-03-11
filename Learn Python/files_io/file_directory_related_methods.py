#File & Directory Related Methods
print("* File & Directory Related Methods *")

print("""There are three important sources, which provide a wide range of utility methods to handle and manipulate files & directories on Windows and Unix operating systems. They are as follows- 
    * File Object Methods: The file object provides functions to manipulate files. 
    * OS Object Methods: This provides methods to process files as well as directories. 
File Methods A file object is created using open function and here is a list of functions which can be called on this object""")

#file.close()
"""Close the file. A closed file cannot be read or written any more."""
print("\n*File close() Method*")
print("""Description 
The method close() closes the opened file. A closed file cannot be read or written any more. Any operation, which requires that the file be opened will raise a ValueError after the file has been closed. Calling close() more than once is allowed. 
Python automatically closes a file when the reference object of a file is reassigned to another file. It is a good practice to use the close() method to close a file. 
Syntax 
Following is the syntax for close() method- 
    fileObject.close() 
Parameters 
NA 
Return Value 
This method does not return any value.""")
fo = open("dum.txt",'wb')
print("fo.name:",fo.name)
print("fo.mode:",fo.mode)
fo.close()
print("fo.close() \nfo.closed:",fo.closed)


#file.flush()
"""Flush the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects."""
print("\n*File flush() Method*")
print("""
Description 
The method flush() flushes the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects. 
Python automatically flushes the files when closing them. But you may want to flush the data before closing any file. 
Syntax 
Following is the syntax for flush() method- 
    fileObject.flush() 
Parameters 
NA 
Return Value 
This method does not return any value. """)
fo = open('foo1.txt','r')
print('fo.name:',fo.name)
print("# Here it does nothing, but you can call it with read operation. \nfo.flush()")
# Here it does nothing, but you can call it with read operation.
fo.flush()
fo.close()


#file.fileno()
"""Returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system."""
print("\n*File fileno() Method*")
print("""Description 
The method fileno() returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system. 
Syntax 
Following is the syntax for fileno() method- 
    fileObject.fileno()  
Parameters 
NA 
Return Value 
This method returns the integer file descriptor. """)
fo = open('dum.txt','wb')
f1 = open('foo1.txt','wb')
print("fo.name:",fo.name)
print("fo.fileno():",fo.fileno())
print("f1.name:",f1.name)
print("f1.fileno():",f1.fileno())
fo.close()
f1.close()


#file.isatty()
"""Returns True if the file is connected to a tty(-like) device, else False."""
print("\n*File isatty() Method*")
print("""
Description 
The method isatty() returns True if the file is connected (is associated with a terminal device) to a tty(-like) device, else False. 
 
Syntax Following is the syntax for isatty() method- 
    fileObject.isatty() 
Parameters
 NA 
Return Value 
This method returns true if the file is connected (is associated with a terminal device) to a tty(-like) device, else false.
""")
fo = open('dum.txt','wb')
print("fo.name:",fo.name)
print("fo.isatty():",fo.isatty())
fo.close()

#next(file)
"""Returns the next line from the file each time it is being called."""
print("\n*File next() Method*")
print("""Description
File object in Python 3 does not support next() method. Python 3 has a built-in function next() which retrieves the next item from the iterator by calling its __next__() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised. This method can be used to read the next input line, from the file object. 
Syntax 
Following is the syntax for next() method-
    next(iterator[,default]) 
Parameters 
    *iterator : file object from which lines are to be read  
    *default : returned if iterator exhausted. If not given, StopIteration is raised 
Return Value 
This method returns the next input line. 
""")
fo = open('lan.txt','r+')
print("fo.name:",fo.name)
for i in range(8):
    line = next(fo)
    print("Line[%d]: %s"%(i,line))
fo.close()

#file.read([size])
"""Reads at most size bytes from the file (less if the read hits EOF before obtaining size bytes)."""
print("\n*File read() Method*")
print("""Description 
The method read() reads at most size bytes from the file. If the read hits EOF before obtaining size bytes, then it reads only available bytes. 
Syntax 
Following is the syntax for read() method- 
    fileObject.read( size ); 
Parameters 
    *size - This is the number of bytes to be read from the file. 
Return Value 
This method returns the bytes read in string. """)
fo = open('lan.txt','r+')
print("fo.name:",fo.name)
print("fo.mode:",fo.mode)
print("fo.read(10):",fo.read(10))
fo.close()

#file.readline([size])
"""Reads one entire line from the file. A trailing newline character is kept in the string."""
print("\n*File readline() Method*")
print("""
Description 
The method readline()reads one entire line from the file. A trailing newline character is kept in the string. If the size argument is present and non-negative, it is a maximum byte count including the trailing newline and an incomplete line may be returned. 
An empty string is returned only when EOF is encountered immediately. 
Syntax 
Following is the syntax for readline() method- 
    fileObject.readline( size ); 
Parameters 
    *size - This is the number of bytes to be read from the file. 
Return Value
 This method returns the line read from the file. """)
fo = open('lan.txt','r')
print("fo.name:",fo.name)
print("fo.mode:",fo.mode)
print("fo.readline():",fo.readline())
fo.close()


#file.readlines([sizehint])
"""Reads until EOF using readline() and return a list containing the lines. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read."""
print("\n*File readlines() Method*")
print("""
Description 
The method readlines() reads until EOF using readline() and returns a list containing the lines. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read. 
An empty string is returned only when EOF is encountered immediately. 
Syntax 
Following is the syntax for readlines() method- 
    fileObject.readlines( sizehint ); 
Parameters 
*sizehint - This is the number of bytes to be read from the file. 
Return Value 
This method returns a list containing the lines. 
""")
fo = open('lan.txt','r')
print("fo.name:",fo.name)
print("fo.mode:",fo.mode)
print("fo.readlines(): ",fo.readlines())
fo = open('lan.txt','r')
print("fo.readlines(3):",fo.readlines(3))
fo.close()


#file.seek(offset[, whence])
"""Sets the file's current position"""
print("\n*File seek() Method*")
print("""
Description 
The method seek() sets the file's current position at the offset. The whence argument is optional and defaults to 0, which means absolute file positioning, other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end. 
There is no return value. Note that if the file is opened for appending using either 'a' or 'a+', any seek() operations will be undone at the next write. 
If the file is only opened for writing in append mode using 'a', this method is essentially a no-op, but it remains useful for files opened in append mode with reading enabled (mode 'a+'). 
If the file is opened in text mode using 't', only offsets returned by tell() are legal. Use of other offsets causes undefined behavior. 
Note that not all file objects are seekable. 
Syntax 
Following is the syntax for seek() method- 
    fileObject.seek(offset[, whence]) 
Parameters 
    *offset- This is the position of the read/write pointer within the file.  
    *whence- This is optional and defaults to 0 which means absolute file positioning, other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end. 
Return Value 
This method does not return any value. """)
fo = open('lan.txt','r')
print("fo.name:",fo.name)
print("fo.mode:",fo.mode)
print("fo.readlines(8): ",fo.readlines(8))
print("fo.seek(8,0):",fo.seek(8,0))
print("fo.readlines(3):",fo.readlines(3))
fo.close()


#file.tell()
"""Returns the file's current position"""
print("\n*File tell() Method*")
print("""
Description 
The method tell() returns the current position of the file read/write pointer within the file. 
Syntax 
Following is the syntax for tell() method- 
    fileObject.tell() 
Parameters 
NA 
Return Value 
This method returns the current position of the file read/write pointer within the file.""")
fo = open('lan.txt','r+')
print("fo.name:",fo.name)
print("fo.mode:",fo.mode)
print("fo.tell():",fo.tell())
print("fo.readlines(8): ",fo.readlines(8))
print("fo.seek(8,0):",fo.seek(8,0))
print("fo.tell():",fo.tell())
print("fo.readlines(3):",fo.readlines(3))
fo.close()


#file.truncate([size])
"""Truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size."""
print("\n*File truncate() Method*")
print("""
Description 
The method truncate() truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size. 
The size defaults to the current position. The current file position is not changed. Note that if a specified size exceeds the file's current size, the result is platform-dependent. 
*Note: This method will not work in case the file is opened in read-only mode. 
Syntax 
Following is the syntax for truncate() method- 
    fileObject.truncate( [ size ]) 
Parameters 
    *size - If this optional argument is present, the file is truncated to (at most) that size. 
Return Value 
This method does not return any value.""")
fo = open('lan.txt','r+')
print("fo.name:",fo.name)
print("fo.mode:",fo.mode)
print("fo.readlines(8): ",fo.readlines(8))
print("fo.readlines(8):",fo.readlines(8))
#print("fo.truncate():",fo.truncate())
print("fo.readline():",fo.readline())
#print("fo.truncate():",fo.truncate(20))
print("fo.readlines():",fo.readlines())
print("*When you truncate it cuts down the file affecting the iteration for next(file) function!!!*")
fo.close()

#file.write(str)
"""Writes a string to the file. There is no return value."""
print("\n*File write() Method*")
print("""
Description 
The method write() writes a string str to the file. There is no return value. Due to buffering, the string may not actually show up in the file until the flush() or close() method is called. 
Syntax 
Following is the syntax for write() method- 
    fileObject.write( str ) 
Parameters 
*str - This is the String to be written in the file. 
Return Value 
This method does not return any value. """)
fo = open('Java_.txt','w')
fo.close()
fo = open('Java_.txt','r+')
str = """
       public class Java_{
         public static void main(String[]args){
          System.out.println("Hello, this is Java!")
        }
       }
    """
#fo.write(str)
print("fo.name:",fo.name)
print("fo.mode:",fo.mode)
print("fo.read():",fo.read())
fo.close()
fo = open('Java_.txt','r+')
print("fo.name:",fo.name)
print("fo.read():",fo.read())
fo.close()

#file.writelines(sequence)
"""Writes a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings."""

print("\n*File writelines() Method*")
print("""
Description 
The method writelines() writes a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings. There is no return value. 
Syntax 
Following is the syntax for writelines() method − 
    fileObject.writelines( sequence ) 
Parameters 
    *sequence - This is the Sequence of the strings. 
Return Value 
This method does not return any value.""")
fo = open('lines.txt','w')
fo.close()
fo = open('lines.txt','r+')
lines = ['0123456789\n','abcdefgh\n','!@#$%^&*\n','/*<>?:()\n']
fo.writelines(lines)
print("fo.name:",fo.name)
print("fo.read():",fo.read())
fo.close()

fo = open('lines.txt','r+')
print("fo.name:",fo.name)
print("fo.read():",fo.read())
fo.close()