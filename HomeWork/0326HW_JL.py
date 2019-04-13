# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:59:35 2019

@author: JL
"""

import requests
import bs4 
#from urllib.request import urlopen
class crawler(object):
    def __init__(self,url,savePath):
        self.url=url
        self.savePath=savePath
    def crawler(self):
        try:
            h={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
            webCrawler=requests.get(url,headers=h)
            soup=bs4.BeautifulSoup(webCrawler.text,'lxml')
            with open(self.savePath + "//webCrawler.txt", "w", encoding = "utf-8") as wf:
                tdNode=soup.find_all('td')
                for e in tdNode:
                    #print(e.string)
                    wf.write(e.string)
                #wf.write(soup.prettify())
                wf.close()
                print("儲存完成,路徑:%s"%(self.savePath))
        except Exception as error:
            print(error)
if __name__=='__main__':
    url="http://www.tse.com.tw/exchangeReport/MI_5MINS_INDEX?response=html&date=20190327"
    savePath="d:"
    crawlerClass=crawler(url,savePath)
    crawlerClass.crawler()
