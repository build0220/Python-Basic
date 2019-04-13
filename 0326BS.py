# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:55:23 2019

@author: student-03
"""
import requests
import bs4
url="http://192.168.0.16/"
#url="http://192.168.0.16/no.html"
try:
    page=requests.get(url)
    #soup=bs4.BeautifulSoup(page.text,"html.parser")
    soup=bs4.BeautifulSoup(page.text,"lxml")
    print(soup.prettify())
    print("擷取成功")
except Exception as error:
    print("error:",error)
    

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

try:
    htmldoc=requests.get("http://192.168.0.16")
    htmldoc.encoding="utf-8"
    soup=bs4.BeautifulSoup(htmldoc.text,"lxml")
    tagTitle=soup.title
    print(tagTitle.string)
    print(tagTitle.text)
    print("擷取成功")
except Exception as error:
    print("error:",error)
    

try:
    htmldoc=requests.get("http://192.168.0.16")
    htmldoc.encoding="utf-8"
    soup=bs4.BeautifulSoup(htmldoc.text,"lxml")
    aNode=soup.find_all('a')
    for e in aNode:
        print(e.string)
        print(e.text)
        print(e.getText())
        print(e.get("href"))
        print("擷取成功")
except Exception as error:
    print("error:",error)
    