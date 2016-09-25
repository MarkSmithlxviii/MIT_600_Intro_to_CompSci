# -*- coding: utf-8 -*-
"""
MIT 6.00 introduction to Computer Science and Programming

Problem Set 1 Problem 1

A program to calculate the 1000th prime

Created on Sun Sep 11 03:21:40 2016

@author: marka
"""

from math import log

possiblePrime = 3  # start at 3 first odd prime
primeCounter = 1   # 1 because the program does not check 2 for primeness
primeLogSum = 0

while primeCounter < 222 :
   factor = 2
   notprime = 0
   while factor < (possiblePrime**0.5)+1 and notprime == 0:
       if possiblePrime % factor == 0 :
           notprime = 1
           possiblePrime += 2
       if factor > possiblePrime**0.5 and notprime == 0:
           primeCounter +=1
           factor = possiblePrime
           primeLogSum += log(possiblePrime)
           possiblePrime +=2
       factor += 1
print("The {0}th prime is {1}".format(primeCounter, possiblePrime))
print('The sum of the logs of the primes smaller than {0} is {1}'.format(possiblePrime, round(primeLogSum,1)))
print('The ratio of the sum of the logs over {0} is: '.format(possiblePrime))
print(primeLogSum / possiblePrime)