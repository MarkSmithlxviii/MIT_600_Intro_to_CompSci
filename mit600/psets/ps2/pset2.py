# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 11:07:07 2014

@author: Mark
"""

# find the lowest number abov which all numbers can be 
# expressed as a sum of the McNugget numbers 6, 9, and 20
# Answers question 1 problem set 2


for x in range (56):
    max_a = x/6+1
    max_b = x/9+1
    max_c = x/20+1
    for c in range (max_c):
        for b in range (max_b):
            for a in range (max_a):
                if 6*a+9*b+20*c-x == 0:
                    print x,'=6*',a,'+9*',b,'+20*',c                    