# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:07:06 2019

@author: student-03
"""
import bubbleSort
class binarySearch(object):
    def __init__(self,x,d):
        self.x=x
        self.d=d
    def binarySearch(self):
        lower=0
        upper=len(self.x)-1
        while lower<=upper:
            mid=(lower+upper)//2
            if self.x[mid]<self.d:
                lower=mid+1
            elif self.x[mid]>self.d:
                upper=mid-1
            else:
                return mid
        return -1
    
if __name__=='__main__':
    x=[3,20,9,15,2]
    bubbleSortAg=bubbleSort.bubbleSort(x)
    xSort=bubbleSortAg.bubbleSort()
    d=15
    binarySearchAg=binarySearch(xSort,d)
    print(xSort)
    print(binarySearchAg.binarySearch())
        