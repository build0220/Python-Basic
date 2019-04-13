# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:17:13 2019

@author: student-03
"""

class seqSearch(object):
    def __init__(self,x,d):
        self.d=d
        self.x=x
        
    def seqSearch(self):
        lst=[0]*(len(self.x)+1)
        for i in range(1,len(lst)):
           lst[i]=self.x[i-1]
        lst[0]=self.d
        i=len(x)
        while lst[i]!=lst[0]:
            i-=1
        return i-1
if __name__=='__main__':
    x=[3,20,9,15,2]
    d=15
    seqSearchAg=seqSearch(x,d)
    print("before:",x)
    print("after", seqSearchAg.seqSearch())
