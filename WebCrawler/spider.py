from urllib.request import urlopen
from finder import Finder
from demo import *


class Spider:

    projectName = ''
    baseURL = ''
    domain = ''
    onQueue = ''
    itsDone = ''
    queue = set()
    crawled = set()


    def __init__(self, projectName, baseURL, domain):
        Spider.projectName = projectName
        Spider.baseURL = baseURL
        Spider.domain = domain
        Spider.onQueue = Spider.projectName + '/onList.txt'
        Spider.itsDone = Spider.projectName + '/whatsDone.txt'
        self.boot()
        self.crawlPage('First Spider', Spider.baseURL)


    def boot(self):
        createDirectory(Spider.projectName)
        createDataFiles(Spider.projectName, Spider.baseURL)
        Spider.queue = fileSetter(Spider.onQueue)
        Spider.crawled = fileSetter(Spider.itsDone)
