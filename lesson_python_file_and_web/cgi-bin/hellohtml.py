#!/usr/bin/python3

# import cgi
import cgitb
cgitb.enable()


def load_and_display(html):
    with open(html) as f:
        data = f.read()
        print("Content-type: text/html\n")
        print(data % vars(), end="")

        
load_and_display("hello.html")

