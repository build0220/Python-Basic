# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:25:18 2019

@author: student-03
"""
import os

print(os.getcwd())

print(os.path.abspath('.'))
print(os.path.abspath('..'))

print(os.path.relpath('F:/python/0312IO.py'))
print(os.path.relpath('F:/python'))

print(os.path.getsize('0312IO.py'),'bytes')

print(os.path.isfile('0312IO.py'))
print(os.path.isdir('0312IO.py'))

print(os.path.exists('0312IO.py'))

print(os.path.isabs('F:/python'))
print(os.path.isabs('0312IO.py'))
print(os.path.isabs('python'))


song="i love python and ML\n"
wf=open('test.txt','w')
wf.write(song)
wf.close()

song="遊戲"
wf=open('test.txt','a') #附寫在後面
wf.write(song)
wf.close()

rf=open('test.txt','r')
for e in rf:
    print(e)
rf.close()

with open('test.txt','r') as rf:
    for e in rf:
        print(e)
rf.close()

def createFile():
    if os.path.exists('myfile.txt'):
        os.rmove('myfile.txt')
        print('已完成刪除 myfile.txt')
    else:
        print('無此檔案')
        
    if not os.path.isdir('test'):
        print('資料夾已存在')
    else:
        os.mkdir('test')
    
    if os.path.isdir('test2'):
         os.rmdir('test2')
    else:
        os.mkdir('test2')
        
createFile()
        
