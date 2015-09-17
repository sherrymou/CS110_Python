'''
Keni Mou
Kmou1@binghamton.edu
Assignment 4, Exercise 3
Lab Section 52
CA Kyle Mille
'''

'''
Analysis
calculate the income tax

Output to monitor:
  income (float) 
  tax (float)
  statue- married or single (for debug)
  income level (for debug)
  
Input from keyboard:
  statue(int)- 0 for married, others for single
  income (float)
  
Tasks allocated to Functions:
  marriedChecker
    check the marry statue

  taxCalculate
    calculate the tax based on the rule
    The rule is :
      If status is single 
        income is over 0 but not over 8000,
        the tax is 10% of the amount over 0
        income is over 8000 but not over 32000,
        the tax is  $800 + 15% of the amount over 8000
        income is over 32000,
        the tax is $4,400 + 25% of the amount over 32000
      If status is married
        income is over 0 but not over 16000,
        the tax is 10% of the amount over 0
        income is over 16000 but not over 64000,
        the tax is 1600 + 15% of the amount over 16000
        income is over 64000,
        the tax is 8800 + 25% of the amount over 64000
'''

# Constants
LOW_RATIO = 0.1 #10%
MID_RATIO = 0.15 #15%
HIGH_RATIO = 0.25 #25%

SINGLE_LOW_LINE = 8000 #$
SINGLE_MID_LINE = 32000 #$
MARRIED_LOW_LINE = 16000 #$
MARRIED_MID_LINE = 64000 #$

  #if one's salary reach the last line, they should pay this amount first,
  #and then calculate the rest using the proper ratio
SINGLE_MID_BASE = 800 #$
SINGLE_HIGH_BASE = 4400 #$
MARRIED_MID_BASE = 1600 #$
MARRIED_HIGH_BASE = 8800 #$


# check married or single
# statue(int)- 0=married, others = single.
# return Ture if marride, False if single.
def marriedChecker(statue):
  return statue == 0 

# tax calculate
# income(float)
# tax(float)
# return the calculated tax
def taxCalculate(income,statue):
  if marriedChecker(statue):
    if income <= MARRIED_LOW_LINE:
      tax= income * LOW_RATIO
    elif income <= MARRIED_MID_LINE:
      tax= (income-MARRIED_LOW_LINE)*MID_RATIO + MARRIED_MID_BASE
    else:
      tax= (income-MARRIED_MID_LINE)*HIGH_RATIO + MARRIED_HIGH_BASE
  else:
    if income <= SINGLE_LOW_LINE:
      tax= income * LOW_RATIO
    elif income <= SINGLE_MID_LINE:
      tax= (income-SINGLE_LOW_LINE)*MID_RATIO + SINGLE_MID_BASE
    else:
      tax= (income-SINGLE_MID_LINE)*HIGH_RATIO + SINGLE_HIGH_BASE
  return tax

#ask user to input marry statue and the income amount.
#calculate the tax
def main():
  print("This program is to calculate the income tax based on the rule")

  # Take in user input and convert
  statueStr=input("Please input your marry statue.\n"\
                  "input 0 for married and 1 for single.\n"\
                  "(if you enter other interger rather than 1 or 0,\n"\
                  "You will be processed as single.)")
    #input 0 or 1 instead of "married" or "single" to avoid spelling mistake
  statue= int(statueStr)

  incomeStr= input("please input your total income.")
  income=float(incomeStr)
  
  # calculate
  tax=taxCalculate(income,statue)

  # Display
  
  #There are lots of outputs on the screen,
  #So I want to use a line to seperate the result from the description
  #It may make the output clear. 
  print("----------------------------------------------------")
  if marriedChecker(statue):
    print("You are married")
  else:
    print ("You are single")
  print ("Your income is $", income, ",and your tax is $",tax)

main()
