import cgi
import cgitb;

print "Content-Type: text/html"

arguments = cgi.FieldStorage()
for argument in arguments.keys():
	print "Argument: " + arguments[i]
	print "Value: " + arguments[i].value