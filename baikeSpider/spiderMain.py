# coding:utf8

import urlManager, htmlDownloader, htmlParser, htmlOutputer

class SpiderMain(object):
    def __init__(self):
        self.urls = urlManager.UrlManager()
        self.downloader = htmlDownloader.HtmlDownloader()
        self.parser = htmlParser.HtmlParser()
        self.outputer = htmlOutputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.addNewUrl(rootUrl)
        while self.urls.hasNewUrl():
            #try :
                newUrl = self.urls.getNewUrl()
                print('craw %d:%s'%(count,newUrl))
                htmlContent = self.downloader.download(newUrl)
                newUrls, newData = self.parser.parser(newUrl, htmlContent)
                self.urls.addNewUrls(newUrls)
                self.outputer.collectData(newData)

                if count == 5:
                    break
                count = count + 1
            #except:
             #   print("craw failed")
        self.outputer.outputHtml()

if __name__=="__main__":
    rootUrl = "https://baike.baidu.com/item/Python/407313"
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)
