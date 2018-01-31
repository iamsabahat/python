from html.parser import HTMLParser
from urllib import parse


class Finder(HTMLParser):

    def __init__(self, baseURL, pageURL):
        super().__init__()
        self.baseURL = baseURL
        self.pageURL = pageURL
        self.links = set()

    def errorFinder(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    urlLinker = parse.urljoin(self.baseURL, value)
                    self.links.add(urlLinker)

    def pageLink(self):
        return self.links
