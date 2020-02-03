#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()


def load_and_display(html):
    with open(html) as f:
        data = f.read()
        print("Content-type: text/html\n")
        print(data % vars(), end="")

        
def save(message):
    with open("results.txt", "a") as f:
        f.write(message+"\n")

        
form = cgi.FieldStorage()
if "id_message" in form:
    message = form.getfirst("id_message")
    save(message)
    load_and_display("thanks.html")
else:
    load_and_display("form.html")
    
