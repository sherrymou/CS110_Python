'''
Keni Mou
Kmou1@binghamton.edu
Lab 5, Exercise 2
Lab Section 52
CA Kyle Mille
'''

'''
Analysis

To print out the leap year between 1600 and 2014

Output to monitor:
  a list of leap year
  i(int)-leap year
Tasks allocated to Functions:
  isLeap
    to compute whether a year is a leap year
'''
# Constants
CENTURY_CONST=100 #the ratio of a century
LEAP_YEAR_RATIO=4
LEAP_YEAR_CENTURY_RATIO=400

YEAR_BEGIN=1600
YEAR_END=2015 #2014+1=2015

# to determine whether a year is a leap year
# param year (int)
# return ture or false of whether the year is a leap year
def isLeap(year):
  return year % CENTURY_CONST != 0 and year % LEAP_YEAR_RATIO == 0 \
           or year % CENTURY_CONST != 0 and year % LEAP_YEAR_CENTURY_RATIO ==0

# to determine whether the given years are leap years
# use seven years to check the program
def main():
  print("This program is to check whether a year is a leap year.\n"\
        "A year is a leap year if it is divisible by 4\n"\
        "unless it is a century that is not divisible by 400. ")

  #Compute and display
  for i in range (YEAR_BEGIN,YEAR_END):
    if isLeap(i):
      print(i, "is a leap year")

main()
