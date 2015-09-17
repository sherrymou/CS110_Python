'''
Keni Mou
Kmou1@binghamton.edu
Assignment11 Part1-2
Lab Section 52
CA Kyle Mille
'''

import random
import tkinter.messagebox

#Constants
MIN_SIDES=4


'''
User defined exception class (subclass of Exception)
'''

class BadArgument(Exception):

  def __init__(self):
    self.__title="Bad Argument"
    self.__message="Sides must be greater than or equal to four"

  def getTitle(self):
    return self.__title

  def __str__(self):
    return self.__message
'''
Models a single multi-sided die
'''

#param sides(int)
#return true if sides is valid
def isValid(sides):
  sidesStr=str(sides)
  return sidesStr.isdigit() and int(sides)>=MIN_SIDES
  
class DieMultiSided:
  
  # ------------------------------------------------------
  # Constructor
  
  # param initial(int)
  def __init__(self, sides=6, value= -1):
    self.__value = value
    self.__sides = sides
    if not isValid(self.__sides):
      raise BadArgument

  # --------------------------------------------------------
  # Accessors

  def getSides(self):
    return self.__sides

  def getValue(self):
    return self.__value

  # -------------------------------------------------------
  # Mutators
  
  # roll the dice
  def roll(self):
    value = random.randrange(1, (self.__sides+1))
    self.__value = value

  def reset(self):
    self.__value=-1

  # string ------
  def __str__(self):
    return  " " if self.__value == -1 else "%s"%(self.__value)

'''
# Tester for DieMultiSided class
def main():
  print("Create default die")
  die = DieMultiSided()
  print("Value of sides: %d" % die.getSides())
  print("Value (int): %d" % die.getValue())
  print("Value (str): %s" % die)
  
  die.roll()
  print("Value (int): %d" % die.getValue())  
  print("Value (str): %s" % die)

  print("Create 12-sided die")
  die = DieMultiSided(12)
  print("Value of sides: %d" % die.getSides())
  print("Value (int): %d" % die.getValue())
  print("Value (str): %s" % die)
  
  inputStr = ''
  while not inputStr:
    die.roll()
    print("Value: %d" % die.getValue())  
    print("Value: %s" % die)
    inputStr = input("Press any key to exit loop: ")
    
  print("Create die with invalid state")
  try:  
    die = DieMultiSided(3)
    print("Value of sides: %d" % die.getSides())
    print("Value (int): %d" % die.getValue())
    print("Value (str): %s" % die)
    die.roll()
    print("Value (int): %d" % die.getValue())
    print("Value (str): %s" % die)
  except BadArgument as err:
    tkinter.messagebox.showerror(err.getTitle(), str(err)) 
  
main()
'''
