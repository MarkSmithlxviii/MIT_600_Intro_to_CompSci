# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 11:07:07 2014

@author: Mark
"""

# find the lowest number abov which all numbers can be 
# expressed as a sum of the McNugget numbers 6, 9, and 20

McTest = 1
McNumber = 1
notMcNumber = 1
stop = 200
McNuggets = (13, 29, 40)
while (McNumber - notMcNumber) <= McNuggets[0] and (
    McNumber < stop):
    max_a = McTest / McNuggets[0] + 2
    max_b = McTest / McNuggets[1] + 2
    max_c = McTest / McNuggets[2] + 2
    for c in range (max_c):
        for b in range (max_b):
            for a in range (max_a):
                if McTest - (McNuggets[0]*a+McNuggets[1]*b+
                             McNuggets[2]*c) == 0:
                    print McTest,'=',McNuggets[0],'*',a,\
                    '+',McNuggets[1],'*',b,'+', McNuggets[2],'*',c                    
                    McNumber = McTest
                elif a == max_a - 1  and b == max_b - 1 and(
                      c == max_c - 1) and McNumber != McTest:
                          notMcNumber = McTest
    McTest += 1   
if (McNumber - notMcNumber) >= McNuggets [0]and (
    McNumber < stop):
    print 'The largest number of McNuggets that cannot be \
    bought in exact quanity is:', notMcNumber
else:
    print 'Range to small to definitively calculate largest \
non-McNugget number'