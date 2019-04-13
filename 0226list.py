# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:41:40 2019

@author: student-03
"""
#List 串列
#可以存多型別資料(陣列僅能存單型別資料) 
#可以變換元素

income=[]
while True:
    salary=input("輸入數字")
    if salary!='q':
        income.append(salary)
    else:
        break
        
print(type(income))    #確認型別
print(type(income[0])) 
print(type(int(income[0]))) #轉型別

for i in range(len(income)):
    income[i]=int(income[i])
    
for i in income:
    i=int(i)
    
max(income)
sum(income) #加總

print("before %s"%(income))
income.insert(1,"250")
print(income)
income.pop(1)
print(income)
income.sort
print(income)

#income2=income.copy()
#print(income2)
#income2.clear()
#print(income2)
strToList="I love 台灣"
print(list(strToList))



