'''
Keni Mou
Kmou1@binghamton.edu
Assignment 7 Exerciese 1 
Lab Section 52
CA Kyle Mille
'''

'''
analyze
test the module

Output to the monitor
theList(list)
average value(float)
maximum value(int)
sum of squares (int)
odd count(int)
sum even numbers(int)
sum negative numbers(int)


'''

from listFunctions import createRandomInts, computeAverage, computeMax, \
     computeSumOfSquares, isEven, isNegative, sumUpEvenNumbers, countOddNumbers,\
     sumUpNegative

#Constants
NUMBERS=100
START_NUMBER1=0
START_NUMBER2=-1000
END_NUMBER=1000

def main():
    #First list test 
    theList=createRandomInts(NUMBERS,START_NUMBER1,END_NUMBER)
    print("List contents:",theList)
    print("Average value = ",computeAverage(theList))
    print("Maximum value = ",computeMax(theList))
    print("Sum of squares = ",computeSumOfSquares(theList))
    print("Odd count = ",countOddNumbers(theList))
    print("Sum even numbers = ",sumUpEvenNumbers(theList),'\n')

    #Last list test
    anotherList=createRandomInts(NUMBERS,START_NUMBER2,END_NUMBER)
    print("List contents:",anotherList)
    print("Sum negative numbers:",sumUpNegative(anotherList))

main()
