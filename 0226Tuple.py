# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:49:19 2019

@author: student-03
"""

#Tuple 元組
#可以存多型別資料
#不可變換元素

tupleHello=(1,"我",2.6,"He")
print(tupleHello[1])

print(type(tupleHello))
tupleHelloToList=list(tupleHello)
print(type(tupleHelloToList))


city=["雲林","台南","嘉義","屏東"] #zip 迭代
cityCode=[700,600,500,300]
cityLsitZip=zip(city,cityCode)
print(cityLsitZip)
print(list(cityLsitZip))
