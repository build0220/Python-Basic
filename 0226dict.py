# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:43:46 2019

@author: student-03
"""

#dict 大括號建立 {"key",value}
dictHello={"a":100,"b":50,"c":60}
#dict dict加List建立 dict(["key",value])
dictHello=dict([["a",100],["b",50],["c",60],["d",70]])
#dict dict加List建立 dict(key=value)
dessert=dict(a=100,b=50,c=80)

new={"d":60}
dir(dictHello)
print(dictHello)
print(dictHello.get("a"))
dictHello.update(new)
print(dictHello)
new={"d":50}
dictHello.update(new)
print(dictHello)

print(dictHello['f']) #不存在返回錯誤訊息
print(dictHello.get('f')) #不存在返回None，不會有錯誤訊息
dictHello.clear()  #清空字典
print(dictHello)
del dictHello  #刪除字典
print(dictHello)

dessert={"a":100,"b":50,"c":80}
dessert=dict(a=100,b=50,c=80)
for e in dessert:
    print(e,dessert[e])

dessert=dict(A=dict(a=195),B=dict(b=160))

