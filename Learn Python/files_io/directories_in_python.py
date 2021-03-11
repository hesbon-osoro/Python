#Directories in Python
print("*Directories in Python*")
print("""All files are contained within various directories, and Python has no problem handling these too. The os module has several methods that help you create, remove, and change directories.""")
print("*The mkdir() Method*")
print("""You can use the mkdir() method of the os module to create directories in the current directory. You need to supply an argument to this method, which contains the name of the directory to be created. 
Syntax 
    os.mkdir("newdir")""")

print("Example")
import os
#Uncomment the next code to create a directory if it doesn't exist
#os.mkdir('test')

print("os.mkdir('test')")
print("\n*The chdir() Method*")
print("""You can use the chdir() method to change the current directory. The chdir() method takes an argument, which is the name of the directory that you want to make the current directory. 
Syntax 
    os.chdir("newdir")""")
print()
print("Current dir os.getcwd():",os.getcwd())
#Changing directory to desktop
os.chdir('C:/Users/user/Desktop/Leshan')
print("os.chdir('C:/Users/user/Desktop/Leshan')")
print("New dir os.getcwd():",os.getcwd())

print("*The getcwd() Method*")
print("""The getcwd() method displays the current working directory. 
Syntax 
    os.getcwd()""")

print("\n*The rmdir() Method*")
print("""The rmdir() method deletes the directory, which is passed as an argument in the method. 
Before removing a directory, all the contents in it should be removed. 
Syntax 
    os.rmdir('dirname') 
\nExample Following is an example to remove the "/tmp/test" directory. It is required to give fully qualified name of the directory, otherwise it would search for that directory in the current directory.""")

print("\nLook at the rem_dir.py file :)")