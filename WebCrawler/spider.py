from urllib.request import urlopen
from finder import Finder
from demo import *
from domain import *

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

    @staticmethod
    def boot(self):
        createDirectory(Spider.projectName)
        createDataFiles(Spider.projectName, Spider.baseURL)
        Spider.queue = fileSetter(Spider.onQueue)
        Spider.crawled = fileSetter(Spider.itsDone)


    @staticmethod
    def crawlpage(thread_name, pageURL):
        if pageURL not in Spider.crawled:
            print(thread_name + 'Spider is now crawling => ' + pageURL)
            print('Queue : ' + str(len(Spider.queue)) + ' | Crawled : ' + str(len(Spider.crawled)))
            Spider.addLinksToList(Spider.gatherLinks(pageURL))
            Spider.queue.remove(pageURL)
            Spider.crawled.add(pageURL)
            Spider.update_files()


    @staticmethod
    def gatherLinks(pageURL):
        html_string = ''
        try:
            response = urlopen(pageURL)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finderObject = Finder(Spider.baseURL, pageURL)
            finderObject.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finderObject.pageLink()


    @staticmethod
    def addLinksToList(links):
        for urls in links:
            if(urls in Spider.queue) or (urls in Spider.crawled):
                continue
            if Spider.domain != get_domain_name(urls):
                continue
            Spider.queue.add(urls)

    @staticmethod
    def update_files():
        setFile(Spider.queue, Spider.onQueue)
        setFile(Spider.crawled, Spider.itsDone)
