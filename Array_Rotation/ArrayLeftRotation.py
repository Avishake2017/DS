# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:41:37 2020

@author: Avishake
"""

def ArrayRotation(givenList,numberOfRotations):
    for i in range(0,n):
        firstEle = givenList[0]
        
        for j in range(0,len(givenList)-1):
            givenList[j] = givenList[j+1]
        
        givenList[len(givenList) - 1] = firstEle
    
    return givenList

if __name__ == '__main__':
    '''A Demo List for example. You can take yours'''
    givenList = [1,2,3,4,5]
    '''Number of Rotations to be performed'''
    n = 3 
    
    requiredList = ArrayRotation(givenList,n)
    print(requiredList)