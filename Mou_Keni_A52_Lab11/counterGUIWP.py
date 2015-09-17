'''
Keni Mou
Kmou1@binghamton.edu
Lab11, Excerise 1
Lab Section 52
CA Kyle Mille
'''

'''
Virtual counter GUI
Allows user to count up or down using buttons, reset counter using buttons,
  and set counter by entering value and pressing enter on keyboard

Output:
  value of counter displayed in Label(int)

Input:
  value of counter entered into Entry box(int)

Tasks:
  Create GUI with
  Model-counter(Counter)
      Controllers: buttonUp, bottonDown, buttonReset(Button)
      entryBox: (Entry)
  view:value(Lable)
  __watch():prevent counter from going negative
  countUp()
  countDown()
  reset()
  set()
'''
from tkinter import *
from counterWP import *

class CounterGUIWP:
  def __init__(self):
    
    #Main window
    self.__win=Tk()

    #Frames
    self.__topFrame=Frame(self.__win)
    self.__midFrame=Frame(self.__win)
    self.__bottomFrame=Frame(self.__win)
    
    #Top frame
    #count up and count down buttons
    self.__counter=CounterWP()

    #It seems if I put this after the setting up the frame, the command
    #cannot find this value so it is a error.
    self.__iVal=IntVar()
    self.__iVal.set(self.__counter.getValue())
    
    self.__buttonUp=Button(self.__topFrame, text="Count Up", command=self.countUp)
    self.__buttonDown=Button(self.__topFrame, text="Count Down", command=self.countDown)
    self.__buttonUp.pack(side="left")
    self.__buttonDown.pack (side="left")

    #Mid frame
    #reset button and entry box
    self.__buttonReset=Button(self.__midFrame, text="Reset counter", command=self.reset)
    self.__promptLabel=Label(self.__midFrame, text="Set Counter: ")
    self.__entryBox=Entry(self.__midFrame, width=7)
    self.__entryBox.bind("<Return>", self.set)
    self.__buttonReset.pack(side="left")
    self.__promptLabel.pack(side="left")
    self.__entryBox.pack(side="left")

    #Bottom frame
    #label and value
    self.__label=Label(self.__bottomFrame,text="Count=")
    self.__value=Label(self.__bottomFrame,textvariable=self.__iVal)
    self.__label.pack(side="left")
    self.__value.pack(side="left")

    #Pack the frames
    self.__topFrame.pack()
    self.__midFrame.pack()
    self.__bottomFrame.pack()

    mainloop()

  def countUp(self):
    self.__counter.increment()
    self.__iVal.set(self.__counter.getValue())
   # print("yean i count up") #debug

  def countDown(self):
    temp=self.__counter.getValue()
    self.__counter.decrement()
    self.__watch(temp)
    self.__iVal.set(self.__counter.getValue())

  def reset(self):
    self.__counter.reset()
    self.__iVal.set(self.__counter.getValue())

  def set(self, counter):
    temp=self.__counter.getValue()
    entryValue=int(self.__entryBox.get())
    self.__counter.set(entryValue)
    self.__watch(temp)
    self.__iVal.set(self.__counter.getValue())
    self.__entryBox.delete(0,END)

  def __watch(self, oldValue):
    if self.__counter.isNegative():
      messagebox.showinfo("warning", "Counter cannot be negative!")
      self.__counter.set(oldValue)


CounterGUIWP()
    
