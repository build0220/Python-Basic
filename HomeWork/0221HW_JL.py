# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:45:30 2019

@author: JL
"""

salary=int(input("請輸入年收入金額"))
taxLevels=[400000,1000000,1500000,3000000,salary] #稅金level
taxWeights=[0.05,0.1,0.2,0.5]   #稅金level對應稅金權重
k=0
tax=0
while salary>0:
    salary=salary-taxLevels[k]
    if salary<0:
        break
    tax=tax+salary*taxWeights[k]
    k=k+1
    
print("應繳稅為%s元"%(tax))