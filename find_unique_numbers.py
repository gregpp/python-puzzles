# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:17:35 2020

@author: GP
This script find the elements which occur exactly once in the input list
"""

def find_unique_numbers(numbers):
    
    d = {}
    l = []
    
    for n in numbers:
        if n in d:
            d[n]+=1
        else:
            d[n]=1
    
    for n in d:
        if d[n] == 1:
            l.append(n)
        else:
            pass
    return l

print (find_unique_numbers([1,2,3,4,5,5]))
