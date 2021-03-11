#!"E:\xampp\perl\bin\perl.exe"
print "Content-type: text/html\n\n";
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
