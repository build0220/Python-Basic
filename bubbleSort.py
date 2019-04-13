# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:39:04 2019

@author: student-03
"""

class bubbleSort(object):
    def __init__(self,x):
        self.x=list(x)
    def bubbleSort(self):
        for i in range(len(self.x)-1):
            for j in range(len(self.x)-1,i,-1):
                if self.x[j]<self.x[j-1]:
                    self.x[j],self.x[j-1]=self.x[j-1],self.x[j]
        return(self.x)
                    
if __name__=='__main__':
    x=[3,20,9,15,2]
    bubbleSortAg=bubbleSort(x)
    print("before:",x)
    print("after",bubbleSortAg.bubbleSort())