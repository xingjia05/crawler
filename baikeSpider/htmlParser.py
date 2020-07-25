#coding:utf8
from bs4 import BeautifulSoup
import re
from urllib.parse import parse_qsl, urljoin, urlparse

class HtmlParser(object):

    def getNewUrls(self, pageUrl, soup):
        newUrls = set()
        links = soup.find_all('a', href=re.compile(r"/item/\w+/\d+"))
        for link in links:
            newUrl = link['href']
            newFullUrl = urljoin(pageUrl, newUrl)
            newUrls.add(newFullUrl)
        return newUrls

    def getNewData(self, pageUrl, soup):
        resData = {}

        resData['url'] = pageUrl
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        titleNode = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        resData['title'] = titleNode.getText()

        #<div class="lemma-summary"
        summaryNode = soup.find('div', class_="lemma-summary")
        resData['summary'] = summaryNode.getText()
        return resData

    def parser(self, pageUrl, htmlContent):
        if pageUrl is None or htmlContent is None:
            return
        
        soup = BeautifulSoup(htmlContent, "html.parser")

        newUrls = self.getNewUrls(pageUrl, soup)
        newData = self.getNewData(pageUrl, soup)
        return newUrls, newData

