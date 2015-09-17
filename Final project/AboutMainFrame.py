'''
Keni Mou
Kmou1@binghamton.edu
Kristy Stevens
ksteven4@binghamton.edu
Final Project 2/7
Lab Section 52
CA Kyle Mille
'''

#This file is written by Keni

'''
Note:
Thise is the "Notes" window.
It contains the basic infomations and some cute stuffs.
Also it is a good place for user to take notes
They can output their modified text to a txt file

Output
  outputfile(file)

Input
  line(str)

Modules imported:
  tkinter
  tkinter.scrolledtext
  Outputmodule
'''

#-----------------------------------------------------------------------

from tkinter import *
import tkinter.scrolledtext as tkst

import Outputmodule

#Texts
ABOUT_CONTENT='''\
        ,----,
   ___.`      `,
   `===  D     :
     `'.      .'
        )    (                   ,
       /      \_________________/|
      /                          |
     |                           ;
     |               _____       /
     |      \       ______7    ,'
     |       \    ______7     /
      \       `-,____7      ,'      
^~^~^~^`\                  /~^~^~^~^
  ~^~^~^ `----------------' ~^~^~^
~^~^~^~^~^^~^~^~^~^~^~^~^~^~^~^~

////////////////////////////////////
This is a timer program.
You can set a time between 00:01 to 10:59
Whenever you want to stop, you can pause or unpause it.
After finished, there will be a sound

==================================
↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
----------------------------------
Here is also a good place for you to take notes while doing timing

You are free to change the words here,
and you can also output your modified text to a .txt file
-----------------------------------
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
===================================

Authors:
Binghamton University

Keni Mou
(kmou1@binghamton.edu)
Kristy Steven
(kstevens4@binghamton.edu)

Spring 2014
CS110
Final Project

'''

OUT_PUT_MESSAGE="\
Do you want to output your modified text to a file? \n However,\
I know you won't write too much here...."


class About:

  #Constructor------------------------------------------------

  #win(TK)
  #textFrame (Frame)
  #outPutFrame (Frame)
  
  #textBox (scrolledtext)
  #label(Label)
  #outputButton(Button)
  
  def __init__(self):

    #
    self.__win=Tk()
    #change title
    self.__win.title("Notes")
    #change icon
    self.__win.iconbitmap("favicon.bmp")

    #Text Frame----------------------------------------------------------
    self.__textFrame=Frame(self.__win)
    
    self.__textBox=tkst.ScrolledText(self.__win)
    self.__textBox.insert(INSERT,ABOUT_CONTENT)
    self.__textBox.pack()

    self.__textFrame.pack()

    #Output Frame--------------------------------------------------------
    self.__outPutFrame=Frame(self.__win)
    self.__label=Label(self.__win,text=OUT_PUT_MESSAGE)
    self.__outPutButton=Button(self.__outPutFrame, text="Output to file",command=self.output)
    self.__label.pack(side="top")
    self.__outPutButton.pack(side="top")
    self.__outPutFrame.pack()

    self.__win.mainloop()

  #output to file
  def output(self):
    line=self.__textBox.get(1.1000000,1000000.1)
    Outputmodule.outputToFile(line)
