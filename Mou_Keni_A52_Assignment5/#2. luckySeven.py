'''
Keni Mou
Kmou1@binghamton.edu
Assignment 5, Exercise 2
Lab Section 52
CA Kyle Mille
'''

'''
Analyse
To simulate the lucky sevens game

Output to monitor:
    roll(int)- to count the rolls
    maxSoFar(float)- the maximum money amount
    maxRoll(int)- the roll number when the amount was the highest

Input from keyboard
    money(Str)-how much you want to use to play the game

Tasks allocated to Functions:
    simulateDice
        To simulate 2 dices

    diceChekcer(dice):
        to check whether the number is lucky number

    checkMoney(money):
        to check whether the user still has money

    checkMax(maxNumber,presentNumber):
        to filt the maximum money

'''

import random

# CONSTATN
WIN_POINT=4
LOSE_POINT=1

DICE_START=1
DICE_END=6

LUCKY_NUMBER=7


# To simulate 2 dices
# param dice1(int)
# param dice2(int)
# param dice(int)- the sum of 2 dices (return)
def simulateDice():
    dice1 = random.randrange(DICE_START,DICE_END+1)
    dice2 = random.randrange(DICE_START,DICE_END+1)
    dice = dice1 + dice2
##  print(dice) #debug
    return dice

# to check whether the number is lucky number
# return true if dice = 7
def diceChekcer(dice):
    return dice == LUCKY_NUMBER

# to check whether the user still has money
# param money(float)
# return true if user still have money
def checkMoney(money):
    return money >= 0

# to filt the maximum money
# param maxNumber(float)
# param presentNumber(float)
# return true if the present number is greater than the max number
def checkMax(maxNumber,presentNumber):
    return maxNumber < presentNumber

# to simulate the lucky number game.
# param roll(int)- to count the rolls
# param maxSoFar(float)- the maximum money amount
# param maxRoll(int)- the roll number when the amount was the highest
def main():
    #description
    print("This is the game of Lucky Sevens")

    #get the input for user
    moneyStr=input("Please place your bet in whole dollars:\n"\
                "OR press <Enter> to quit:")

    while moneyStr != "":

        money=float(moneyStr)

        roll=0 #initial condition
        maxSoFar=0 #initial condition

        #print the table header
        #for ↓better output↓
        print('\n'\
              "Rolls", '\t', "Value", '\t', "Dollars")

        #simulate the game
        while checkMoney(money):
            roll=roll+1
            dice = simulateDice()
            if diceChekcer(dice):
                money=money+WIN_POINT
            else:
                money=money-LOSE_POINT
                
            #avoid $-1 appears in the last line
            if checkMoney(money):
                print (roll,'\t',dice,'\t',"$%.2f" %(money))

            #filt out the max money
            if checkMax(maxSoFar,money):
                maxSoFar=money
                maxRoll=roll

        #display    
        print("You became broke after", roll, "rolls\n"\
              "You should have quit after", maxRoll, \
              "rolls","when you had", "$%.2f" %(maxSoFar) )
        
        #start again
        moneyStr=input("Please place your bet in whole dollars: \n"\
                    "Or press ENTER to quit.")
    #quit message
    print("You quited this program")

main()
