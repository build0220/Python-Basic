# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:34:57 2019

@author: student-03
"""

lang={}  #字典
print(type(lang))
langs={"C","R","python"} #set 集合，無順序、可儲存多型、無重複、有key無值

#走訪元素
for e in langs:
    print(e)
    
langs.add("java")
print(langs)
langs.add("C")
print(langs)
langs.update([1997,2008]) #家ㄖㄨ
print(langs)
langs.remove("C") #刪除
print(langs)
langs.remove("C") #刪除 error，因為langs 無此值
langs.discard("C") #discard 刪除，避免無此資料錯誤

#set 函數
langs=set()
print(type(langs))
langs.update({"C","R","python"})

#update與add差別
web=("HTML","CSS","JS")
api=["BS","W3C"]

langs.add(web)
print(langs)
langs.update(api)
print(langs)

#練習唯一值
location=["高雄","台北","新竹","台中","高雄","嘉義","台北","台南","屏東","嘉義"]
locationSet=set()
locationSet.update(location)
print(locationSet)

#set 運算
Math={"A","B","C","D","E"}
Eng={"C","A","E","G"}
allStudyStudent=Math&Eng
print(allStudyStudent)
OneStudyStudent=(Math-Eng)|(Eng-Math)
print(OneStudyStudent)

#difference 函數
Math.difference(Eng)

#symmetric
sym=Math^Eng
print(sym)
Math.symmetric_difference(Eng) #同 ^

#練習
firstPeople={2,7,4,9,8}
secondPeople={2,4,7,9,8}
thirdPeople={2,7,4,9,8}

firstPeople==secondPeople
firstPeople==thirdPeople
secondPeople==thirdPeople

firstPeople!=secondPeople
firstPeople!=thirdPeople
secondPeople!=thirdPeople

#指定
Math={"A","B","C","D","E"}
Eng=Math                     #指定相同記憶體位置
Math.add(11)
print(Math)
print(Eng)

Math={"A","B","C","D","E"}
Eng=Math.copy()              #新增物件(產生記憶體位置)           
Math.add(11)
print(Math)
print(Eng)
