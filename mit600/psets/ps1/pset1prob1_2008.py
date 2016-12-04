# -*- coding: utf-8 -*-
"""
MIT 6.00 introduction to Computer Science and Programming

Problem Set 1 Problem 1

A program to calculate the 1000th prime

Created on Sun Sep 11 03:21:40 2016

@author: marka
"""

possiblePrime = 3  # start at 3 first odd prime
primeCounter = 1   # 1 because the program does not check 2 for primeness
nth_prime = 10

while primeCounter < nth_prime:
   factor = 2
   notprime = 0
   while factor < (possiblePrime**0.5)+1 and notprime == 0:
       if possiblePrime % factor == 0 :
           notprime = 1
           possiblePrime += 2
       if factor > possiblePrime**0.5 and notprime == 0:
           primeCounter +=1
           notprime = 1  # well ... it is a prime but I need to break the loop somehow :)
           if primeCounter == nth_prime :
               break
           #print("The {0}th prime is {1}".format(primeCounter, possiblePrime))
           possiblePrime +=2
       factor += 1
print("The {0}th prime is {1}".format(primeCounter, possiblePrime))