# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:59:35 2019

@author: JL
"""

import requests
import bs4 
import csv
import os
import time
import matplotlib.pyplot as plt
from collections import Counter

class crawler(object):
    def __init__(self,url,savePath,sleepSecond,times):
        self.url=url                    #網址
        self.savePath=savePath          #存檔路徑
        self.sleepSecond=sleepSecond   #間隔幾秒抓取
        self.times=times                #總共抓取幾次

    def crawler(self): #定時定次數爬蟲
        try:
            times_temp=1
            while times_temp<(self.times+1):
                h={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
                webCrawler=requests.get(self.url,headers=h) #爬蟲並伪裝成chrome
                #webCrawler.encoding="utf-8"
                soup=bs4.BeautifulSoup(webCrawler.text,'lxml') 
                bingo=soup.select('.contents_box01')
                yBall=bingo[0].find_all('div',{"class":"ball_tx ball_yellow"})
                bingoNumber=[]
                if not os.path.exists(self.savePath + '//bingo.csv'): #判斷是否存在此檔案
                    with open(self.savePath + '//bingo.csv', 'w') as wf:
                        wf.close
                for i in range(len(yBall)): #將字串丟入至list
                        luckyNumber=yBall[i].text
                        bingoNumber.append(luckyNumber)
                with open(self.savePath + '//bingo.csv','a+', encoding='utf8',newline='') as wf:
                    writer = csv.writer(wf)
                    writer.writerow(bingoNumber)
                    wf.close
                    print("第%s次抓取資料"%(times_temp))
                    times_temp=times_temp+1
                time.sleep(self.sleepSecond) #時間間隔
            print("全部抓取完成，儲存完成,路徑:%s"%(self.savePath))
        except Exception as error:
            print(error)
            
class pltBar(object): #畫長條圖
    def __init__(self,noList):
        self.noList = noList
        
    def pltBar(self):
        count=Counter(self.noList[0])  
        for i in range(1,len(self.noList),1): #計數
            count=count+Counter(self.noList[i])
        labels, values = zip(*count.items())
        plt.figure(figsize=(15,5))
        plt.bar(labels, values)
        plt.show()
        return count
        
if __name__=='__main__':
    #定時定次抓取樂透彩號碼，並統計號碼出現次數劃出長條圖
    url="http://www.taiwanlottery.com.tw/"
    savePath="d:"
    sleepSecond=int(input("請輸入間隔幾秒抓1次:"))
    times=int(input("請輸入總共要抓幾次:"))
    crawlerClass=crawler(url,savePath,sleepSecond,times)
    crawlerClass.crawler()
    with open(savePath + '//bingo.csv', 'r',encoding="utf8") as rf:
        noList=[e for e in csv.reader(rf)]
    bingoBar=pltBar(noList)
    bingoBar.pltBar()