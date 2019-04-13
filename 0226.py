# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:41:40 2019

@author: student-03
"""

income=[]
while True:
    salary=input("輸入數字")
    if salary!='q':
        income.append(int(salary))
    else:
        break
        
print(type(income))    #確認類別
print(type(income[0])) 
print(type(int(income[0]))) #轉型

sum(income) #加總

