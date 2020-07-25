#coding:utf8

class UrlManager(object):
    
    def __init__(self):
        self.oldUrls = set()
        self.newUrls = set()

    def addNewUrl(self, url):
        if url is None:
            return
        if url not in self.oldUrls and url not in self.newUrls:
            self.newUrls.add(url)
    
    def addNewUrls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.addNewUrl(url)

    def hasNewUrl(self):
        return len(self.newUrls) != 0

    def getNewUrl(self):
        newUrl = self.newUrls.pop()
        self.oldUrls.add(newUrl)
        return newUrl
