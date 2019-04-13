# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:35:50 2019

@author: student-03
"""

#import os
import glob   #可用萬用字搜尋

for file in glob.glob('F:\\python'):
    print(file)
    
for file in glob.glob('F:\\python\\0314Sample\\*.*'):
    print(file)

for file in glob.glob('F:\\python\\0314Sample\\myfile.txt'):
    f=open(r'%s'%(file),'r')
    f.close()
   
    
fileName='F:\\python\\0314Sample\\myfile.txt'
with open(fileName,'r') as rf:
    print(rf.readlines())
    rf.close()

with open(fileName,'r') as rf:
    lineList=rf.readlines()
    for line in lineList:
        print(line)
    rf.close()
    
with open(fileName,'r') as rf:
    print(rf.read())
    rf.close()

lineStr=''
with open(fileName,'r') as rf:
    for line in rf:
       lineStr+=' '+line.rstrip()
    print(lineStr)
    rf.close()
    
#searchStr=input("輸入搜尋字:")
#index=lineStr.find(searchStr)
#if index>=0:
#    print("index:%d,char:%s"%(index,searchStr))
    
#import shutil
#
#shutil.copy(fileName,'newMyFile.txt')
#shutil.move('newMyFile.txt','.\\test')

import csv

with open('.\\0314Sample\\score.csv','r',encoding='utf8') as rf:
    score=[k for k in csv.reader(rf)]
    print(score)
    rf.close()
    
with open(".\\test\\newScore.csv","w",newline="") as wf:
    w=csv.writer(wf)
    w.writerows(score)
    
import xlwt
import xlrd

workBook=xlwt.Workbook()
worksheet=workBook.add_sheet("stuInfo")
worksheet.write(0,0,"No")
worksheet.write(0,1,"Name")
worksheet.write(0,2,"Tell")
workBook.save("stuInfo.xls")

readXlb=xlrd.open_workbook("stuInfo.xls")
readXls=readXlb.sheet_by_name("stuInfo")
print(readXls.cell(0,0).value)
print(readXls.cell(0,2).value)
print(readXls.cell(0,1).value)

import json
stu='{"數字":20,"名字":"愛台灣","英文":"Eng"}'
rJ=json.loads(stu)
print(type(rJ))
print(rJ["數字"])

for e in rJ:
    print(e,'->',rJ.get(e))
    
stuDic={"數字":20,"名字":"愛台灣","英文":"Eng"}
stuJson=json.dumps(stuDic)
print(type(stuJson))

rJ=json.loads(stuJson)
print(type(rJ))

i=10
try:
    print(i)
except:
    print("找不到 i")
    
try:
    print(j)
except:
    print("找不到 j")

#import os
#try:
#    os.mkdir("fff")
#    print("建立完成資料夾fff")
#except:
#    print("已存在此資料夾")
#    
#import os
#try:
#    os.rmdir("fff")
#    print("刪除資料夾fff")
#except:
#    print("不存在此資料夾")
    
import os
try:
    os.rmdir("fff")
    print("刪除資料夾fff")
except FileNotFoundError as e:
    print("other error")
    print(e)
except :
    print("不存在此資料夾")
finally:
    print("必定執行")
