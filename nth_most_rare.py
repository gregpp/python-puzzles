# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:34:09 2020

@author: GP
This script finds the n-th most rare element in the input list
"""


def nth_most_rare(elements, n):
    """
    :param elements: (list) List of integers.
    :param n: (int) The n-th element function should return.
    :returns: (int) The n-th most rare element in the elements list.
    """
    s = set(elements)
    if n > len(s) or n <= 0:
        print ("N must be a positive integer not great than number\
               of unique elements in a list")
        return None
    d = {}
    
    for e in elements:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    
    x = sorted(d.items(),key = lambda x: x[1], reverse = False)
    #print (x)
    
    return x[n-1][0]

print(nth_most_rare([1,1,2,2,2,3,3,3,3], 3))
