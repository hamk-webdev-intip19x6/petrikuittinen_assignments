from html.parser import HTMLParser
from urllib.request import urlopen
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=="a":
            for attr, value in attrs:
                if attr=="href":
                    print("link:", value)
    #def handle_endtag(self, tag):
    #    pass
    #def handle_data(self, data):
    #    pass

parser = MyHTMLParser()
with urlopen("https://yle.fi/uutiset") as f:
    data = f.read()
    parser.feed(data.decode("utf-8"))
