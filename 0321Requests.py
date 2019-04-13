# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:29:37 2019

@author: student-03
"""

import requests
url="http://www.hopax.com.tw/tc/index.asp"
#url="http://localhost"
page=requests.get(url)
page.encoding="utf8"
print(type(page))
print(page.text)