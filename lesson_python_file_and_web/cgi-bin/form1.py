#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
message = form.getfirst("id_message")
print("Content-type: text/plain\n")
print(message)
