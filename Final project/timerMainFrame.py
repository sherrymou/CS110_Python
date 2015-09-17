'''
Keni Mou
Kmou1@binghamton.edu
Kristy Stevens
ksteven4@binghamton.edu
Final Project 7/7
Lab Section 52
CA Kyle Mille
'''

#This file is written by Keni

'''
Note:
This window is for counting down.
Users can select minutes bewteen 0-10 and enter a second bewteen 0-59
There is also a progress bar.
The functions include: start, pause, reset

Modules used:
  tkinter
  threading

Classes used:
  timer
  progressBar
  testSound

Output:
  currentSec(str)
  currentMin(str)

Input:
  secVar(str)
  minVar(int)
'''

#---------------------------------------------------------------------------------------


from tkinter import *
import threading
import timer
import progressBar
import testsound


class TimerGUI:

  #===Views===
  #instruLabel(Label)
  #instruLabelExplain(Label)
  #minLabel(Label)
  #secLabel(Label)
  #currentSec(StringVar)
  #currentMin(StringVar)
  #currentSecLabel(Label)
  #currentMinLabel(Label)
  #minLeft(Label)
  #secLeft(Label)
  #stageLabel(Label)

  #===Controls===
  #minOption(OptionMenu)
  #secEntry(Entry)
  #startButton(Button)
  #pauseButton(Button)
  #resetButton(Button)

  #===Organizational widgets===
  #win(Tk)
  #instruFrame(Frame)
  #chooseFrame(Frame)
  #commandFrame(Frame)
  #displayFrame(Frame)
  #textFrame(Frame)
  #loadingFrame(Frame)

  #===Vars===
  #minVar(IntVar)
  #secVar(IntVar)
  #stageVar(StringVar)

  #===others===
  #stage(Bool)
  #minList(list)

  def __init__(self):

    #Create the window----------------------------------------------------------
    self.__win=Tk()
    self.__win.title("Timer")  
    self.__win.iconbitmap("favicon.bmp")

    #Frame contain simple words-------------------------------------------------
    self.__instruFrame=Frame(self.__win)
    self.__instruLabel=Label(self.__instruFrame,text="Please select minutes and enter seconds")
    self.__instruLabelExplain=Label(self.__instruFrame,text="This timer only allow count \
down within 10:59 minutes.\n Please enter a integer between 0 to 59 as the seconds")
    self.__instruLabel.pack(side="top")
    self.__instruLabelExplain.pack(side="top")
    self.__instruFrame.pack()
    
    #Frame contian the dropdown bars---------------------------------------------

    self.__chooseFrame=Frame(self.__win)

    #For min
    self.__minList=[0,1,2,3,4,5,6,7,8,9,10]
    self.__minVar=IntVar(self.__chooseFrame)
    self.__minVar.set(0)
    self.__minOption=OptionMenu(self.__chooseFrame,self.__minVar,\
                                *self.__minList,command=self.checkStartTimer)
    self.__minLabel=Label(self.__chooseFrame,text="Min")

    #For sec
    self.__secVar=IntVar(self.__chooseFrame)
    self.__secVar.set(0)
    self.__secEntry=Entry(self.__chooseFrame,width=7)
    self.__secEntry.bind('<Return>',self.setSec)
    self.__secLabel=Label(self.__chooseFrame,text="Sec")

    #pack
    self.__minOption.pack(side="left")
    self.__minLabel.pack(side="left")
    self.__secEntry.pack(side="left")
    self.__secLabel.pack(side="left")
    
    self.__chooseFrame.pack()
    
    #Frame contain the command buttons-------------------------------------------
    self.__commandFrame=Frame(self.__win)

    self.__stage=False

    #The buttons should be disabled initially    
    self.__startButton=Button(self.__commandFrame,text="Start",command=self.start)
    self.__startButton.config(state="disabled")

    self.__pauseButton=Button(self.__commandFrame,text="Pause",command=self.pause)
    self.__pauseButton.config(state="disabled")

    self.__resetButton=Button(self.__commandFrame,text="Reset",command=self.reset)
    self.__resetButton.config(state="disabled")

    self.__startButton.pack(side="left")
    self.__pauseButton.pack(side="left")
    self.__resetButton.pack(side="left")

    self.__commandFrame.pack()

    #Display frame-------------------------------------------------------------

    self.__displayFrame=Frame(self.__win)

    #text frame
    self.__textFrame=Frame(self.__displayFrame)
    
    self.__stageVar=StringVar(self.__textFrame)
    self.__stageVar.set(" ")
    self.__stageLabel=Label(self.__textFrame,textvariable=self.__stageVar)

    self.__currentSec=IntVar(self.__textFrame)
    self.__currentSec.set(0)
    self.__currentMin=IntVar(self.__textFrame)
    self.__currentMin.set(0)

    self.__currentMinLable=Label(self.__textFrame,textvariable=self.__currentMin)
    self.__minLeft=Label(self.__textFrame,text="Min")
    self.__currentSecLable=Label(self.__textFrame,textvariable=self.__currentSec)
    self.__secLeft=Label(self.__textFrame,text="Sec")
    
    self.__currentMinLable.pack(side="left")
    self.__minLeft.pack(side="left")
    self.__currentSecLable.pack(side="left")
    self.__secLeft.pack(side="left")
    self.__stageLabel.pack(side="left")
    
    self.__textFrame.pack()

    #Loading frame
    self.__loadingFrame=Frame(self.__displayFrame)
    self.__progressBar=progressBar.progressBar(self)
    self.__loadingFrame.pack()
    self.__displayFrame.pack()

    mainloop()
    

  #Accessors-----------------------------------------------------------------------
  def getsecVar(self):
    return self.__secVar.get()
  
  def getminVar(self):
    return self.__minVar.get()

  def getCurrentSec(self):
    return self.__currentSec.get()

  def getCurrentMin(self):
    return self.__currentMin.get()

  def getLoadingFrame(self):
    return self.__loadingFrame
  
  #Predictators--------------------------------------------------------------------

  #return true if set time is not 0
  def validChoices(self):
    return self.__secVar.get() != 0 or self.__minVar.get()!= 0

  #return true if the entry is valid
  def validEntry(self):
    return self.__secEntry.get().isdigit() and int(self.__secEntry.get())<60

  #return true if there is no in-progress count down
  def countDownOver(self):
    return self.__currentSec.get()==0 and self.__currentMin.get()==0


  #Mutators------------------------------------------------------------------------
  #Button and entrybox enables and disables
  def enableStartButton(self):
    self.__startButton.config(state="normal")

  def disableStartButton(self):
    self.__startButton.config(state="disabled")

  def enablePauseButton(self):
    self.__pauseButton.config(state="normal")
    
  def disablePauseButton(self):
    self.__pauseButton.config(state="disabled")

  def enableResetButton(self):
    self.__resetButton.config(state="normal")

  def disableResetButton(self):
    self.__resetButton.config(state="disabled")

  def enableEntryBox(self):
    self.__secEntry.config(state="normal")

  def disableEntryBox(self):
    self.__secEntry.config(state="disabled")

  def cleanEntryBox(self):
    self.__secEntry.delete(0,END)
    

  #Cases
  
  #Set the sec from entry box
  def setSec(self,event):
  
    if self.validEntry():
      self.__secVar.set(int(self.__secEntry.get()))
      self.disableEntryBox()
      self.checkStartTimer(self.__secVar)

    else:
      messagebox.showerror("Invalid Input","Second is an integer bewteen 0 to 59")
      self.cleanEntryBox()

  #if the set time is not 0, enable start command   
  def checkStartTimer(self,newValue):
    if self.validChoices():
      self.enableStartButton()
      self.enableResetButton()

  #update current time
  def updateCurrent(self):
    self.__currentSec.set(self.__timer.getCurrentSec())
    self.__currentMin.set(self.__timer.getCurrentMin())

  #update initial setting
  #if it is a new count down, params will be taken from chooseFrame
  #if it countinues last count down, params will be taken from current time
  def updateInit(self):
    if self.countDownOver():
      self.__currentSec.set(self.getsecVar())
      self.__currentMin.set(self.getminVar())    
  

  #Commands------------------------------------------------------------------------------

  def start(self):
    self.disableStartButton()
    self.enablePauseButton()
    self.disableResetButton()
    self.__stage=True

    def callback():
      
      self.updateInit()
      self.__timer=timer.Timer(self.getCurrentSec(),self.getCurrentMin())
      self.updateCurrent()
      self.__progressBar.start()
      self.__stageVar.set("left")

      for i in self.__timer.getRange():
        if self.__stage:
          self.__timer.countDown()
          self.updateCurrent()

      #Check if the count down is over
      #And if it is over, change the button setting
      if self.countDownOver():
        self.enableStartButton()
        self.disablePauseButton()
        self.enableResetButton()
        self.__stageVar.set("Count Down Over!")
        self.__progressBar.stop()
        testsound.playAudio()
        
        

    t=threading.Thread(target=callback)
    t.start()

  def pause(self):
    if self.__stage:
      self.__stage = False
      self.__pauseButton["text"]="Continue"
      self.enableResetButton()
      self.__stageVar.set("Paused")
      self.__progressBar.stop()
    else:
      self.__stage = True
      self.__pauseButton["text"]="Pause"
      self.start()


  def reset(self):
    self.__secVar.set(0)
    self.__minVar.set(0)
    self.__currentSec.set('0')
    self.__currentMin.set('0')
    self.__stageVar.set(" ")
    self.__pauseButton['text']='Pause'
    self.enableEntryBox()
    self.cleanEntryBox()
    self.disableStartButton()
    self.disablePauseButton()
    self.disableResetButton()

#TimerGUI()
