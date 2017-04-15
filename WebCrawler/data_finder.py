from html.parser import HTMLParser
from urllib import parse

class DataFinder (HTMLParser):
    def __init__ (self, page_url):
        super ().__init__ ()
        self.page_url = page_url
        self.name = set ()

    def handle_starttag (self, tag, attrs):
        if tag == 'span':
            for (attribute, value) in attrs:
                print (attribute + " " + value)

    def error (self, message):
        pass