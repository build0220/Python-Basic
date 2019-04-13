# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:59:52 2019

@author: JL
"""

class strCounty:
    
    def __init__(self,x):
        self.x=x
    
    def strCount(self):
        count=0
        for e in self.x:
            count+=1
        return count
        
if __name__=='__main__':
    with open('D:\\0314HW.txt','r',encoding="utf8") as rf:
        rfStr=''.join((rf.read()).split())
        rf.close()
    strCounty=strCounty(rfStr)
    print("總共有%d個字:"%(strCounty.strCount()))
        