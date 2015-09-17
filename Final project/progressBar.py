'''
Keni Mou
Kmou1@binghamton.edu
Kristy Stevens
ksteven4@binghamton.edu
Final Project 4/7
Lab Section 52
CA Kyle Mille
'''

#This file is written by Kristy

'''
Notes:
This is the progress bar.

'''

from tkinter.ttk import *
from tkinter import *

class progressBar:
  def __init__(self,parent):
    self.__parent=parent
    self.__frame=self.__parent.getLoadingFrame()
    self.__loadingTime=IntVar()
    self.__loadingTime.set(0)

    self.__bar= ttk.Progressbar(self.__frame,orient ="horizontal",length = 150, \
                         mode ="indeterminate")
    self.__bar.pack()
  

  def start(self):
    self.__bar.start()
    
  def stop(self):
    self.__bar.stop()
