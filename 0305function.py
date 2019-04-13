# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 20:26:49 2019

@author: student-03
"""

#函數-無參數無回傳
def Fun():
    print("無參數無回傳")
    
#函數-有參數無回傳
def paramterFun(x):    
    print(x)
    
#函數-無參數有回傳
def returnFun():
    return "無參數有回傳"

#函數-有參數有回傳

def paramterReturnFun(x):
    return x

#預設參數
def parameterDefaultFun(x="預設x"):
    return x



Fun()
paramterFun("有參數無回傳")
print(returnFun())
print(paramterReturnFun("有參數有回傳"))
print(parameterDefaultFun())

#練習BMI
def bmi(x,y):
    #BMI=(x/100)/(y/100)**2
    BMI=round((x/100)/pow(y/100,2))
    return BMI

print(bmi(60,180))
print(bmi(y=180,x=60)) #參數名代替位置順序

print(bmi(60,180))
print(bmi(y=180,x=60)) #參數名代替位置順序

#練習 多重回傳
def MutiReturn(x,y):
    add=x+y
    diff=x-y
    pro=x*y
    div=x/y
    return add,diff,pro,div

a,b,c,d=MutiReturn(4,6)

#回傳型態比較
print(type(MutiReturn(4,6)))
print(type(bmi(4,6)))
print(type(Fun))
print(type(Fun()))
print(type(paramterFun(x=1))) #資料型態notype,None 相當Null

#練習宣告函數回傳字典
def dictFun(x,y):
    diction={"id":x,"name":y}
    return diction
Info=dictFun("1","John")
for e in Info:
    print(Info.get(e))
    
print(type(Info))


#未定參數數量
def anyParameterFuc(*name):
    for e in name:
        print(e)
    
anyParameterFuc("恰恰","林書豪","王建民")
print(type(anyParameterFuc("恰恰","林書豪","王建民"))) #資料型態notype,None 相當Null

#內建字串函數
song=["I","love","python"]
print(song)
strSong=" ".join(song) #空白串接
print(strSong)

strSlipt=strSong.split(" ") #以空白切割
print(strSlipt)

strSalad="I love Saled"
strSalad2=strSalad.strip()
print(strSalad)
print(type(strSalad))
print(type(strSalad2))
