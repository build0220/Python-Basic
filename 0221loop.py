# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:40:16 2019

@author: student-03
"""

coffee=["紅茶","奶茶","綠茶","咖啡"]
for e in coffee:
    print(e)
    
for c in "紅茶":
    print(c)

i=0
while i<10:
    i=i+1    
    if i==5:
        break
    print(i)

i=0
while i<10:
    i=i+1
    if i==5:
        continue
    print(i)
    

for e in range(2,30,2):
    print(e)
else:
    print("finish")
    
intList=[]
for e in range(10):
    intList.append(e)

print(intList)

myNum=[]
for e in range(1,6):
    num=e**2
    myNum.append(num)
print(myNum)  

for i in range(1,10):
    for j in range(1,10):
        k=i*j  
        print("%d*%d=%2d"%(i,j,k),end=" ")
        if (j%3)==0:
            print(end="\n")        
    print()