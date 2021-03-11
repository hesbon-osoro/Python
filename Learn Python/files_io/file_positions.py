#File Positions
print("*File Positions*")
print("""The tell() method tells you the current position within the file; in other words, the next read or write will occur at that many bytes from the beginning of the file. 
The seek(offset[, from]) method changes the current file position. The offset argument indicates the number of bytes to be moved. The from argument specifies the reference position from where the bytes are to be moved. 
If from is set to 0, the beginning of the file is used as the reference position.  If it is set to 1, the current position is used as the reference position. If it is set to 2 then the end of the file would be taken as the reference position. 
""")
#Open a file
fo = open("test.txt","r+")
#fo.write("""Now is the good time for all good men to come to the end of the party
#Where is party?""")
print("fo.name:",fo.name)
print("fo.mode:",fo.mode)
print("fo.closed:",fo.closed)
print("fo.read():",fo.read())
#Check current position
print("fo.tell():",fo.tell())
print("fo.seek(0,0):",fo.seek(0,0))
print("fo.read(40):",fo.read(40))
print("fo.tell():",fo.tell())
print("fo.seek(0,1):",fo.seek(0,1))
print("fo.read(40):",fo.read(40))
print("fo.tell():",fo.tell())
print("fo.seek(20,0):",fo.seek(20,0))
print("fo.read(40):",fo.read(40))
print("fo.tell():",fo.tell())
print("fo.seek(0,2):",fo.seek(0,2))
print("fo.read(40):",fo.read(40))
print("fo.tell():",fo.tell())
fo.close()