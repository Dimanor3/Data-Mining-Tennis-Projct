from html.parser import HTMLParser
from selenium import webdriver
from bs4 import BeautifulSoup

class DataFinder (HTMLParser):
    def __init__ (self, base_url, page_url):
        super ().__init__ ()
        self.base_url = base_url
        self.page_url = page_url
        self.name = set ()

    def handle_starttag (self, tag, attrs):
        if tag == 'span':
            for (attribute, value) in attrs:
                print (attribute + " " + value)
        else:
            print("null")
              
    def page_links (self):
        return self.links  

    def error (self, message):
        pass
    