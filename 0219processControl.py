# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

age=int(input("請輸入您的年齡:"))
if age>18:
    print("限制級")
elif age>15:
    print("15輔導級")
elif age>12:
    print("12輔導級")
elif age>6:
    print("保護級")
else:
    print("普通級")