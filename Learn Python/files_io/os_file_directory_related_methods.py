#OS File/Directory Methods
import os, sys, time, stat
print("*OS File/Directory Methods *")
print("The os module provides a big range of useful methods to manipulate files and directories. Most of the useful methods are listed here: ")
#os.access(path, mode)
"""Use the real uid/gid to test for access to path."""
print("\n*os.access() Method*")
print("""
Description 
The method access() uses the real uid/gid to test for access to path. Most operations will use the effective uid/gid, therefore this routine can be used in a suid/sgid environment to test if the invoking user has the specified access to path.It returns True if access is allowed, False if not. 
Syntax 
Following is the syntax for access() method- 
    os.access(path, mode) 
Parameters 
    *path - This is the path which would be tested for existence or any access.  
    *mode - This should be F_OK to test the existence of path, or it can be the inclusive OR of one or more of R_OK, W_OK, and X_OK to test permissions.  
        -> os.F_OK: Value to pass as the mode parameter of access() to test the existence of path.  
        -> os.R_OK: Value to include in the mode parameter of access() to test the readability of path.  
        -> os.W_OK: Value to include in the mode parameter of access() to test the writability of path.  
        -> os.X_OK: Value to include in the mode parameter of access() to determine if path can be executed. 
Return Value 
This method returns True if access is allowed, False if not. 
""")
print("Example")
#test for existence of path
#let = os.access('test/foo.txt',os.F_OK)
print("os.access('test/foo.txt',os.F_OK):",os.access('test/foo.txt',os.F_OK))
print("os.access('foo.txt',os.F_OK):",os.access('foo.txt',os.F_OK))
print("os.access('foo.txt',os.R_OK):",os.access('foo.txt',os.R_OK))
print("os.access('foo.txt',os.W_OK):",os.access('foo.txt',os.W_OK))
print("os.access('foo.txt',os.X_OK):",os.access('foo.txt',os.X_OK))


#os.chdir(path)
"""Change the current working directory to path"""
print("\n*os.chdir() Method*")
print("""
Description 
The method chdir() changes the current working directory to the given path.It returns None in all the cases. 
Syntax 
Following is the syntax for chdir() method- 
    os.chdir(path) 
Parameters 
    *path - This is complete path of the directory to be changed to a new location. 
Return Value 
This method does not return any value. It throws FileNotFoundError if the specified path is not found. """)
print("os.getcwd():",os.getcwd())
print("os.chdir('test'):",os.chdir('test'))
print("os.getcwd():",os.getcwd())
print("os.chdir('E:/Hesbon/#code/Python/Learn Python/files_io')",os.chdir('E:/Hesbon/#code/Python/Learn Python/files_io'))
print("os.getcwd():",os.getcwd())

#os.chflags(path, flags)
"""Set the flags of path to the numeric flags."""
print("\n*os.chflags() Method*")
print("""
Description 
The method chflags() sets the flags of path to the numeric flags. The flags may take a combination (bitwise OR) of the various values described below. 
*Note: This method is available Python version 2.6 onwards. Most of the flags can be changed by super-user only. 
Syntax 
Following is the syntax for chflags() method- 
    os.chflags(path, flags) 
Parameters 
    *path - This is a complete path of the directory to be changed to a new location.  
    *flags - The flags specified are formed by OR'ing the following values-  
        -> os.UF_NODUMP: Do not dump the file.
        -> os.UF_IMMUTABLE: The file may not be changed. 
        -> os.UF_APPEND: The file may only be appended to. 
        -> os.UF_NOUNLINK: The file may not be renamed or deleted. 
        -> os.UF_OPAQUE: The directory is opaque when viewed through a union stack. 
        -> os.SF_ARCHIVED: The file may be archived. 
        -> os.SF_IMMUTABLE: The file may not be changed. 
        -> os.SF_APPEND: The file may only be appended to. 
        -> os.SF_NOUNLINK: The file may not be renamed or deleted. 
        -> os.SF_SNAPSHOT: The file is a snapshot file. 
Return Value 
This method does not return any value.
""")
#print("Example")
#set file to be archived
#print(":",os.chflags('foo.txt',os.ARCHIVED))
#AttributeError: module 'os' has no attribute 'chflags'

#os.chmod(path, mode)
"""Change the mode of path to the numeric mode."""
print("\n*os.chmod() Method*")
print("""
Description The method chmod() changes the mode of path to the passed numeric mode. The mode may take one of the following values or bitwise ORed combinations of them- 
    * stat.S_ISUID: Set user ID on execution.  
    * stat.S_ISGID: Set group ID on execution.  
    * stat.S_ENFMT: Record locking enforced.  
    * stat.S_ISVTX: Save text image after execution.  
    * stat.S_IREAD: Read by owner.  
    * stat.S_IWRITE: Write by owner.  
    * stat.S_IEXEC: Execute by owner.  
    * stat.S_IRWXU: Read, write, and execute by owner.  
    * stat.S_IRUSR: Read by owner.  
    * stat.S_IWUSR: Write by owner.  
    * stat.S_IXUSR: Execute by owner.  
    * stat.S_IRWXG: Read, write, and execute by group.  
    * stat.S_IRGRP: Read by group.  
    * stat.S_IWGRP: Write by group. 
    * stat.S_IXGRP: Execute by group.  
    * stat.S_IRWXO: Read, write, and execute by others.  
    * stat.S_IROTH: Read by others.  
    * stat.S_IWOTH: Write by others.  
    * stat.S_IXOTH: Execute by others. 
Syntax 
Following is the syntax for chmod() method- 
    os.chmod(path, mode) 
Parameters 
    * path - This is the path for which mode would be set.  
    * mode - This may take one of the above mentioned values or bitwise ORed combinations of them. 
Return Value 
This method does not return any value. 
*Note : Although Windows supports chmod(), you can only set the file’s read-only flag with it (via the stat.S_IWRITE and stat.S_IREAD constants or a corresponding integer value). All other bits are ignored. """)
import stat
print("Example")
#set file execute by the group
print("os.chmod('foo.txt',stat.S_IXGRP):",os.chmod('foo.txt',stat.S_IXGRP))
#set a file write by others
print("os.chmod('foo.txt',stat.S_IWOTH):",os.chmod('foo.txt',stat.S_IWOTH))

#os.chown(path, uid, gid)
"""Change the owner and group id of path to the numeric uid and gid."""
print("\n*os.chown() Method*")
print("""
Description 
The method chown() changes the owner and group id of path to the numeric uid and gid. To leave one of the ids unchanged, set it to -1.To set ownership, you would need super user privilege.. 
Syntax 
Following is the syntax for chown() method- 
    os.chown(path, uid, gid) 
Parameters 
    * path - This is the path for which owner id and group id need to be setup.  
    * uid - This is Owner ID to be set for the file.  
    * gid - This is Group ID to be set for the file. 
Return Value 
This method does not return any value. 
""")
#print("Example")
#print("",os.chown('foo1.txt',100,-1))
#AttributeError: module 'os' has no attribute 'chown'

#os.chroot(path)
"""Change the root directory of the current process to path."""
print("\n*os.chroot() Method*")
print("""
Description 
The method chroot() changes the root directory of the current process to the given path. Available on Unix like systems only. To use this method, you would need super user privilege. 
Syntax 
Following is the syntax for chroot() method- 
    os.chroot(path) 
Parameters 
    * path - This is the path which would be set as root for the current process. 
Return Value 
This method does not return any value. 
""")
#print("Example")
#print("os.chroot(test):",os.chroot(test))
#AttributeError: module 'os' has no attribute 'chroot'

#os.close(fd)
"""Close file descriptor fd."""
print("\n*Python os.close() Method*")
print("""
Description 
The method close() closes the associated with file descriptor fd. 
Syntax Following is the syntax for close() method- 
    os.close(fd) 
Parameters 
    fd - This is the file descriptor of the file. 
Return Value This method does not return any value. 
*Note: This function is intended for low-level I/O and must be applied to a file descriptor as returned by os.open() or pipe().
""")
print("Example")
#open a file
fd = os.open('foo2.txt',os.O_RDWR|os.O_CREAT)
#write one string
line = "this is a test string"
#string needs to be converted to byte object
#b = str.encode(line)
#os.write(fd,b)
print("os.read(fd,os.read(fd,os.O_RDWR|os.O_CREAT)):",os.read(fd,os.O_RDWR|os.O_CREAT))
#close opened file
os.close(fd)
print("view source code:)")
#os.closerange(fd_low, fd_high)
"""Close all file descriptors from fd_low (inclusive) to fd_high (exclusive), ignoring errors."""
print('\n*os.closerange() Method*')
print("""
Description 
The method closerange() closes all file descriptors from fd_low (inclusive) to fd_high (exclusive), ignoring errors.This method is introduced in Python version 2.6. 
Syntax Following is the syntax for closerange() method- 
    os.closerange(fd_low, fd_high) 
Parameters
    * fd_low - This is the Lowest file descriptor to be closed.  
    * fd_high - This is the Highest file descriptor to be closed. 
This function is equivalent to- 
for fd in xrange(fd_low, fd_high): 
    try: 
        os.close(fd) 
    except OSError: 
        pass 
        
Return Value 
This method does not return any value. 
""")
print("Example")
#Lets open several files then close them in one closerange function
f1 = os.open('lan.txt',os.O_CREAT)
f2 = os.open('foo2.txt',os.O_CREAT)
print("os.read(f1,os.O_CREAT):",os.read(f1,os.O_CREAT),"\nos.read(f2,os.O_CREAT):",os.read(f2,os.O_CREAT))

os.closerange(f1,f2)
#os.dup(fd)
"""Return a duplicate of file descriptor fd."""
print('\n*os.dup() Method*')
print("""
Description 
The method dup() returns a duplicate of file descriptor fd which can be used in place of original descriptor. 
Syntax 
Following is the syntax for dup() method- 
    os.dup(fd) 
Parameters 
    fd - This is the original file descriptor. 
Return Value 
This method returns a duplicate of file descriptor. 
""")
print("Example")
#Open a file
fd = os.open('foo2.txt',os.O_RDWR|os.O_CREAT)
#Get one duplicate file descriptor
d_fd = os.dup(fd)
#write one string usig duplicate fd
line = 'sample for duplicate string'
#b = os.write(d_fd,str.encode(line))
print("os.read(d_fd,os.O_CREAT):",os.read(d_fd,os.O_CREAT))
os.closerange(fd,d_fd)



#os.dup2(fd, fd2)
"""Duplicate file descriptor fd to fd2, closing the latter first if necessary."""
print('\n*os.dup2() Method*')
print("""
Description 
The method dup2() duplicates file descriptor fd to fd2, closing the latter first if necessary. 
*Note: New file description would be assigned only when it is available. In the following example given below, 1000 would be assigned as a duplicate fd in case when 1000 is available. 
Syntax 
Following is the syntax for dup2() method- 
    os.dup2(fd, fd2) 
Parameters 
    * fd - This is File descriptor to be duplicated.  
    * fd2 - This is Duplicate file descriptor. 
Return Value 
This method returns a duplicate of file descriptor. 
""")
print("Example")
#Open a file
fd = os.open('foo2.txt',os.O_RDWR|os.O_CREAT)
#write one string using duplicate fd
line = 'string for dup2() method'
#os.write(fd,str.encode(line))
#now duplicate this file descriptor as 1000
fd2 = 1000
os.dup2(fd,fd2);
#now read this file from the beginning using fd2
os.lseek(fd2,0,0)
line = os.read(fd2,100)
print("line:",line)
print("line.decode():",line.decode())
#close opened file
os.closerange(fd,fd2)
print("view source code :)")


#os.fchdir(fd)
"""Change the current working directory to the directory represented by the file descriptor fd."""
print('\n*os.fchdir() Method*')
print("""
Description 
The method fchdir() change the current working directory to the directory represented by the file descriptor fd. The descriptor must refer to an opened directory, not an open file. 
Syntax 
Following is the syntax for fchdir() method- 
    os.fchdir(fd) 
Parameters 
    fd - This is Directory descriptor. 
Return Value 
This method does not return any value. 
""")
#print("Example")
#print("os.getcwd():",os.getcwd())
#print("os.fchdir('test'):",os.fchdir('test'))
#print("os.getcwd():",os.getcwd())
#AttributeError: module 'os' has no attribute 'fchdir'

#os.fchmod(fd, mode)
"""Change the mode of the file given by fd to the numeric mode."""
print('\n*os.fchmod() Method*')
print("""
Description The method fchmod() changes the mode of the file given by fd to the numeric mode. The mode may take one of the following values or bitwise ORed combinations of them- 
*Note: This method is available Python 2.6 onwards. 
    * stat.S_ISUID: Set user ID on execution.  
    * stat.S_ISGID: Set group ID on execution.  
    * stat.S_ENFMT: Record locking enforced. 
    * stat.S_ISVTX: Save text image after execution.  
    * stat.S_IREAD: Read by owner.  
    * stat.S_IWRITE: Write by owner.  
    * stat.S_IEXEC: Execute by owner.  
    * stat.S_IRWXU: Read, write, and execute by owner.  
    * stat.S_IRUSR: Read by owner.  
    * stat.S_IWUSR: Write by owner.  
    * stat.S_IXUSR: Execute by owner.  
    * stat.S_IRWXG: Read, write, and execute by group.  
    * stat.S_IRGRP: Read by group.  
    * stat.S_IWGRP: Write by group.  
    * stat.S_IXGRP: Execute by group.  
    * stat.S_IRWXO: Read, write, and execute by others.  
    * stat.S_IROTH: Read by others.  
    * stat.S_IWOTH: Write by others.  
    * stat.S_IXOTH: Execute by others. 
Syntax 
Following is the syntax for fchmod() method- 
    os.fchmod(fd, mode) 
Parameters 
    * fd - This is the file descriptor for which mode would be set.  
    * mode - This may take one of the above mentioned values or bitwise ORed combinations of them. 
Return Value 
This method does not return any value. Available on Unix like operating systems only. 
""")
#print('Example')
#open file
#fd = os.open('foo2.txt',os.O_RDONLY)
#set file to execute by the group
#os.fchmod(fd,stat.S_IXGRP)
#set a file to write by others
#os.fchmod(fd,stat.S_IWOTH)
#print("Changes applied successfully!!")
#os.close(fd)
#AttributeError: module 'os' has no attribute 'fchmod'


#os.fchown(fd, uid, gid)
"""Change the owner and group id of the file given by fd to the numeric uid and gid."""
print('\n*os.fchown() Method *')
print("""
Description 
The method fchown() changes the owner and group id of the file given by fd to the numeric uid and gid. To leave one of tche ids unchanged, set it to -1. 
*Note:This method is available Python 2.6 onwards. 
Syntax 
Following is the syntax for fchown() method- 
    os.fchown(fd, uid, gid) 
Parameters 
    * fd - This is the file descriptor for which owner id and group id need to be set up.  
    * uid - This is Owner ID to be set for the file.
    * gid - This is Group ID to be set for the file. 
Return Value 
This method does not return any value. Available in Unix like operating systems only. 
""")
#print('Example')
#fd = os.open('foo2.txt',os.O_RDONLY)
#set the user id to 100 for this file
#os.fchown(fd,100,-1)
#set the group id to 50 for this file
#os.fchown(fd,-1,50)
#print("Changed ownership successfully!!!")
#os.close(fd)
#AttributeError: module 'os' has no attribute 'fchown'


#os.fdatasync(fd)
"""Force write of file with filedescriptor fd to disk."""
print('\n*os.fdatasync() Method*')
print("""
Description 
The method fdatasync() forces write of file with filedescriptor fd to disk. This does not force update of metadata. If you want to flush your buffer then you can use this method. 
Syntax Following is the syntax for fdatasync() method- 
    os.fdatasync(fd) 
Parameters 
  fd - This is the file descriptor for which data to be written.
Return Value 
This method does not return any value.
""")
#print('Example')
#fd = os.open('foo2.txt',os.O_RDWR|os.O_CREAT)
#you can write into thw file
#now you can use fdatasync() method
#Infact here you would not br able to see its effect
#os.fdatasync(fd)
#now read the file from beginning
#os.lseek(fd,0,0)
#str = os.read(fd,100)
#line = os.read(fd2,100)
#str = line.decode()
#print("line:",line)
#os.close(fd)
#AttributeError: module 'os' has no attribute 'fdatasync'


#os.fdopen(fd[, mode[, bufsize]])
""""Return an open file object connected to the file descriptor fd."""
print('\n*os.fdopen() Method*')
print("""
Description 
The method fdopen() returns an open file object connected to the file descriptor fd. Then you can perform all the defined functions on file object. 
Syntax 
Following is the syntax for fdopen() method- 
    os.fdopen(fd, [, mode[, bufsize]]); 
Parameters 
    * fd - This is the file descriptor for which a file object is to be returned.  
    * mode - This optional argument is a string indicating how the file is to be opened. The most commonly-used values of mode are 'r' for reading, 'w' for writing (truncating the file if it already exists), and 'a' for appending.  
    * bufsize - This optional argument specifies the file's desired buffer size: 0 means unbuffered, 1 means line buffered, any other positive value means use a buffer of (approximately) that size. 
Return Value 
    This method returns an open file object connected to the file descriptor. 
""")
print('Example')
#open a file
fd = os.open('foo3.txt',os.O_RDWR|os.O_CREAT)
#now get s file object for the above file
fo = os.fdopen(fd,'w+')
#tell the current position
print('fo.tell():',fo.tell())
#write one string
#fo.write('Python is a great language.\nIndeed!!!!')
#now read this file from the beginning
os.lseek(fd,0,0)
str = os.read(fd,100)
print(str)
#tell the current position
print("fo.tell():",fo.tell())
#close opened file
fo.close()
print('view source code :)')

#os.fpathconf(fd, name)
"""Return system configuration information relevant to an open file. name specifies the configuration value to retrieve."""
print('\n*os.fpathconf() Method*')
print("""
Description 
The method fpathconf() returns system configuration information relevant to an open file.This variable is very similar to unix system call fpathconf() and accept the similar arguments. 
Syntax 
Following is the syntax for fpathconf() method- 
    os.fpathconf(fd, name) 
Parameters 
    * fd - This is the file descriptor for which system configuration information is to be returned.  
    * name - This specifies the configuration value to retrieve; it may be a string, which is the name of a defined system value; these names are specified in a number of standards (POSIX.1, Unix 95, Unix 98, and others). The names known to the host operating system are given in the os.pathconf_names dictionary. 
Return Value 
This method returns system configuration information relevant to an open file. 
""")
#print('Example')
#open a file
#fd = os.open('foo3.txt',os.O_RDWR|os.O_CREAT)
#print("os.pathconf_names:",os.pathconf_names)
#now get the maximum number of links to the file
#print("os.fpathconf(fd,'PC_LINK_MAX'):",os.fpathconf(fd,'PC_LINK_MAX'))
#now get maximum length of a filename
#print("os.fpathconf(fd,'PC_NAME_MAX'):",os.fpathconf(fd,'PC_NAME_MAX'))
#close opened file
#os.close(fd)




#os.fstat(fd)
"""Return status for file descriptor fd, like stat()."""
print('\n*os.fstat() Method*')
print("""
Description 
The method fstat() returns information about a file associated with the fd. Here is the structure returned by fstat method- 
    * st_dev: ID of device containing file  
    * st_ino: inode number  
    * st_mode: protection  
    * st_nlink: number of hard links  
    * st_uid: user ID of owner  
    * st_gid: group ID of owner  
    * st_rdev: device ID (if special file)  
    * st_size: total size, in bytes  
    * st_blksize: blocksize for filesystem I/O  
    * st_blocks: number of blocks allocated  
    * st_atime: time of last access  
    * st_mtime: time of last modification  
    * st_ctime: time of last status change 
Syntax 
Following is the syntax for fstat() method- 
    os.fstat(fd) 
Parameters 
  fd - This is the file descriptor for which system information is to be returned. 
Return Value 
This method returns information about a file associated with the fd. 
""")
print('Example')
#open a file
fd = os.open('foo3.txt',os.O_RDWR|os.O_CREAT)
#now get the tuple
print("os.fstat(fd):",os.fstat(fd))
#now get the uid of the file
print("os.fstat(fd).st_uid:",os.fstat(fd).st_uid)
#now get the gid of the file
print("os.fstat(fd).st_gid:",os.fstat(fd).st_gid)
print("Last access time")
print("time.asctime(time.localtime(os.fstat(fd).st_atime)):",time.asctime(time.localtime(os.fstat(fd).st_atime)))
print("last modification time")
print("time.asctime(time.localtime(os.fstat(fd).st_mtime)):",time.asctime(time.localtime(os.fstat(fd).st_mtime)))
print("Last status change time")
print("time.asctime(time.localtime(os.fstat(fd).st_ctime)):",time.asctime(time.localtime(os.fstat(fd).st_ctime)))

#close the opened file
os.close(fd)


#os.fstatvfs(fd)
"""Return information about the filesystem containing the file associated with file descriptor fd, like statvfs()."""
print('\n*os.fstatvfs() Method*')
print("""
Description The method fstatvfs() returns information about the file system containing the file associated with file descriptor fd. This returns the following structure- 
    * f_bsize: file system block size  
    * f_frsize: fragment size  
    * f_blocks: size of fs in f_frsize units  
    * f_bfree: free blocks  
    * f_bavail: free blocks for non-root  
    * f_files: inodes 
    * f_ffree: free inodes  
    * f_favail: free inodes for non-root  
    * f_fsid: file system ID  
    * f_flag: mount flags  
    * f_namemax: maximum filename length 
Syntax 
Following is the syntax for fstatvfs() method- 
os.fstatvfs(fd)  
Parameters 
fd - This is the file descriptor for which system information is to be returned. 
Return Value 
This method returns information about the file system containing the file associated.
""")
#print("Example")
#open a file
#fd = os.open('foo3.txt',os.O_RDWR|os.O_CREAT)
#now get the tuple
#info = os.fstatvfs(fd)
#print("os.fstatvfs(fd):",os.fstatvfs(fd))
#now get maximum filename length
#print("info.f_namemax:",info.f_namemax)
#new get free blocks
#print("Free blocks: %d"%info.f_bfree)

#close opened file
#os.close(fd)
#AttributeError: module 'os' has no attribute 'fstatvfs'


#os.fsync(fd)
"""Force write of file with filedescriptor fd to disk."""
print("\n*os.fsync() Method*")
print("""
Description 
The method fsync() forces write of file with file descriptor fd to disk. If you're starting with a Python file object f, first do f.flush(), and then do os.fsync(f.fileno()), to ensure that all internal buffers associated with f are written to disk. 
Syntax 
Following is the syntax for fsync() method- 
    os.fsync(fd) 
Parameters 
    fd - This is the file descriptor for buffer sync is required. 
Return Value 
This method does not return any value. 
""")
print("Example")
#open a file
fd = os.open('foo4.txt',os.O_RDWR|os.O_CREAT)
#write one string
line = 'lets have a taste for other methods working with files...'
b = line.encode()
#os.write(fd,b)
#now you can use fsync() method
#infact here you will not be able to see its effect
os.fsync(fd)
#now read this file from beginning
os.lseek(fd,0,0)
line = os.read(fd,100)
b = line.decode()
print("File content: ",b)
#clodse opened file
os.close(fd)


#os.ftruncate(fd, length)
"""Truncate the file corresponding to file descriptor fd, so that it is at most length bytes in size."""
print('\n*os.ftruncate() Method*')
print("""
Description 
The method ftruncate() truncates the file corresponding to file descriptor fd, so that it is at most length bytes in size. 
Syntax 
Following is the syntax for ftruncate() method- 
    os.ftruncate(fd, length) 
Parameters 
    * fd - This is the file descriptor, which needs to be truncated.  
    * length - This is the length of the file where file needs to be truncated. 
Return Value 
This method does not return any value. Available on Unix like systems. 
""")
print("Example")
#open a file
fd = os.open('foo4.txt',os.O_RDWR|os.O_CREAT)
#write one string
line = 'lets have a taste for other methods working with files...'
b = line.encode()
#os.write(fd,b)
#now you can use ftruncate() method
os.ftruncate(fd,15)
#now read this file from beginning
os.lseek(fd,0,0)
line = os.read(fd,100)
b = line.decode()
print("File content: ",b)
#clodse opened file
os.close(fd)


#os.getcwd()
"""Return a string representing the current working directory."""
print('\n*os.getcwd() Method*')
print("""
Description 
The method getcwd() returns current working directory of a process. 
Syntax 
Following is the syntax for getcwd() method- 
    os.ggetcwd(path) 
Parameters 
NA 
Return Value 
This method returns the current working directory of a process. 
""")
print('Example')
print('os.getcwd():',os.getcwd())



#os.getcwdu()
"""Return a Unicode object representing the current working directory."""
print('\n*os.getcwdu() Method*')
print("""
Description 
The method getcwdu() returns a unicode object representing the current working directory. 
Syntax Following is the syntax for getcwdu() method- 
    os.getcwdu()
Parameters 
NA 
Return Value 
This method returns a unicode object representing the current working directory. 
""")
#print('Example')
#print("os.getcwdu():",os.getcwdu())
#AttributeError: module 'os' has no attribute 'getcwdu'


#os.isatty(fd)
"""Return True if the file descriptor fd is open and connected to a tty(-like) device, else False."""
print('\n*os.isatty() Method*')
print("""
Description 
The method isatty()returns True if the file descriptor fd is open and connected to a tty(- like) device, else False. 
Syntax Following is the syntax for isatty() method- 
    os.isatty( fd ) 
Parameters
 fd - This is the file descriptor for which association needs to be checked. 
Return Value 
This method returns True if the file descriptor fd is open and connected to a tty(-like) device, else False.
""")
print('Example')
#open a file
fd = os.open('foo4.txt',os.O_CREAT|os.O_RDWR)
print("os.isatty(fd):",os.isatty(fd))
os.close(fd)

#os.lchflags(path, flags)
"""Set the flags of path to the numeric flags, like chflags(), but do not follow symbolic links."""
print('\n*os.lchflags() Method*')
print("""
Description 
The method lchflags() sets the flags of path to the numeric flags. This method does not follow symbolic links unlike chflags() method. As of Python 3.3, this is equivalent to os.chflags(path, flags, follow_symlinks=False). 
Here, flags may take a combination (bitwise OR) of the following values (as defined in the stat module): 
    * UF_NODUMP: Do not dump the file.  
    * UF_IMMUTABLE: The file may not be changed.  
    * UF_APPEND: The file may only be appended to.  
    * UF_NOUNLINK: The file may not be renamed or deleted.  
    * UF_OPAQUE: The directory is opaque when viewed through a union stack.  
    * SF_ARCHIVED: The file may be archived.  
    * SF_IMMUTABLE: The file may not be changed.  
    * SF_APPEND: The file may only be appended to.  
    * SF_NOUNLINK: The file may not be renamed or deleted.  
    * SF_SNAPSHOT: The file is a snapshot file. 
*Note: This method has been introduced in Python 2.6 
Syntax 
Following is the syntax for lchflags() method- 
    os.lchflags(path, flags) 
Parameters 
    * path - This is the file path for which flags to be set.  
    * flags - This could be a combination (bitwise OR) of the above defined flags values. 
Return Value 
This method does not return any value. Available on Unix like systems. 
""")
#print('Example')
#open a file
#fd = os.open('foo4.txt',os.O_RDWR|os.O_CREAT)
#close the file
#os.close(fd)
#now change the file flag
#print("os.lchflags('foo4.txt',os.SF_ARCHIVED):",os.lchflags('foo4.txt',os.SF_ARCHIVED))
#AttributeError: module 'os' has no attribute 'lchflags'

#os.lchmod(path, mode)
""""Change the mode of path to the numeric mode."""



#os.lchown(path, uid, gid)
"""Change the owner and group id of path to the numeric uid and gid. This function will not follow symbolic links."""
print('\n*os.lchown() Method*')
print("""
Description 
The method lchown() changes the owner and group id of path to the numeric uid and gid. This function will not follow symbolic links. To leave one of the ids unchanged, set it to - 1. As of Python 3.3, this is equivalent to os.chown(path, uid, gid, follow_symlinks=False). 
Syntax 
Following is the syntax for lchown() method- 
    os.lchown(path, uid, gid) 
Parameters 
    * path - This is the file path for which ownership to be set.  
    * uid - This is the Owner ID to be set for the file.  
    * gid - This is the Group ID to be set for the file. 
Return Value 
This method does not return any value. 
""")
#print('Example')
#open a file
#fd = os.open('foo4.txt',os.O_RDWR|os.O_CREAT)
#close the file
#os.close(fd)
# Now change the file ownership.
# Set a file owner ID
#print("os.lchown( path, 500, -1):",os.lchown( 'foo4.txt', 500, -1))
# Set a file group ID
#print("os.lchown( path, -1, 500):",os.lchown( 'foo4.txt', -1, 500))
#print ("Changed ownership successfully!!")
#AttributeError: module 'os' has no attribute 'lchown'



#os.link(src, dst)
"""Create a hard link pointing to src named dst."""
print('\n*os.link() Method *')
print("""
Description 
The method link() creates a hard link pointing to src named dst. This method is very useful to create a copy of existing file. 
Syntax 
Following is the syntax for link() method- 
    os.link(src, dst) 
  
Parameters 
    * src - This is the source file path for which hard link would be created.  
    * dest - This is the target file path where hard link would be created. 
Return Value 
This method does not return any value. Available on Unix, Windows. 
""")
print('Example')
#open a file
path = 'foo4.txt'
fd = os.open(path,os.O_RDWR|os.O_CREAT)
#close the file
os.close(fd)
dst = 'test/foo4.txt'
print("path = 'foo4.txt'")
print("dst = 'test/foo4.txt'")
print("os.link(path,dst)")
#os.link(path,dst)
print ("Created hard link successfully!!")



#os.listdir(path)
"""Return a list containing the names of the entries in the directory given by path."""
print('\n*os.listdir() Method *')
print("""
Description 
The method listdir() returns a list containing the names of the entries in the directory given by path. The list is in arbitrary order. It does not include the special entries '.' and '..' even if they are present in the directory. 
path may be either of type str or of type bytes. If path is of type bytes, the filenames returned will also be of type bytes; in all other circumstances, they will be of type str. 
Syntax 
Following is the syntax for listdir() method- 
    os.listdir(path) 
Parameters 
path - This is the directory, which needs to be explored. 
Return Value This method returns a list containing the names of the entries in the directory given by path. 
""")
path = 'E:\\Hesbon\\#code\\Python\\Learn Python\\files_io'
print("path:",path)
print("os.listdir():",os.listdir())
print()
print("os.listdir(path):",os.listdir(path))


#os.lseek(fd, pos, how)
"""Set the current position of file descriptor fd to position pos, modified by how."""
print('\n*os.lseek() Method*')
print("""
Description 
The method lseek() sets the current position of file descriptor fd to the given position pos, modified by how. 
Syntax
 Following is the syntax for lseek() method- 
    os.lseek(fd, pos, how) 
Parameters 
    * fd - This is the file descriptor, which needs to be processed.  
    * pos - This is the position in the file with respect to given parameter how. You give os.SEEK_SET or 0 to set the position relative to the beginning of the file, os.SEEK_CUR or 1 to set it relative to the current position; os.SEEK_END or 2 to set it relative to the end of the file.  
    * how - This is the reference point with-in the file. os.SEEK_SET or 0 means beginning of the file, os.SEEK_CUR or 1 means the current position and os.SEEK_END or 2 means end of the file. 
*Defined pos constants 
-> os.SEEK_SET - 0 
-> os.SEEK_CUR - 1 
-> os.SEEK_END - 2 
Return Value 
This method does not return any value. 
""")
print('Example')
#open a file
fd = os.open('foo3.txt',os.O_RDWR|os.O_CREAT)
os.lseek(fd,os.SEEK_SET,os.SEEK_CUR)
print("os.read(fd,100):",os.read(fd,100))
#close opened file
os.close(fd)

#os.lstat(path)
"""Like stat(), but do not follow symbolic links."""
print('\n*os.lstat() Method *')
print("""
Description 
The method lstat() is very similar to fstat() and returns a stat_result object containing the information about a file, but do not follow symbolic links. This is an alias for fstat() on platforms that do not support symbolic links, such as Windows. 
Here is the structure returned by lstat method- 
    * st_dev: ID of device containing file  
    * st_ino: inode number  
    * st_mode: protection  
    * st_nlink: number of hard links  
    * st_uid: user ID of owner  
    * st_gid: group ID of owner  
    * st_rdev: device ID (if special file)  
    * st_size: total size, in bytes  
    * st_blksize: blocksize for filesystem I/O  
    * st_blocks: number of blocks allocated  
    * st_atime: time of last access  
    * st_mtime: time of last modification  
    * st_ctime: time of last status change 
   
Syntax 
Following is the syntax for lstat() method: 
    os.lstat(path) 
Parameters 
path - This is the file for which information would be returned. 
Return Value 
This method returns the information about a file.
 
""")
print('Example')
#open a file
fd = os.open('foo2.txt',os.O_RDWR|os.O_CREAT)
path = 'foo2.txt'
#close the opened file
os.close(fd)
#now get the tuple
print("os.lstat(path):",os.lstat(path))
#now get the uid of the file
print("os.lstat(path).st_uid:",os.lstat(path).st_uid)
#now get the gid of the file
print("os.lstat(path).st_gid:",os.lstat(path).st_gid)
print("Last access time")
print("time.asctime(time.localtime(os.lstat(path).st_atime)):",time.asctime(time.localtime(os.lstat(path).st_atime)))
print("last modification time")
print("time.asctime(time.localtime(os.lstat(path).st_mtime)):",time.asctime(time.localtime(os.lstat(path).st_mtime)))
print("Last status change time")
print("time.asctime(time.localtime(os.lstat(path).st_ctime)):",time.asctime(time.localtime(os.lstat(path).st_ctime)))




#os.major(device)
"""Extract the device major number from a raw device number."""
print('\n*os.major() Method*')
print("""
Description 
The method major() extracts the device major number from a raw device number (usually the st_dev or st_rdev field from stat). 
Syntax 
Following is the syntax for major() method- 
    os.major(device) 
Parameters 
device - This is a raw device number (usually the st_dev or st_rdev field from stat). 
Return Value 
This method returns the device major number.
""")
#print('Example')
#path = 'foo2.txt'
#get the tuple
#print("os.lstat(path):",os.lstat(path))
#print("os.minor(os.lstat(path).st_dev):",os.major(os.lstat(path).st_dev))
#print("os.minor(os.lstat(path).st_rdev):",os.major(os.lstat(path).st_rdev))
#print("os.minor(os.lstat(path).st_dev):",os.minor(os.lstat(path).st_dev))
#print("os.minor(os.lstat(path).st_rdev):",os.minor(os.lstat(path).st_rdev))

#AttributeError: module 'os' has no attribute 'major'
#AttributeError: module 'os' has no attribute 'minor'

#os.makedev(major, minor)
"""Compose a raw device number from the major and minor device numbers."""
print('\n*os.makedev() Method*')
print("""
Description   
The method makedev() composes a raw device number from the major and minor device numbers. 
Syntax 
Following is the syntax for makedev() method- 
    os.makedev(major, minor) 
Parameters 
    * major - This is Major device number.  
    * minor - This is Minor device number. 
Return Value 
This method returns the device number.  
""")
#print('Example')
#path = 'foo2.txt'
#get the tuple
#print("os.lstat(path):",os.lstat(path))
#print("os.minor(os.lstat(path).st_dev):",os.major(os.lstat(path).st_dev))
#print("os.minor(os.lstat(path).st_rdev):",os.major(os.lstat(path).st_rdev))
#print("os.minor(os.lstat(path).st_dev):",os.minor(os.lstat(path).st_dev))
#print("os.minor(os.lstat(path).st_rdev):",os.minor(os.lstat(path).st_rdev))
# Make a device number
#print("os.makedev(os.major(os.lstat(path).st_dev),os.minor(os.lstat(path).st_dev)):",os.makedev(os.major(os.lstat(path).st_dev),os.minor(os.lstat(path).st_dev)))
#AttributeError: module 'os' has no attribute 'makedev'




#os.makedirs(path[, mode])
"""Recursive directory creation function."""
print('\n*os.makedirs() Method*')
print("""
Description 
The method makedirs() is recursive directory creation function. Like mkdir(), but makes all intermediate-level directories needed to contain the leaf directory. 
The default mode is 0o777 (octal). On some systems, mode is ignored. Where it is used, the current umask value is first masked out. 
If exist_ok is False (the default), an OSError is raised if the target directory already exists. 
Syntax Following is the syntax for makedirs() method- 
os.makedirs(path[, mode]) 
Parameters 
    * path - This is the path, which needs to be created recursively.  
    * mode - This is the Mode of the directories to be given. 
Return Value This method does not return any value. 
""")
print('Example')
path = 'test/tmp/monthly/daily'
#os.makedirs(path,493) #decimal equivalent of 0755 used on windows
print("os.makedirs(path,493)")
print("Path is created: ",path)





#os.minor(device)
"""Extract the device minor number from a raw device number ."""
print('os.minor() Method ')
print("""
Description 
The method minor() extracts the device minor number from a raw device number (usually the st_dev or st_rdev field from stat).
Syntax 
Following is the syntax for minor() method- 
    os.minor(device) 
Parameters 
    device - This is a raw device number (usually the st_dev or st_rdev field from stat). 
Return Value 
This method returns the device minor number.  
""")
#print('Example')
#path = 'foo2.txt'
#get the tuple
#print("os.lstat(path):",os.lstat(path))
#print("os.minor(os.lstat(path).st_dev):",os.major(os.lstat(path).st_dev))
#print("os.minor(os.lstat(path).st_rdev):",os.major(os.lstat(path).st_rdev))
#print("os.minor(os.lstat(path).st_dev):",os.minor(os.lstat(path).st_dev))
#print("os.minor(os.lstat(path).st_rdev):",os.minor(os.lstat(path).st_rdev))

#AttributeError: module 'os' has no attribute 'major'
#AttributeError: module 'os' has no attribute 'minor'

#os.mkdir(path[, mode])
"""Create a directory named path with numeric mode mode."""
print('\n*os.mkdir() Method*')
print("""
Description 
The method mkdir() create a directory named path with numeric mode mode. The default mode is 0777 (octal). On some systems, mode is ignored. Where it is used, the current umask value is first masked out.
Syntax 
Following is the syntax for mkdir() method- 
    os.mkdir(path[, mode]) 
Parameters 
    * path - This is the path, which needs to be created.  
    * mode - This is the mode of the directories to be given. Return Value 
This method does not return any value. 
""")
print('Example')
#path = 'test/tmp2/monthly/daily'
#mkdir can.t work using this path
path = 'tmp'
#os.mkdir(path,0o755);
print("os.mkdir(path,0o755)")
print("Path is created: ",path)




#os.mkfifo(path[, mode])
"""Create a FIFO (a named pipe) named path with numeric mode mode. The default mode is 0666 (octal)."""
print('\n*os.mkfifo() Method *')
print("""
Description 
The method mkfifo() create a FIFO named path with numeric mode. The default mode is 0666 (octal).The current umask value is first masked out. 
FIFOs are pipes that can be accessed like regular files. FIFOs exist until they are deleted 
Syntax 
Following is the syntax for mkfifo() method- 
    os.mkfifo(path[, mode])
Parameters
    * path - This is the path, which needs to be created.  
    * mode - This is the mode of the named path to be given. 
Return Value 
This method does not return any value.
""")
#print('Example')
#path = '/tmp/hourly'
#os.mkfifo(path,0o644)
#print("os.mkfifo(path,0o644)")
#print("Path created: ",path)
#os.mkfifo(path,0o644)

#os.mknod(filename[, mode=0600, device])
"""Create a filesystem node (file, device special file or named pipe) named filename."""
print('\n*os.mknod() Method*')
print("""
Description 
The method mknod() creates a filesystem node (file, device special file or named pipe) named filename. 
Syntax 
Following is the syntax for mknod() method- 
    os.mknod(filename[, mode=0600[, device=0]]) 
Parameters 
    * filename - This is the filesystem node to be created.  
    * mode - The mode specifies both the permissions to use and the type of node to be created combined (bitwise OR) with one of the values stat.S_IFREG, stat.S_IFCHR, stat.S_IFBLK, and stat.S_IFIFO. They can be ORed base don requirement.  
    * device - This is the device special file created and its optional to provide. 
""")
#print('Example')
#filename = 'tmp/tmpfile'
#mode = 0o600 | stat.S_IRUSR
#filesystem node specified with different nodes
#os.mknod(filename,mode)

#AttributeError: module 'os' has no attribute 'mknod'


#os.open(file, flags[, mode])
"""Open the file file and set various flags according to flags and possibly its mode according to mode."""
print('\n*os.open() Method*')
print("""
Description 
The method open() opens the file file and set various flags according to flags and possibly its mode according to mode.The default mode is 0777 (octal), and the current umask value is first masked out. 
Syntax 
Following is the syntax for open() method: 
    os.open(file, flags[, mode]); 
Parameters 
    * file - File name to be opened.  
    * flags - The following constants are options for the flags. They can be combined using the bitwise OR operator |. Some of them are not available on all platforms. 
        -> os.O_RDONLY: open for reading only 
        -> os.O_WRONLY: open for writing only 
        -> os.O_RDWR : open for reading and writing 
        -> os.O_NONBLOCK: do not block on open 
        -> os.O_APPEND: append on each write 
        -> os.O_CREAT: create file if it does not exist 
        -> os.O_TRUNC: truncate size to 0 
        -> os.O_EXCL: error if create and file exists 
        -> os.O_SHLOCK: atomically obtain a shared lock 
        -> os.O_EXLOCK: atomically obtain an exclusive lock 
        -> os.O_DIRECT: eliminate or reduce cache effects 
        -> os.O_FSYNC : synchronous writes 
        -> os.O_NOFOLLOW: do not follow symlinks 
    * mode - This work in similar way as it works for chmod() method. 

Return Value 
This method returns the file descriptor for the newly opened file.
""")
print('Example')
#open a file
fd = os.open('dum.txt',os.O_RDWR|os.O_CREAT)
#write a string
#line = 'sample dummy text in a dummy file'
#b = str.encode(line)
#os.write(b)
print("File opened successfully")
os.close(fd)
print('File closed successfully')


#os.openpty()
"""Open a new pseudo-terminal pair. Return a pair of file descriptors (master, slave) for the pty and the tty, respectively."""
print('\n*os.openpty() Nethod*')
print("""
The method openpty() opens a pseudo-terminal pair and returns a pair of file descriptors(master,slave) for the pty & the tty respectively. 
The new file descriptors are non-inheritable. For a (slightly) more portable approach, use the pty module. 
Syntax 
Following is the syntax for openpty() method- 
    os.openpty() 
Parameters 
NA 
Return Value 
This method returns a pair of file descriptors i.e., master and slave. 
""")
#print('Example')
#master for pty, slave for tty
#m,s = os.openpty()
#print("m,s = os.openpty()")
#print(m)
#print(s)
#showing terminal name
#s = os.ttyname(s)
#print(m)
#print(s)
#AttributeError: module 'os' has no attribute 'openpty'



#os.pathconf(path, name)
"""Return system configuration information relevant to a named file."""
print('\n*os.pathconf() Method*')
print("""
The method pathconf() returns system configuration information relevant to a named file. 
Syntax 
Following is the syntax for pathconf() method- 
    os.pathconf(path, name) 
Parameters 
    * path - This is the file path.  
    * name - This specifies the configuration value to retrieve; it may be a string which is the name of a defined system value; these names are specified in a number of standards (POSIX.1, Unix 95, Unix 98, and others). The names known to the host operating system are given in the os.pathconf_names dictionary.  
Return Value 
This method returns system configuration information of a file. Available on Unix like systems. 
""")
#print('Example')
#print ("%s" % os.pathconf_names)
# Retrieve maximum length of a filename
#no = os.pathconf('files_io.py', 'PC_NAME_MAX')
#print ("Maximum length of a filename :%d" % no)
# Retrieve file size
#no = os.pathconf('a2.py', 'PC_FILESIZEBITS')
#print ("file size in bits  :%d" % no)


#os.pipe()
"""Create a pipe. Return a pair of file descriptors (r, w) usable for reading and writing, respectively."""
print('\n*os.pipe() Method*')
print("""
Description 
The method pipe() creates a pipe and returns a pair of file descriptors (r, w) usable for reading and writing, respectively 
Syntax 
Following is the syntax for pipe() method- 
    os.pipe() 
Parameters
 NA 
Return Value 
This method returns a pair of file descriptors. 
""")
#print('Example')
#print("The child will write text to a pipe and ")
#print("the parent will read text written by child...")
#file descriptors r, w for reading and writing
#r,w = os.pipe()

#process_id = os.fork()
#if process_id:
    #This is the parent process
    #Closes file descriptor w
 #   os.close(w)
 #  r = os.fdopen(r)
  # print("Parent reading")
    #str = r.read()
    #print("r: ",r)
    #sys.exit(0)
#else:
    #This is the child process
 #   os.close(r)
  #  w = os.fdopen(w,'w')
   # print("Child writing")
    #w.write("Text written by child...")
    #w.close()
    #print('Child closing')
    #sys.exit(0)

#AttributeError: module 'os' has no attribute 'fork'


#os.popen(command[, mode[, bufsize]])
"""Open a pipe to or from command."""
print('\n*os.popen() Method*')
print("""
Description 
The method popen() opens a pipe to or from command.The return value is an open file object connected to the pipe, which can be read or written depending on whether mode is 'r' (default) or 'w'.The bufsize argument has the same meaning as in open() function. 
Syntax 
Following is the syntax for popen() method- 
    os.popen(command[, mode[, bufsize]]) 
Parameters 
    * command - This is command used.  
    * mode - This is the Mode can be 'r'(default) or 'w'. 
    * bufsize - If the buffering value is set to 0, no buffering will take place. If the buffering value is 1, line buffering will be performed while accessing a file. If you specify the buffering value as an integer greater than 1, then buffering action will be performed with the indicated buffer size. If negative, the buffer size is the system default(default behavior). 
Return Value 
This method returns an open file object connected to the pipe.
""")
print('Example')
#using command mkdir
#a = 'mkdir nwdir'
print("a = 'mkdir nwdir'")
#b = os.popen(a,'r',1)
print("print (b = os.popen(a,'r',1))")
#print('b:',b)
print("b: <os._wrap_close object at 0x0000009448540F98>")


#os.read(fd, n)
"""Read at most n bytes from file descriptor fd. Return a string containing the bytes read. If the end of the file referred to by fd has been reached, an empty string is returned."""
print('\n*os.read() Method*')
print("""
Description 
The method read() reads at most n bytes from file desciptor fd, return a string containing the bytes read. If the end of file referred to by fd has been reached, an empty string is returned. 
*Note: This function is intended for low-level I/O and must be applied to a file descriptor as returned by os.open() or pipe(). To read a “file object” returned by the built-in function open() or by popen() or fdopen(), or sys.stdin, use its read() or readline() methods. 
Syntax 
Following is the syntax for read() method- 
    os.read(fd,n) 
Parameters 
    * fd - This is the file descriptor of the file.  
    * n - These are n bytes from file descriptor fd. 
Return Value
 This method returns a string containing the bytes read. 
""")
print('Example')
# Open a file
fd = os.open("foo3.txt",os.O_RDWR)
# Reading text
ret = os.read(fd,12)
print (ret.decode())
# Close opened file
os.close(fd)

#os.readlink(path)
"""Return a string representing the path to which the symbolic link points."""
print('\n*os.readlink() Method*')
print("""
Description 
The method readlink() returns a string representing the path to which the symbolic link points. It may return an absolute or relative pathname. 
Syntax 
Following is the syntax for readlink() method- 
    os.readlink(path) 
Parameters 
path - This is the path or symblic link for which we are going to find source of the link. 
Return Value 
This method return a string representing the path to which the symbolic link points. 
""")
#print('Example')
#src = 'test/tmp/monthly/daily'
#dst = 'test/tmp/monthly/daily2'
# This creates a symbolic link on python in tmp directory
#os.symlink(src, dst)
# Now let us use readlink to display the source of the link.
#path = os.readlink( dst )
#print (path)


#os.remove(path)
"""Remove the file path."""
print('\n*os.remove() Method*')
print("""
Description 
The method remove() removes the file path. If the path is a directory, OSError is raised. 
Syntax Following is the syntax for remove() method- 
    os.remove(path) 
Parameters
 path - This is the path, which is to be removed. 
Return Value
 This method does not return any value. 
""")
#print("Example")
#removing
#os.remove(dum.txt)


#os.removedirs(path)
"""Remove directories recursively."""
print('\n*os.removedirs() Method*')
print("""
Description 
The method removedirs() removes dirs recursively. If the leaf directory is succesfully removed, removedirs tries to successively remove every parent directory displayed in path. Raises OSError if the leaf directory could not be successfully removed. 
Syntax 
Following is the syntax for removedirs() method- 
    os.removedirs(path) 
Parameters
 path - This is the path of the directory, which needs to be removed. 
Return Value 
This method does not return any value.
""")
#print('Example')
#os.remove('test/tmp/monthly/daily/hourly')


#os.rename(src, dst)
"""Rename the file or directory src to dst."""
print('\n*os.rename() Method*')
print("""
Description 
The method rename() renames the file or directory src to dst. If dst is a file or directory(already present), OSError will be raised. 
Syntax 
Following is the syntax for rename() method- 
    os.rename(src, dst) 
Parameters 
    * src - This is the actual name of the file or directory.  
    * dst - This is the new name of the file or directory. 
Return Value 
This method does not return any value. 
""")
#print('Example')
#os.rename('dum.txt','dum_file.txt')
#os.rename('tmp','tempo')

#os.renames(old, new)
"""Recursive directory or file renaming function."""

print('\n*os.renames() Method*')
print("""
Description
The method renames() is recursive directory or file renaming function. It does the same functioning as os.rename(), but it also moves a file to a directory, or a whole tree of directories, that do not exist. 
Syntax 
Following is the syntax for renames() method: 
    os.renames(old, new) 
Parameters 
    * old - This is the actual name of the file or directory to be renamed.  
    * new - This is the new name of the file or directory. It can even include a file to a directory, or a whole tree of directories, that do not exist. 
Return Value 
This method does not return any value.
""")
#print('Example')
#os.renames('dum.txt','myfiles/dummy_files/dum.txt')



#os.rmdir(path)
"""Remove the directory path"""
print('\n*os.rmdir() Method*')
print("""
The method rmdir() removes the directory path. It works only when the directory is empty, else OSError is raised. 
Syntax 
Following is the syntax for rmdir() method- 
    os.rmdir(path) 
Parameters 
path - This is the path of the directory, which needs to be removed. 
""")
#print('Example')
#os.rmdir(tmp)

#os.stat(path)
"""Perform a stat system call on the given path."""
print('\n*os.stat() Method*')
print("""
Description 
The method stat() performs a stat system call on the given path. 
Syntax 
Following is the syntax for stat() method- 
    os.stat(path) 
Parameters 
path - This is the path, whose stat information is required. 
Return Value 
Here is the list of members of stat structure- 
    * st_mode: protection bits.
    * st_ino: inode number. 
    * st_dev: device. 
    * st_nlink: number of hard links. 
    * st_uid: user id of owner. 
    * st_gid: group id of owner. 
    * st_size: size of file, in bytes. 
    * st_atime: time of most recent access. 
    * st_mtime: time of most recent content modification. 
    * st_ctime: time of most recent metadata change.
""")
print('Example')
print("os.stat('foo.txt')",os.stat('foo.txt'))
print("os.stat('foo.txt').st_mode",os.stat('foo.txt').st_mode)


#os.stat_float_times([newvalue])
"""Determine whether stat_result represents time stamps as float objects."""
print('\n*os.stat_float_times() Method*')
print("""
Description 
The method stat_float_times() determines whether stat_result represents time stamps as float objects. 
Syntax 
Following is the syntax for stat_float_times() method- 
    os.stat_float_times([newvalue]) 
Parameters 
    * newvalue - If newvalue is True, future calls to stat() return floats, if it is False, future call on stat returns ints. If newvalue is not mentioned, it returns the current settings. 
Return Value 
This method returns either True or False.
""")
#print('Example')
# Stat information
#statinfo = os.stat('files_io.py')
#print (statinfo)
#statinfo = os.stat_float_times()
#print (statinfo)
#AttributeError: module 'os' has no attribute 'stat_float_times'


#os.statvfs(path)
"""Perform a statvfs system call on the given path."""
print('\n*os.statvfs() Method*')
print("""
Description 
The method statvfs() perform a statvfs system call on the given path. 
Syntax 
Following is the syntax for statvfs() method- 
    os.statvfs(path) 
Parameters
*path - This is the path, whose statvfs information is required. 
Return Value 
Here is the list of members of statvfs structure- 
    * f_bsize: preferred file system block size. 
    * f_frsize: fundamental file system block size. 
    * f_blocks: total number of blocks in the filesystem. 
    * f_bfree: total number of free blocks. 
    * f_bavail: free blocks available to non-super user. 
    * f_files: total number of file nodes. 
    * f_ffree: total number of free file nodes. 
    * f_favail: free nodes available to non-super user. 
    * f_flag: system dependent. 
    * f_namemax: maximum file name length. 
""")
#print('Example')
#print("os.statvfs('foo.txt'):",os.statvfs('foo.txt'))
#AttributeError: module 'os' has no attribute 'statvfs'


#os.symlink(src, dst)
"""Create a symbolic link pointing to src named dst."""
print('\n*os.symlink() Method*')
print("""
Description 
The method symlink() creates a symbolic link dst pointing to src. 
Syntax 
Following is the syntax for symlink() method- 
    os.symlink(src, dst) 
Parameters 
    * src - This is the source.  
    * dest - This is the destination, which did not exist previously. 
Return Value 
This method does not return any value. 
""")
#print('Example')
#src = 'test/tmp/monthly/daily'
#dst = 'tmp/daily'
#This creates a symbolic link on pythob in tmp directory
#os.symlink(src,dst)
#print('symlink created: ',dst)

#OSError: symbolic link privilege not held

#os.tcgetpgrp(fd)
"""Return the process group associated with the terminal given by fd (an open file descriptor as returned by open())."""
print('\n*os.tcgetpgrp() Method*')
print("""
Description 
The method tcgetpgrp() returns the process group associated with the terminal given by fd (an open file descriptor as returned by os.open()) 
Syntax 
Following is the syntax for tcgetpgrp() method- 
    os.tcgetpgrp(fd) 
Parameters 
fd - This is the file descriptor. 
Return Value 
This method returns the process group.
""")
#print('Example')
#fd = os.open('foo.txt',os.O_RDONLY)
#fd = os.open('test/tmp/monthly',os.O_RDONLY)
#PermissionError: [Errno 13] Permission denied: 'test/tmp/monthly'
#showing the process grouop
#print("os.tcgetpgrp(fd)",os.tcgetpgrp(fd))
#os.close(fd)

#AttributeError: module 'os' has no attribute 'tcgetpgrp'


#os.tcsetpgrp(fd, pg)
"""Set the process group associated with the terminal given by fd (an open file descriptor as returned by open()) to pg."""
print('\n*os.tcsetpgrp() Method*')
print("""
Description 
The method tcsetpgrp() sets the process group associated with the terminal given by fd (an open file descriptor as returned by os.open()) to pg. 
Syntax 
Following is the syntax for tcsetpgrp() method- 
    os.tcsetpgrp(fd, pg) 
Parameters 
    * fd - This is the file descriptor.  
    * pg - This set the process group to pg. 
Return Value 
This method does not return any value.
""")
print('Example')
fd = os.open('foo.txt',os.O_RDONLY)
#fd = os.open('test/tmp/monthly',os.O_RDONLY)
#PermissionError: [Errno 13] Permission denied: 'test/tmp/monthly'
#showing the process group
#print("os.tcgetpgrp(fd)",os.tcgetpgrp(fd))
#Setting the process group
#print("os.tcsetpgrp(fd,2672):",os.tcsetpgrp(fd,2672))
#s.close(fd)
#AttributeError: module 'os' has no attribute 'tcsetpgrp'



#os.tempnam([dir[, prefix]])
"""Return a unique path name that is reasonable for creating a temporary file."""
print('\n*os.tempnam() Method*')
print("""
Description 
The method tempnam() returns a unique path name that is reasonable for creating a temporary file. 
Syntax 
Following is the syntax for tempnam() method- 
    os.tempnam(dir, prefix) 
Parameters 
    * dir - This is the dir where the temporary filename will be created.  
    * prefix - This is the prefix of the generated temporary filename. 
Return Value 
This method returns a unique path. 
""")
#print('Example')
#prefix is pre of the generated file
#print("os.tempnam('test/tmp','pre'):",os.tempnam('test/tmp','pre'))
#AttributeError: module 'os' has no attribute 'tempnam'

#os.tmpfile()
"""Return a new file object opened in update mode (w+b)."""
print('\n*os.tmpfile() Method*')
print("""
Description 
The method tmpfile() returns a new temporary file object opened in update mode (w+b). The file has no directory entries associated with it and will be deleted automatically once there are no file descriptors. 
Syntax 
Following is the syntax for tmpfile() method- 
    os.tmpfile 
Parameters 
NA  
Return Value 
This method returns a new temporary file object.
""")
#print('Example')
# The file has no directory entries associated with it and will be
# deleted automatically once there are no file descriptors.
#tmpfile = os.tmpfile()
#tmpfile.write("Here goes a temporary file....")
#tmpfile.seek(0)
#print("tmpfile.read():",tmpfile.read())
#tmpfile.close()
#AttributeError: module 'os' has no attribute 'tmpfile'


#os.tmpnam()
"""Return a unique path name that is reasonable for creating a temporary file."""
print('\n*os.tmpnam() Method*')
print("""
Description 
The method tmpnam() returns a unique path name that is reasonable for creating a temporary file. 
Syntax 
Following is the syntax for tmpnam() method- 
    os.tmpnam() 
Parameters 
NA 
Return Value 
This method returns a unique path name.
""")
#print('Example')
#temporary file generated in current directory
#tmpfn = os.tmpnam()
#print("os.tmpnam():",tmpfn)

#AttributeError: module 'os' has no attribute 'tmpnam'


#os.ttyname(fd)
"""Return a string which specifies the terminal device associated with file descriptor fd. If fd is not associated with a terminal device, an exception is raised."""
print('\n*os.ttyname() Method*')
print("""
The method ttyname() returns a string, which specifies the terminal device associated with fd. If fd is not associated with a terminal device, an exception is raised. 
Syntax 
Following is the syntax for ttyname() method- 
    os.ttyname(fd) 
Parameters 
fd - This is the file descriptor. 
Return Value 
This method returns a string which specifies the terminal device. Available on Unix like Systems.
""")
#print('Example')
#fd = os.open('foo3.txt',os.O_RDONLY)
#print("os.ttyname(fd):",os.ttyname(fd))
#os.close(fd)
#AttributeError: module 'os' has no attribute 'ttyname'


#os.unlink(path)
"""Remove the file path."""
print('\n*os.unlink() Method*')
print("""
Description 
The method unlink() removes (deletes) the file path. If the path is a directory, OSError is raised. This function is identical to the remove() mehod; the unlink name is its traditional Unix name. 
Syntax 
Following is the syntax for unlink() method- 
    os.unlink(path) 
Parameters 
path - This is the path, which is to be removed. 
Return Value 
This method does not return any value. 
""")
#print('Example')
#os.unlink('foo.txt')



#os.utime(path, times)
"""Set the access and modified times of the file specified by path."""
print('\n*os.utime() Method*')
print("""
Description 
The method utime() sets the access and modified times of the file specified by path. 
Syntax 
Following is the syntax for utime() method- 
    os.utime(path, times) 
Parameters 
    * path - This is the path of the file.  
    * times - This is the file access and modified time. If times is none, then the file access and modified times are set to the current time. The parameter times consists of row in the form of (atime, mtime) i.e (accesstime, modifiedtime). 
Return Value 
This method does not return any value.
""")
print('Example')
print("os.utime('foo3.txt',(0,0)):",os.utime('foo3.txt',(0,0)))
print("time.asctime(time.localtime(os.stat('foo3.txt').st_atime)):",time.asctime(time.localtime(os.stat('foo3.txt').st_atime)))
print("os.utime('foo3.txt')):",os.utime('foo3.txt'))
print("time.asctime(time.localtime(os.stat('foo3.txt').st_atime)):",time.asctime(time.localtime(os.stat('foo3.txt').st_atime)))
#os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
"""Generate the file names in a directory tree by walking the tree either top-down or bottom-up."""
print('\n*os.walk() Method*')
print("""
Description 
The method walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up. 
Syntax 
Following is the syntax for the walk() method- 
    os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]]) 
Parameters 
    * top - Each directory rooted at directory, yields 3-tuples, i.e., (dirpath, dirnames, filenames)  
    * topdown - If optional argument topdown is True or not specified, directories are scanned from top-down. If topdown is set to False, directories are scanned from bottom-up.  
    * onerror - This can show error to continue with the walk, or raise the exception to abort the walk.  
    * followlinks - This visits directories pointed to by symlinks, if set to true. 
Return Value 
This method does not return any value. 
""")
print('Example')
for root, dirs, files in os.walk(".",topdown = False):
    for name in files:
        print(os.path.join(root,name))
    for name in dirs:
        print(os.path.join(root,name))

print("\nview source code :)")

#os.write(fd, str)
"""Write the string str to file descriptor fd. Return the number of bytes actually written."""

print('\n*os.write() Method*')
print("""
Description 
The method write() writes the string str to file descriptor fd. It returns the number of bytes actually written. 
Syntax 
Following is the syntax for write() method- 
    os.write(fd, str) 
Parameters
    * fd - This is the file descriptor.  
    * str - This is the string to be written. 
Return Value 
This method returns the number of bytes actually written.
""")
#print('Example')
# Open a file
#fd = os.open( "f1.txt", os.O_RDWR|os.O_CREAT )
# Write one string
#line="this is test"
#print("os.write(fd,'this is test'):",os.write(fd,"this is test"))
# string needs to be converted byte object
#b=str.encode(line)
#ret=os.write(fd, line)
# ret consists of number of bytes written to f1.txt
#print ("the number of bytes written: ", ret)
# Close opened file
#os.close( fd)



