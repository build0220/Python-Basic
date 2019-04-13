# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:57:21 2019

@author: JL
"""
import random
import math

class cardsChoose(object):
    
    def __init__(self,playerNumber):
            self.playerNumber=playerNumber

    def cardsShuffle(self):    
        #s-spades黑桃h-hearts紅桃d-diamonds方塊c-clubs梅花
        cardtype=["S","H","D","C"]
        cardNum=list(range(1,14))
        cards=list()
        for e in cardtype:
            for ee in cardNum:
                cards.append(e+str(ee))
        random.shuffle(cards)
        j=0
        onePersonCradsCount=math.floor(52/self.playerNumber)
        for i in range(self.playerNumber+1):
            if i<self.playerNumber:
                locals()["player%s"%(i+1)]=cards[j:j+onePersonCradsCount]
                print("Player%s:"%(i+1),locals()["player%s"%(i+1)])
                j=j+onePersonCradsCount
            else:
                print("other:",cards[j:])
        
if __name__ == '__main__':
    playerNumber=int(input("請輸入玩家人數:"))
    playerCardsChoose=cardsChoose(playerNumber)
    playerCardsChoose.cardsShuffle()
