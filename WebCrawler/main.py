import threading
from queue import Queue
from spider import Spider
from domain import *
from demo import *

PROJECT_NAME = 'thesite'
HOMEPAGE = 'http://wishfie.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/onList.txt'
CRAWLED_FILE = PROJECT_NAME + '/whatsDone.txt'
NUMBER_OF_THREADS = 8
queue = Queue
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def crawl():
    queued_links = fileSetter(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' Links on list.')
        createJobs()


def createJobs():
    for links in fileSetter(QUEUE_FILE):
        queue.put(links)
        queue.join()
        crawl()
