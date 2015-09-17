'''
Keni Mou
Kmou1@binghamton.edu
Assignment 4, Exercise 2
Lab Section 52
CA Kyle Mille
'''

'''
Analysis

To determine whether a year is a leap year

Output to monitor:
  the tested year, and whether it is a leap year
  
Tasks allocated to Functions:
  isLeap
    to compute whether a year is a leap year
'''
# Constants
CENTURY_CONST=100 #the ratio of a century
LEAP_YEAR_RATIO=4
LEAP_YEAR_CENTURY_RATIO=400

#Constants used for testing
TEST1 = 1944
TEST2 = 2011
TEST3 = 1986
TEST4 = 1800
TEST5 = 1900
TEST6 = 2000
TEST7 = 2056

# to determine whether a year is a leap year
# year (int)
# return ture or false of whether the year is a leap year
def isLeap(year):
  if year % CENTURY_CONST != 0:
    return year % LEAP_YEAR_RATIO == 0
  else:
    return year % LEAP_YEAR_CENTURY_RATIO ==0

# to determine whether the given years are leap years
# use seven years to check the program
def main():
  print("This program is to check whether a year is a leap year.\n"\
        "A year is a leap year if it is divisible by 4\n"\
        "unless it is a century that is not divisible by 400. ")

  #Compute and display
  for i in (TEST1, TEST2, TEST3, TEST4, TEST5, TEST6, TEST7):
    if isLeap(i):
      print(i, "is a leap year")
    else:
      print(i, "is not a leap year")

main()
