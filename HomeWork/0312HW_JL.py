# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:48:23 2019

@author: JL
"""

class checkLotto:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def checkLottoNumber(self):
        happyNumber=[]
        for e in self.y:
            AgbinarySearch=Algorithms(self.x,e)
            mid=AgbinarySearch.binarySearch()
            if mid!=-1:
                happyNumber.append(self.x[mid])
        return happyNumber

class Algorithms:
    
    def __init__(self,x,d):
        self.x=x
        self.d=d
        
    def bubbleSort(self):
        lst=list(self.x)
        length=len(lst)
        for i in range(length-1):
            for j in range(i+1,length):
                #print('before',lst)
                if lst[i]>lst[j]:
                   lst[i],lst[j]=lst[j],lst[i] 
                #print('after',lst)
        return lst
    
    def binarySearch(self):
        lst=list(self.x)
        lower=0
        upper=len(lst)-1      
        while lower<=upper:
            mid=(lower+upper)//2
            if self.x[mid]<self.d:
                lower=mid+1
            elif self.x[mid]>self.d:
                upper=mid-1
            else:
                return mid
        return -1
        
class typeNumer:
    def __init__(self):
        None
    def typeNumber(self):
        try:
            myNumber=[]
            i=1
            while len(myNumber)<6:
                myNumber_temp=int(input("請依序輸入6個樂透號碼，我的第%s個樂透號碼:"%(i)))
                myNumber.append(myNumber_temp)
                i+=1
            print('完成號碼輸入')
            return myNumber
        except ValueError: 
            print('Error:請輸入阿拉伯數字')
            
if __name__=='__main__':
    lottoNumber=[3,45,22,6,1,14]
    typeNumer=typeNumer()
    myNumberLst=typeNumer.typeNumber() #我的樂透號碼
    Ag=Algorithms(lottoNumber,myNumberLst) 
    lottoNumberSort=Ag.bubbleSort()   #樂透號碼排序
    checkLotto=checkLotto(lottoNumberSort,myNumberLst) #check Lotto function 
    happyNumber=checkLotto.checkLottoNumber() #比對出中獎的號碼
    print("有中獎號碼如下",happyNumber)