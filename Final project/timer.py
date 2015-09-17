'''
Keni Mou
Kmou1@binghamton.edu
Kristy Stevens
ksteven4@binghamton.edu
Final Project 6/7
Lab Section 52
CA Kyle Mille
'''

#This part is written by Keni

'''
This is the timer class.
It conducts the counting down
'''

import time

class Timer:
  def __init__(self,sec,minu):
    self.__sec=sec
    self.__min=minu
    self.__current=self.__sec+self.__min*60

  def getCurrentTime(self):
    return int(self.__current)

  def getCurrentSec(self):
    return int(self.__current%60)

  def getCurrentMin(self):
    return int(self.__current//60)

  def getRange(self):
    return range(self.__current,0,-1)
      
  def countDown(self):
    time.sleep(1)
    self.__current-=1
    


    

  

    
