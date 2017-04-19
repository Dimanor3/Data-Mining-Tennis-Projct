from urllib.request import urlopen
from selenium import webdriver
from data_finder import DataFinder
from link_finder import LinkFinder
from domain import *
from general import *

class Spider:
    # Class variables (shared among all instances)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawl_file = ''
    data_storage_file = ''
    queue = set ()
    data_storage = set ()
    crawled = set ()

    def __init__ (self, base_url, project_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.queue_file = 'TennisPlayers.txt'
        Spider.crawl_file = Spider.project_name + '/crawled.txt'
        Spider.data_storage_file = project_name + '/storage.txt'
        self.boot ()
        self.crawl_page ('First spider', Spider.base_url)

    @staticmethod
    def boot ():
        create_project_dir (Spider.project_name)
        create_data_files (Spider.project_name)
        Spider.queue = file_to_set (Spider.queue_file)
        Spider.crawled = file_to_set (Spider.crawl_file)
        Spider.data_storage = file_to_set (Spider.data_storage_file)

    @staticmethod
    def crawl_page (thread_name, page_url):
        if page_url not in Spider.crawled:
            print (thread_name + ' crawling ' + page_url)
            print ('Queue ' + str (len (Spider.queue)) + ' | Crawled ' + str (len (Spider.crawled)))

            # Update temporary queue and crawl
            #Spider.add_data_to_storage (Spider.gather_data (page_url))
            Spider.gather_data(page_url)
            Spider.queue.remove (page_url)
            Spider.crawled.add (page_url)

            # Permanently add files
            Spider.update_files ()

    @staticmethod
    def gather_data (page_url):
        html_string = ''

        try:
            response = urlopen (page_url)

            if response.getheader ('Content-Type') == 'text/html':
                html_bytes = response.read ()
                html_string = html_bytes.decode ("utf-8")

            finder = DataFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print ('Error: cannot crawl page')
            return set ()
            pass


#     @staticmethod
#     def gather_links (page_url):
#         html_string = ''
# 	
#         try:
#             response = urlopen (page_url)
# 	
#             if response.getheader ('Content-Type') == 'text/html':
#                 html_bytes = response.read ()
#                 html_string = html_bytes.decode ("utf-8")
# 	
#             finder = LinkFinder (Spider.base_url, page_url)
#             finder.feed (html_string)
#         except:
#             print ('Error: cannot crawl page')
#             return set ()
# 	
#         return finder.page_links ()

    # Saves data to storage
    @staticmethod
    def add_data_to_storage(datas):
        for data in datas:
            if (data in Spider.data_storage):
                continue
            Spider.data_storage.add(data)

    @staticmethod
    def update_files ():
        set_to_file (Spider.crawled, Spider.crawl_file)
        set_to_file (Spider.data_storage, Spider.data_storage_file)