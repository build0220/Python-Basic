# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:15:01 2019

@author: student-03
"""

import greeting
from greeting import afternoon
import fruit as ft
import random as r
#greeting 引用 函數
greeting.afternoon()
afternoon()

#greeting 引用 變數
print(greeting.empDict)
print(ft.apple(100))
print(ft.orange(200))

#內建模組
import sys
import platform as pm
import time as t

for p in sys.path:
    print(f"'{p}'")

print(pm.system())
print(pm.version())
print(pm.python_version)

print(t.time()) #百萬分之一秒(微渺)，1970為開始
#目前 微軟 1900,other 1970
tt=t.localtime()
print(tt)
print("%4d年%2d月%2d日"%(tt.tm_year,tt.tm_mon,tt.tm_mday))

r.random() #福點數
r.randint(1,10)#整數
r.uniform(1,2) #某範圍
game="大家恭喜發財"
print(r.choice(game))
for i in range(5): 
    print(r.sample(game,2))
