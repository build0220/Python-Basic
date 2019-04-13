# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:54:30 2019

@author: student-03
"""
import requests

url="http://192.168.0.16/"
#url="http://192.168.0.16/no.html"
try:
    page=requests.get(url)
    page.raise_for_status()
    print(page.text)
    print("擷取成功")
except Exception as error:
    print("error:",error)


#偽裝成Browser
h={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64)\
   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

try:
    page2=requests.get(url,headers=h)
    page2.raise_for_status()
    print(page.text)
    print("擷取成功")
except Exception as error:
    print("error:",error)