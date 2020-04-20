# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:53:31 2020

@author: GP
"""
import statistics

def class_grades(students):
    """
    

    Parameters
    ----------
    students : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    d = {}
    
    for s in students:
        if s[1] in d:
            d[s[1]].append(s[2])
            #d[s[1]] = d[s[1]] + [s[2]]
        else:
            d[s[1]] = [s[2]]
    
    l = []
    for k in d:
        l.append([k,statistics.median(d[k])])
    
    return l

students=[["Ana Stevens","1a",5],["Mark Stevens","1a",4],
          ["Jon Jones","1a",3],["Bob Kent","1b",4],["Bob Kent","1c",2]]

print (class_grades(students))
