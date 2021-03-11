#Renaming and Deleting Files
print("*Renaming and Deleting Files*")
print("""Python os module provides methods that help you perform file-processing operations, such as renaming and deleting files. 
To use this module, you need to import it first and then you can call any related functions. """)
print("\n*The rename() Method*")
print("The rename() method takes two arguments, the current filename and the new filename.")
print("\n*Syntax*")
print("\tos.rename(current_file_name, new_file_name)")

print("\nCreating a dummy file and rename it...")
du = open('dum.txt','w')
du.close()
du = open('dum.txt','r+')
du.write("This is a dummy file")
#du.seek(0,0)
print("du.name:",du.name)
print("\nExample\nos.rename('dum.txt','dummy_file.txt')")
du.close()
#print("du.read():",du.read())
print("\nLook at the *rename.py* file :)")
print("\n*The remove() Method*")
print("""The remove() Method You can use the remove() method to delete files by supplying the name of the file to be deleted as the argument. 
Syntax 
    os.remove(file_name) """)
print("Example\nos.remove('dummy_file.txt')")
print("\nLook at the *remove.py* file")


