## Mit 6.00 Introduction to Computer Science Spring 2011
## Problem Set 1.  Introduction to Flow Control
## August 10 2016
## Write a probram to calculate interest and minimum Monthly payments
## for a credit Card 
## Input from the user for starting balance, interest rate, and minimum
## required payment


loan_amount=input("Enter your Credit Card balance in dollars and cents - ")
minPayRate=input("Enter the Minimum Payment rate - ")
intRate=input('Enter the interest rate charged by you card provider - ')
balOut=loan_amount      # This will be the outstandig balance at the end of the
                        # Calculation Period
monIntChgs = 0          # The dollar value of the monthly interest
minMonPay = 0           # The dolar value of the minimum montly payment
princePd=0                # The dollar value of principle paid monthly
months = range(1,13)

for month in months:
    monIntChgs = intRate/12* balOut
    minMonPay = balOut * minPayRate
    if monIntChgs > minMonPay:
        print('Interest charges exceed the minimum payment, ')
        print('the debt cannot be repaid')
    balOut = balOut-minMonPay+monIntChgs
    princePd = minMonPay - monIntChgs
    
    


