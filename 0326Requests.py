# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:04:16 2019

@author: student-03
"""
import requests
import re
#url="http://www.hopax.com.tw/tc/index.asp"
url="http://192.168.0.16/"
savePath="F://python"
page=requests.get(url)
page.encoding="utf8"
if page.status_code==requests.codes.ok:
    print("抓取成功")
else:
    print("抓取失敗")
print(type(page))
print(page.text)

try:
    with open(savePath + "//webCrawler.txt", "w", encoding = "utf-8") as wf:
        wf.write(page.text)
        print("儲存完成,路徑:%s"%(savePath))
except Exception as error:
    print(error)
finally:
    wf.close()
    
scStr=input("任意字串:")
if scStr in page.text:
    print("存在字串中")
else:
    print("不存在於字串中")
    
word=re.findall(scStr,page.text)
print(type(word))
if word!=None:
    print("網站內有 %s ,出現 %d 次"%(scStr,len(word)))
else:
    print("無此文字")
    