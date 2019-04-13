# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:59:39 2019

@author: JL
"""
import requests
#from bs4 import BeautifulSoup
#from urllib.request import urlopen
class crawler(object):
    def __init__(self,url,savePath):
        self.url=url
        self.savePath=savePath
    def crawler(self):
        try:
            webCrawler=requests.get(self.url)
            with open(self.savePath + "//webCrawler.txt", "w", encoding = "utf-8") as wf:
                wf.write(webCrawler.text)
                wf.close()
                print("儲存完成,路徑:%s"%(self.savePath))
        except Exception as error:
            print(error)
if __name__=='__main__':
    url="https://tw.yahoo.com/"
    savePath="d:"
    h={}
    crawlerClass=crawler(url,savePath)
    crawlerClass.crawler()
    
