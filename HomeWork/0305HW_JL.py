# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:01:14 2019

@author: JL
"""
import random

class lotto(object):
    
    def __init__(self,allnumber,chooseCount):
        self.allnumber=allnumber
        self.chooseCount=chooseCount
        
    def lottoChoose(self):
        chooseNumberLst=list()
        allnumberLst=list(range(1,self.allnumber+1))
        while True:
            chooseNumber=random.choice(allnumberLst)
            chooseNumberLst.append(chooseNumber)
            allnumberLst.remove(chooseNumber)
            if self.chooseCount==len(chooseNumberLst):
                break
        return chooseNumberLst
    
    def bubbleSorted(self,iterable):
        new_list = list(iterable)
        list_len = len(new_list)
        for i in range(list_len-1):
            for j in range(list_len-1,i,-1):
                if new_list[j] < new_list[j-1]:
                    new_list[j],new_list[j-1] = new_list[j-1], new_list[j]
        return new_list
    
    def insertionSort(self,lst):
        for i in range(1, len(lst)):
            temp = lst[i]
            j = i - 1
            while j >= 0 and temp < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = temp
        return lst
        
if __name__ == '__main__':    
    allnumber=int(input("請輸入樂透號碼所有數量:"))
    chooseCount=int(input("請輸入樂透選取數量:"))
    lottoCls=lotto(allnumber,chooseCount)
    lottoNumberLst=lottoCls.lottoChoose()
    lottoNumberSort=lottoCls.insertionSort(lst=lottoNumberLst)
    print("本期樂透號碼:%s"%(lottoNumberSort))
