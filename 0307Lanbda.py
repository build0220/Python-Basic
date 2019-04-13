# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 18:51:31 2019

@author: student-03
"""

x=lambda x:x**2
x(2)

z=lambda x,y:x*y
z(2,5)

r=lambda x:1911+x 
r(107)

s=lambda x,y,z:str(1911+x)+"年"+str(y)+"月"+str(z)+"日"
print(s(108,3,5))

def myfunc(n):
    return lambda x:n*x

i=myfunc(2)
j=myfunc(3)
k=myfunc(5)

print(i(10))
print(j(10))
print(k(10))

def odd(x):
    if x%2!=0:
        return x
    else:
        return None
odd(10)

y=lambda x:x if x%2!=0 else None
y(8) 

#fliter
num=[5,8,9,11,32,25,48,52,17]
filterNum=filter(odd,num)

print("型別",type(filterNum))
print("物件",filterNum)

print(num)
numList=[item for item in filterNum]
print("型別",type(numList))
print(numList)

filterNum=list(filter((lambda x:x%2==0),num))
print(type(filterNum))
print(filterNum)
