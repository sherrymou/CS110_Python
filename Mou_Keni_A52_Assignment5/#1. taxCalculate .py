'''
Keni Mou
Kmou1@binghamton.edu
Assignment 5, Exercise 1
Lab Section 52
CA Kyle Mille
'''

'''
Analysis
calculate the income tax

Output to monitor:
  income (float) 
  tax (float)
  statue- married or single
  
Input from keyboard:
  statue(str)
  income (float)
  
Tasks allocated to Functions:
  marriedChecker
    check the marry statue

  taxCalculate
    calculate the tax based on the rule

  statueValid(statue):
    return if the statue is invalid

  incomeValid(income):
    return if the income is invalid

  continueValid(statue):
    return if the user want to continue this program

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
# param statue(int)- 0=married, others = single.
# return Ture if marride, False if single.
def marriedChecker(statue):
  return statue == "m"

# return if the statue is invalid
def statueValid(statue):
  return statue != "s" and statue != "m"

#return if the income is invalid
def incomeValid(income):
  return income < 0

#return if the user want to continue this program
def continueValid(statue):
  return statue != ""

# tax calculate
# param income(float)
# param tax(float)
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

  #get the marry statue or stop it.
  #for a better output, output "start" at the beginning
  statue=input("-=START=-\n"\
               "Please input your marry statue or press ENTER to quit\n"\
               "input m for married or s for single.")
            
  while continueValid(statue):
  
    #check if the marry statue is valid
    while statueValid(statue):
      statue=input("Your input is invalid. Please input your marry statue.\n"\
                    "input m for married or s for single.")

    #get the income
    incomeStr= input("please input your total income.")
    income=float(incomeStr)
    
    #check if the income is valid
    while incomeValid(income):
      incomeStr = input("Please input your income."\
                        "Your income must be greater than 0.")
      income=float(incomeStr)
      
    # calculate
    tax=taxCalculate(income,statue)

    #for a better output
    print("-=RESULT=-")

    #display the results
    if marriedChecker(statue):
        print("You are married")
    else:
        print ("You are single")
    print ("Your income is $", "$%.2f" %(income), ",and your tax is","$%.2f" %(tax) )
    #"$%.2f" %(value) 
    print ("--=END=--")

    #make the program keep going
    statue=input("\n"\
            "-=START=-\n"\
            "Please input your marry statue(s for single or m for married)\n"\
            "Or press ENTER to quit")

  #end message
  print("You end this program")

main()
