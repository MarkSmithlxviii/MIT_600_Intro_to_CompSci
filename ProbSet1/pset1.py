# -*- coding: utf-8 -*-
"""
Created on Tue Jul 01 11:44:35 2014

@author: Mark
"""
import time  # not part of the problem set interested to see the difference
#            different methods made to runtime

# prime 10 = 29
# prime 100 = 541
# prime 1000 = 7919
# prime 10,000 = 104729

# inintialize the variables
n = 1  # the iterator that will be used to check each odd
#        number greater than 2
cpr = 1  # (c)urrent (p)rime (r)ank
Lop = 3  # (L)ist (o)f (p)rimes starts with the first prime
cond = 'possible prime'  # test condition

start = time.time()

while cpr < 1000:
    for numbers in range(2, Lop):
        # primes are calculated below and appended to this
        # list. The primes are then used in the following 
        # block of code.
        ts = 2 * n + 1  # test subject to be evaluated
        if cond == 'possible prime' and numbers <= ts ** 0.5:
            # for the ith prime in the list of primes this
            # block is evaluated iff all lesser primes are
            # not primes
            if ts % numbers == 0:
                cond = 'not prime'  # if a factor is found
                #                    this could have been any
                #                    value 
                Lop = int(ts ** 0.5) + 2
                break  # reduces run time by breaking the 
                # for loop when the first factor is found
            else:
                cond = 'possible prime'
    if cond == 'possible prime':
        # if all primes less than root(test Subject) are not
        # factors than test subject is a prime and is
        # appended to the list of primes
        Lop = int(ts ** 0.5) + 2
        cpr = cpr + 1  # cpr is increased if ts is a prime
        # print progress through the evaluation
        # print 'The ', cpr, ' prime is ', ts
    cond = 'possible prime'  # reset the test condition for
    #                         the next test subject
    n = n + 1  # increase the test subject iterator
print('Finished')
print('The ', cpr, 'th prime is ', ts)


#for n in range(2, 1299710):
##while cpr < 10000:
#    m = int(n ** 0.5) + 1
#    for x in range(2, m):
#         if n % x == 0:
#             #print n, 'equals', x, '*', n/x
#             break
#    #else:
#         # loop fell through without finding a factor
#        #cpr = cpr + 1
#        
#print n, 'is a prime number'

end = time.time()

print end - start
