import requests
from bs4 import BeautifulSoup
from readability import Document

class HtmlDocument(object):
    
    def __init__(self, url):
        self.url = url;
        self.parseDocument()

    def parseDocument(self):

        # This is the URL that we want to extract the keywords from
        url = self.url
        response = requests.get(url)
        doc = Document(response.text)
        self.title = doc.title()

        soup = BeautifulSoup(doc.summary(), 'html.parser')
                
        paragraph_concat = ""
        for paragraph in soup.find_all('p'):
            paragraph_concat = paragraph_concat + paragraph.text + " "

        self.body = paragraph_concat

    def addUrl(self, url):
        self.url = url

    def getUrl(self):
        return self.url

    def getTitle(self):
        return self.title

    def getBody(self):
        return self.body

    

