#CGI Programming
print("{:^100}".format("***CGI PROGRAMMING***"))
print("""The Common Gateway Interface, or CGI, is a set of standards that define how information is exchanged between the web server and a custom script. The CGI specs are currently maintained by the NCSA and NCSA. """)

print("\n*What is CGI*")
print("""   * The Common Gateway Interface, or CGI, is a standard for external gateway programs to interface with information servers such as HTTP servers.  
    * The current version is CGI/1.1 and CGI/1.2 is under progress. """)
print("\n*Web Browsing *")
print("""To understand the concept of CGI, let us see what happens when we click a hyperlink to browse a particular web page or URL. 
    * Your browser contacts the HTTP web server and demands for the URL, i.e., filename.  
    * The web server parses the URL and looks for the filename. If it finds the particular file, then it sends it back to the browser, otherwise sends an error message indicating that you requested a wrong file.  
    * The web browser takes response from the web server and displays either, the received file or error message. 
However, it is possible to set up the HTTP server so that whenever a file in a certain directory is requested that file is not sent back. Instead, it is executed as a program, and whatever that output of the program, is sent back for your browser to display. This function is called the Common Gateway Interface or CGI and the programs are called CGI scripts. These CGI programs can be Python Script, PERL Script, Shell Script, C or C++ program, etc.
""")

print("{:^50}".format("*CGI Architecture Diagram*"))
#sample sketch diagram
print(""" 
                       ____________
                 |<-- [ Web Server ]
                 |     ------------
                 |         i
                 |         :
                 |         !
  ___________    |  __________________
 [ Web Client]-->| [Server Side Script]
  ------------   |  ------------------
                 |         i
                 |         :
                 |         !
                 |     __________
                 |    ( Database )
                 |     ----------
           HTTP Protocal
""")

print("{:<100}".format("*Web Server Support and Configuration*"))
print("""Before you proceed with CGI Programming, make sure that your Web Server supports CGI and it is configured to handle CGI Programs. All the CGI Programs, which are to be executed by the HTTP server, are kept in a pre-configured directory. This directory is called CGI Directory and by convention it is named as /var/www/cgi-bin. By convention, CGI files have extension as .cgi, but you can keep your files with python extension .py as well. 
By default, the Linux server is configured to run only the scripts in the cgi-bin directory in /var/www. If you want to specify any other directory to run your CGI scripts, comment the following lines in the httpd.conf file −""")

print("""<Directory "/var/www/cgi-bin"> 
   AllowOverride None 
   Options ExecCGI 
   Order allow,deny 
   Allow from all 
</Directory>
<Directory "/var/www/cgi-bin"> 
Options All 
</Directory> 
The following line should also be added for apache server to treat .py file as cgi script. 
    AddHandler cgi-script .py 
Here, we assume that you have Web Server up and running successfully and you are able to run any other CGI program like Perl or Shell, etc. """)

print("\nFirst CGI Program")
print("""Here is a simple link, which is linked to a CGI script called hello.py. This file is kept in /var/www/cgi-bin directory and it has the following content. Before running your CGI program, make sure you have changed the mode of file using chmod 755 hello.py, the UNIX command to make file executable.""")


#cgi program
print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<title>Hello World - First CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Hello World!</h2>")
print("</body>")
print("</html>")

print("""\nWorking code: CGI in Perl:)\n
#!"E:\\xampp\\perl\\bin\\perl.exe"
print "Content-type: text/html\\n\\n";
print '<html>';
print '<head>';
print '<title>Hello World - First CGI Program</title>';
print '</head>';
print '<body>';
print '<h2>Hello World!</h2>';
print '</body>';
print '</html>';
\n**Note: You have to include the #!"E:\\xampp\\perl\\bin\\perl.exe" line !!!
""")
print("""*Note: First line in the script must be the path to Python executable. In Linux, it should be #!/usr/bin/python3 
Enter the following URL in your browser -  
    http://www.tutorialspoint.com/cgi-bin/hello.py 
Hello Word! This is my first CGI program 
This hello.py script is a simple Python script, which writes its output on STDOUT file, i.e., the screen. There is one important and extra feature available that is the first line to be printed Content-type:text/html followed by a blank line. This line is sent back to the browser and it specifies the content type to be displayed on the browser screen. 
By now, you must have understood the basic concept of CGI and you can write many complicated CGI programs using Python. This script can interact with any other external system also to exchange information such as RDBMS. 
""")
print("HTTP Header")
print("""The line Content-type:text/html\\r\\n\\r\\n is part of HTTP header which is sent to the browser to understand the content. All the HTTP header will be in the following form- 
HTTP Field Name: Field Content 
For Example 
Content-type: text/html\\r\\n\\r\\n 
There are few other important HTTP headers, which you will use frequently in your CGI Programming. """)

print("\nHEADER\t\t\t\tDESCRIPTION")
print("Content-type: \tA MIME string defining the format of the file being returned. Example is Content-type:text/html ")
print("Expires: \t\tURL The URL that is returned instead of the URL requested. You can use this field to redirect a request to any file.")
print("Last-modified: \tDate The date of last modification of the resource. ")
print("Content-length: \tN The length, in bytes, of the data being returned. The browser uses this value to report the estimated download time for a file. ")
print("Set-Cookie: \t\t)String Set the cookie passed through the string ")

print("\n*CGI Environment Variables *")
print("All the CGI programs have access to the following environment variables. These variables play an important role while writing any CGI program.")
print("VARIABLE NAME\t\t\t\tDESCRIPTION")
print("CONTENT_TYPE \tThe data type of the content. Used when the client is sending attached content to the server. For example, file upload. ")
print("CONTENT_LENGTH \tThe length of the query information. It is available only for POST requests")
print("HTTP_COOKIE \tReturns the set cookies in the form of key & value pair.")
print("HTTP_USER_AGENT \tThe User-Agent request-header field contains information about the user agent originating the request. It is name of the web browser. ")
print("PATH_INFO \t\tThe path for the CGI script. ")
print("QUERY_STRING \tThe URL-encoded information that is sent with GET method request.")
print("REMOTE_ADDR \tThe IP address of the remote host making the request. This is useful logging or for authentication. ")
print("REMOTE_HOST \tThe fully qualified name of the host making the request. If this information is not available, then REMOTE_ADDR can be used to get IR address. ")
print("REQUEST_METHOD \tThe method used to make the request. The most common methods are GET and POST. ")
print("SCRIPT_FILENAME \tThe full path to the CGI script. ")
print("SCRIPT_NAME \tThe name of the CGI script.")
print("SERVER_NAME \tThe server's hostname or IP Address")
print("SERVER_SOFTWARE \tThe name and version of the software the server is running.")

print("Here is a small CGI program to list out all the CGI variables. Click this link to see the result Get Environment.")
"""
import os
print("Content-type: text/html")
print()
print("<font size=+1>Environment</font><\\br>";)
for param in os.environ.keys():
    print("<b>%20s</b?: %s<\\br>"%(param,os.environ[param]))
"""
print("\nuncomment the source code and make sure it is working")

print("\n*GET and POST Methods*")
print("""You must have come across many situations when you need to pass some information from your browser to web server and ultimately to your CGI Program. Most frequently, a browser uses two methods to pass this information to the web server. These methods are GET Method and POST Method.""")
print("\nPassing Information using GET method ")
print("""The GET method sends the encoded user information appended to the page request. The page and the encoded information are separated by the ? character as follows- 
    http://www.test.com/cgi-bin/hello.py?key1=value1&key2=value2 
    * The GET method is the default method to pass information from the browser to the web server and it produces a long string that appears in your browser's Location:box.  
    * Never use GET method if you have password or other sensitive information to pass to the server.  
    * The GET method has size limtation: only 1024 characters can be sent in a request string.  
    * The GET method sends information using QUERY_STRING header and will be accessible in your CGI Program through QUERY_STRING environment variable. 
You can pass information by simply concatenating key and value pairs along with any URL or you can use HTML <FORM> tags to pass information using GET method.""")

print("\nSimple URL Example – Get Method ")
print("""Here is a simple URL, which passes two values to hello_get.py program using GET method. 
/cgi-bin/hello_get.py?first_name=Malhar&last_name=Lathkar 
Given below is the hello_get.py script to handle the input given by web browser. We are going to use the cgi module, which makes it very easy to access the passed information- """)

print("\n***Note: the cgi programs are running in apache server!!!\n\
Path:E/xampp/htdocs/myfiles")


print("""**Tutorial Example...
# Import modules for CGI handling  
import cgi, cgitb   
# Create instance of FieldStorage  
form = cgi.FieldStorage()
# Get data from fields 
first_name = form.getvalue('first_name') 
last_name  = form.getvalue('last_name')  
print ("Content-type:text/html") 
print() 
print ("<html>)" 
print ("<head>") 
print ("<title>Hello - Second CGI Program</title>") 
print ("</head>") 
print ("<body>") 
print ("<h2>Hello %s %s</h2>" % (first_name, last_name)) 
print ("</body>") 
print ("</html>">)
""")
print("\n*Simple FORM Example – GET Method*")
print("This example passes two values using HTML FORM and submit button. We use the same CGI script hello_get.py to handle this input.")


print("""**Tutorial Example...
<form action="/cgi-bin/hello_get.py" method="get"> 
First Name: <input type="text" name="first_name">  <br />  
Last Name: <input type="text" name="last_name" /> 
<input type="submit" value="Submit" /> 
</form>
""")
print("\nRun the \"E:\\xampp\\htdocs\\myfiles\\formget.cgi\"" )
print("""#!"E:\\xampp\\perl\\bin\\perl.exe"
print "Content-type: text/html\\n\\n";
print"<!DOCTYPE html>";
print"<html>";
print"<head>";
print"	<title>Form GET Method</title>";
print"</head>";
print"<body bgcolor=\"maroon\" font=\"harrington\">";
print"	<fieldset width=\"200\" height=\"200\">";
print"		<legend>Name Input</legend>";
print"		<form action=\"hello_get.py\" method=\"get\">";
print"			<label>First name:</label><input type=\"text\" name=\"first_name\" placeholder=\"John\"> <br />";
print"			<label>Last name:</label><input type=\"text\" name=\"last_name\" placeholder=\"Smith\"> <br />";
print"			<input type=\"submit\" value=\"Submit\">";
print"		</form>";
print"	</fieldset>";
print"</body>";
print"</html>";

""")
print("\n*Passing Information Using POST Method*")
print("""A generally more reliable method of passing information to a CGI program is the POST method. This packages the information in exactly the same way as the GET methods, but instead of sending it as a text string after a ? in the URL, it sends it as a separate message. This message comes into the CGI script in the form of the standard input""")

print("""**Tutorial Example...
# Import modules for CGI handling  
import cgi, cgitb   
# Create instance of FieldStorage  
form = cgi.FieldStorage()   
# Get data from fields 
first_name = form.getvalue('first_name') 
last_name  = form.getvalue('last_name')  
print ("Content-type:text/html") 
print() 
print ("<html>") 
print ("<head>") 
print ("<title>Hello - Second CGI Program</title>") 
print ("</head>") 
print ("<body>") 
print ("<h2>Hello %s %s</h2>" % (first_name, last_name)) 
print ("</body>") 
print ("</html>")

Let us again take the same example as above, which passes two values using the HTML FORM and the submit button. We use the same CGI script hello_get.py to handle this input.

<form action="/cgi-bin/hello_get.py" method="post"> 
First Name: <input type="text" name="first_name"><br /> 
Last Name: <input type="text" name="last_name" />  
<input type="submit" value="Submit" /> 
</form>
""")
print("\nRun the \"E:\\xampp\\htdocs\\myfiles\\formpost.cgi\"" )
print("""#!"E:\\xampp\\perl\\bin\\perl.exe"
print "Content-type: text/html\\n\\n";
print"<!DOCTYPE html>";
print"<html>";
print"<head>";
print"	<title>Form POST Method</title>";
print"</head>";
print"<body bgcolor=\"purple\" font=\"harrington\">";
print"	<fieldset width=\"200\" height=\"200\">";
print"		<legend>Name Input</legend>";
print"		<form action=\"hello_get.py\" method=\"post\">";
print"			<label>First name:</label><input type=\"text\" name=\"first_name\" placeholder=\"John\"> <br />";
print"			<label>Last name:</label><input type=\"text\" name=\"last_name\" placeholder=\"Smith\"> <br />";
print"			<input type=\"submit\" value=\"Submit\">";
print"		</form>";
print"	</fieldset>";
print"</body>";
print"</html>";
""")

print("\n*Passing Checkbox Data to CGI Program ")
print("""Checkboxes are used when more than one option is required to be selected. 
Here is an HTML code example for a form with two checkboxes-

<form action="/cgi-bin/checkbox.py" method="POST" target="_blank"> 
<input type="checkbox" name="maths" value="on" /> Maths 
<input type="checkbox" name="physics" value="on" /> Physics 
<input type="submit" value="Select Subject" /> 
</form>

Given below is the checkbox.cgi script to handle the input given by web browser for checkbox button. 

# Import modules for CGI handling  
import cgi, cgitb   
# Create instance of FieldStorage  
form = cgi.FieldStorage()   
# Get data from fields 
if form.getvalue('maths'): 
   math_flag = "ON" 
else: 
   math_flag = "OFF"  
if form.getvalue('physics'): 
   physics_flag = "ON" 
else:
   physics_flag = "OFF"  
print ("Content-type:text/html") 
print() 
print ("<html>") 
print ("<head>") 
print ("<title>Checkbox - Third CGI Program</title>") 
print ("</head>") 
print ("<body>") 
print ("<h2> CheckBox Maths is : %s</h2>" % math_flag) 
print ("<h2> CheckBox Physics is : %s</h2>" % physics_flag) 
print ("</body>") 
print ("</html>") 
""")