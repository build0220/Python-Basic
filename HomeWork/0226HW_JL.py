# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:51:05 2019

@author: JL
"""

import numpy as np
cost=[]
i=1
while True:
    costInput=input("輸入廣告費用，按q輸入完畢:")
    if costInput!="q":
            print("第%s筆廣告費用:%s"%(i,costInput))
            i=i+1
            cost.append(int(costInput))
    else:
        break
    
print("廣告總花費%s"%(sum(cost)))
print("廣告花費平均%s"%(np.mean(cost)))
