# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:50:47 2019

@author: JL
"""
import numpy as np
import matplotlib.pyplot as plt

class gridDesc(object):
    
    def __init__(self, wInit,epochs,lr):
        self.w = wInit #初始權重
        self.epochs=epochs #迭代次數
        self.lr=lr #學習率
        self.pltRange = np.arange(-10.0, 10.0, 0.01)
        
    def func(x): #目標函數
        return np.square(x+3)
    
    def dfunc(x): #目標函數微分
        return 2*(x+3)
    
    def GD(self): #梯度下降
        try:
            ws = np.zeros(self.epochs+1)
            ws[0]=self.w
            for i in range(self.epochs):         
                dw = gridDesc.dfunc(self.w)              
                v = - dw * self.lr        
                self.w += v        
                ws[i+1] = self.w  
        except Exception as err:
            print(err)
        finally:    
            return ws
    
    def pltGD(self):
        try:
            x=gridDesc.GD(self)
            plt.plot(self.pltRange, gridDesc.func(self.pltRange), c='b')
            plt.plot(x, gridDesc.func(x), c='r', label='lr={}'.format(self.lr))    
            plt.scatter(x, gridDesc.func(x), c='r')    
            plt.legend()
            plt.show()
        except Exception as err:
            print(err)

if __name__=='__main__':
    wInit = int(input("初始權重(請輸入數字):"))    
    epochs = int(input("迭代次數(請輸入數字):")) 
    lr = float(input("學習率(建議 0~1 區間):"))
    gD=gridDesc(wInit,epochs,lr)
    gD.pltGD()
    
    
    
    
