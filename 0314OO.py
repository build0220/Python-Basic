# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:46:26 2019

@author: student-03
"""

class Employee(object):
    
    def __init__(no,name,salary,dept):
        self.no=no
        self.name=name
        self.salary=salary
        self.dept=dept
    
    def showInfo(self):
        print("no:",self.no)
        print("no:",self.name)

