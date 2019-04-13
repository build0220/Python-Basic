# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:22:37 2019

@author: student-03
"""

nameList=["aaa","bbb","ccc","ddd","eee"]
print(nameList)
salaryList=[100,200,300,400,500]
print(salaryList)

emp=[["aaa",100],["bbb",200],["ccc",300],["ddd",400],["eee",500]]

print(emp)
print(emp[3][1])

for e in emp:
    for e1 in e:
        print(e1,end=" ")
    print(end="\n")
print("員工有%d人"%(len(emp)))

for i in range(len(emp)):
    for j in range(len(emp[i])):
        print(emp[i][j],end=" ")
    print()

print("aaa" in nameList)
print(nameList[1:3])




