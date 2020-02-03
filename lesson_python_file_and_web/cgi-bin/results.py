#!/usr/bin/python3

import cgi
import html
import cgitb
cgitb.enable()


def load_and_display(html, param_dict={}):
    with open(html) as f:
        data = f.read()
        print("Content-type: text/html\n")
        print(data % param_dict, end="")

        
def load_results(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        all_lines = html.escape("\n".join(lines))
        return all_lines.replace("\n", "<br>")
    


results = load_results("results.txt")
load_and_display("results.html", vars())

