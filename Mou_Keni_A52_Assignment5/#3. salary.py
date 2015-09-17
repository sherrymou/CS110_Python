'''
Keni Mou
Kmou1@binghamton.edu
Assignment 5, Exercise 3
Lab Section 52
CA Kyle Mille
'''

'''
Analyse
iteratively computes the amount of money a person would earn over a period of time
if his or her salary is one penny the first day, two pennies the second day,
and continues to double each day.

Output to monitor:
    i(int)-the present day
    day(int)-the total days
    earn(float)
    earnTotal(float)
    
Input from keyboard:
    day(int)

Tasks allocated to Function
    calculate
        to calculate the pay for each day

    calculateTotal
        to calculate the total amount of earning

    pennyToDollar
        to conver pennies to dollars
'''
#CONSTANTS
DOUBLE=2
PENNY_DOLLAR=100
START_DAY=2

#to calculate the pay for each day
#param lastEarn(float)- the money the person earned last day
#param presentEarn(float)-the money the person earned this day
#return the present earned amount 
def calculate(lastEarn):
    presentEarn=lastEarn*DOUBLE
    return presentEarn

#to calculate the total amount of earning
#param totalSoFar(float)
#param totalNow(float)
#return the present total amount
def calculateTotal(presentEarn,totalSoFar):
    totalNow=presentEarn+totalSoFar
##  print(totalNow) #debug
    return totalNow

#to conver penny to dollar
#param penny(int)
def pennyToDollar(penny):
    return penny/PENNY_DOLLAR

#to print a table showing both the day and what the salary was for that day
#param day(int)
#param earn(int)
#param earnTotal(int)
#param earnDollar(float)
def main():
    dayStr = input('\n'\
                "Enter the number of days for which salary is to be computed")
    day = int(dayStr)

    print ("Day",'\t','\t','\t',"Pay",'\n'\
           "----------------------------------------------------------")
    
    earn = 1 #initial condition
    earnTotal = 1 #initial condition

    print ("%2d"%(1),'\t',"%20d"%(earn)) #the first line is special
    
    for i in range(day-1):
        earn = calculate(earn)
        earnTotal = calculateTotal(earn,earnTotal)
        print("%2d"%(i+START_DAY),'\t',"%20d"%(earn))

    earnDollar=pennyToDollar(earnTotal)

    print ("In", day, "days a penny grows to", "$%.2f"%(earnDollar))

main()
