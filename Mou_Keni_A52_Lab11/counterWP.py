'''
Keni Mou
Kmou1@binghamton.edu
Lab11, Excerise 1
Lab Section 52
CA Kyle Mille
'''

class CounterWP:

  def __init__(self):
    self.__value = 0

  def getValue(self):
    return self.__value
    
  def __str__(self):
    return "Count" + str(self.__value)

  def increment(self):
    self.__value += 1

  def decrement(self):
    self.__value -=1 

  def reset(self):
    self.__value = 0

  def set(self, avalue):
    self.__value = avalue

  def isNegative(self):
    return self.__value < 0

CounterWP()
