from data_finder import data_finder
from general import *

class Spider:
    # Class variables (shared among all instances)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    queue_update = ''
    crawl_file = ''
    # data_storage_file = ''
    queue = set ()
    data_storage = set ()
    crawled = set ()
    # update_queue = 0

    def __init__ (self, base_url, project_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.queue_file = 'TennisPlayers.txt'
        # Spider.queue_update = Spider.project_name + '/queueUpdate.txt'
        Spider.crawl_file = Spider.project_name + '/crawled.txt'
        Spider.data_storage_file = Spider.project_name + '/storage.txt'
        self.boot ()
        self.crawl_page ('First spider', Spider.base_url)

    @staticmethod
    def boot ():
        create_project_dir (Spider.project_name)
        create_data_files (Spider.project_name)
        Spider.queue = file_to_set (Spider.queue_file)
        # if file_to_set (Spider.queue_update):
        #     Spider.update_queue = int (list (file_to_set (Spider.queue_update))[0])
        Spider.crawled = file_to_set (Spider.crawl_file)
        Spider.data_storage = file_to_set (Spider.data_storage_file)

    @staticmethod
    def crawl_page (thread_name, page_url):
        if page_url not in Spider.crawled:
            print (thread_name + ' crawling ' + page_url)
            print ('Queue ' + str (len (Spider.queue)) + ' | Crawled ' + str (len (Spider.crawled)))# + ' | Queue Update ' + str (Spider.update_queue))

            # Update temporary queue and crawl
            #Spider.add_data_to_storage (Spider.gather_data (page_url))
            Spider.data_storage.add (Spider.gather_data(page_url))
            Spider.queue.remove (page_url)
            # Spider.update_queue += 1
            Spider.crawled.add (page_url)

            # Permanently add files
            Spider.update_files ()

    @staticmethod
    def gather_data (page_url):
        finder = data_finder (Spider.base_url, page_url)

        temp = finder.gatherData ()

        return temp

    # Saves data to storage
    @staticmethod
    def add_data_to_storage(datas):
        for data in datas:
            if (data in Spider.data_storage):
                continue
            Spider.data_storage.add(data)

    @staticmethod
    def update_files ():
        # if Spider.update_queue == 50:
        #     set_to_file (Spider.queue, Spider.queue_file)
        #     Spider.update_queue = 0
        # set_to_file_int (str (Spider.update_queue), Spider.queue_update)
        set_to_file (Spider.crawled, Spider.crawl_file)
        set_to_file (Spider.data_storage, Spider.data_storage_file)