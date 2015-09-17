'''
Keni Mou
Kmou1@binghamton.edu
Kristy Stevens
ksteven4@binghamton.edu
Final Project 1/7
Lab Section 52
CA Kyle Mille
'''

#This part is cooperative

'''
Note:
This is the main window of the program
It contains one picture and two buttons
'''

from tkinter import *
import AboutMainFrame
import timerMainFrame

class MainWindow:
  
  #===Views===
  #animeCanvas(Canvas)

  #===Controls===
  #timerButton(Button)
  #aboutButton(Button)

  #===organizational widgets===
  #win(Tk)
  #welcomeFrame(Frame)
  #buttonFrame(Frame)
  
  def __init__(self):
    
    #create the window------------------
    self.__win=Tk()
    self.__win.title("Timer Main Window")
    self.__win.iconbitmap(r"favicon.bmp")
    
    #welcome frame-----------------------
    self.__welcomeFrame=Frame(self.__win)
    photo=PhotoImage(file="MiuMiu.gif",)
    self.__pictureLabel=Label(self.__welcomeFrame,image=photo)
    self.__pictureLabel.pack()
    self.__welcomeFrame.pack()
    
    #button frame-------------------------
    self.__buttonFrame=Frame(self.__win)
    self.__timerButton=Button(self.__buttonFrame,text="Timer",command=self.openTimer)
    self.__aboutButton=Button(self.__buttonFrame,text="Notes",command=self.openAbout)
    self.__timerButton.pack(side="left")
    self.__aboutButton.pack(side="left")
    self.__buttonFrame.pack()

    mainloop()

  #Buttons events
  def openTimer(self):
    timerMainFrame.TimerGUI()

  def openAbout(self):
    AboutMainFrame.About()

MainWindow()

    
