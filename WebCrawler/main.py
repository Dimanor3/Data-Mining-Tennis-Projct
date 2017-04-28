#!/usr/bin/env python3

import threading
from queue import Queue
from spider import Spider
from general import *

PROJECT_NAME = 'itftennis'
BASE_URL = 'http://www.itftennis.com/juniors/players/player/profile.aspx?PlayerID=100148392'
BASE_URL_TEST_DATA = 'http://www.itftennis.com/juniors/players/player/profile.aspx?playerid=100279265'
QUEUE_FILE = 'TennisPlayers.txt'
QUEUE_UPDATE = PROJECT_NAME + '/queueUpdate.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
DATA_STORAGE_FILE = PROJECT_NAME + '/storage.txt'
NUMBER_OF_THREADS = 1
queue = Queue ()
Spider (BASE_URL, PROJECT_NAME)

# Create worker threads (will die when main exists)
def create_spiders ():
    for _ in range (NUMBER_OF_THREADS):
        t = threading.Thread (target = work)
        t.daemon = True
        t.start ()

# Do the next job in the queue
def work ():
    while True:
        url = queue.get ()
        Spider.crawl_page (threading.current_thread().name, url)
        queue.task_done ()

# Each queued link is a new job
def create_jobs ():
    for link in file_to_set (QUEUE_FILE):
        queue.put (link)

    queue.join ()

    crawl ()

# Check if there are items in the queue, if so crawl them
def crawl ():
    queued_links = file_to_set (QUEUE_FILE)

    if len (queued_links) > 0:
        print (str (len (queued_links)) + ' links in the queue')
        create_jobs ()

create_spiders ()
crawl ()