# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:38:19 2019

@author: student-03
"""

import keyword
keywords=['is','else','None','NONE','NULL']
for e in keywords:
    print(e,keyword.iskeyword(e))
keyword.kwlist    
