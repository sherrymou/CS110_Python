'''
Keni Mou
Kmou1@binghamton.edu
Assignment 7, exersice 1(module)
Lab Section 52
CA Kyle Mille
'''

import random

#creat a ramdon list of numbers
#param number(int)
#param lowest(int)
#param highest(int)
#param randomNumber(int)
#return the list
def createRandomInts(number,lowest,highest):
    myList=[] #initial
    for i in range (number):
        randomNumber=random.randrange(lowest,highest)
        myList.append(randomNumber)
    return myList


#compute the average in a list
#param theList(list)
#param theSum(int)
#param average(float)
#return average 
def computeAverage(theList):
    theSum=0 #initial 
    for i in theList:
        theSum +=i
    average=theSum/len(theList)
    return average


#Pick up the maximum number in the list
#param theList(list)
#param maxSoFar(int)
#return the max number
def computeMax(theList):
    maxSoFar=0
    for i in theList:
        if i > maxSoFar:
            maxSoFar=i
    return maxSoFar


#compute the sum of the squares of the numbers in the list
#param theList(list)
#param theSum(int)
#param squared(int) the square of the number
#return the sum
def computeSumOfSquares(theList):
    theSum = 0
    for i in theList:
        squared = i ** 2
        theSum += squared
    return theSum


#check whether a number is even
#param number(float)
#return true if it is even
def isEven(number):
    return number % 2 ==0


#check whether a number is negative
#param number(float)
#return ture if it is negative
def isNegative(number):
    return number < 0

  
#count the odd numbers of a list
#param theList(list)
#param counter(int)
#return the number of odd numbers. 
def countOddNumbers(theList):
    counter = 0
    for i in theList:
        if not isEven(i):
            counter += 1
    return counter


#Sum up all the even numbers in a list.
#param theList(list)
#param theSum(int)
#return the sum
def sumUpEvenNumbers(theList):
    theSum = 0
    for i in theList:
        if isEven(i):
            theSum += i 
    return theSum


#Sum up all the negative numbers in a list.
#param theList(list)
#param theSum(int)
#return the sum
def sumUpNegative(theList):
    theSum=0
    for i in theList:
        if isNegative(i):
            theSum += i
    return theSum
