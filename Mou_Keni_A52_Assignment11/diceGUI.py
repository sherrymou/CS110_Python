'''
Keni Mou
Kmou1@binghamton.edu
Assignment11 Part4
Lab Section 52
CA Kyle Mille
'''


'''
Note:  should be accompanied by labeled sketch of GUI interface

Provides control and view GUI for set of dice
that can be rolled and summed once per turn in a game

Note:  all names start with self.__

Output to DiceGUI labels:
  sum (StringVar)

Input to DiceGUI:
  numberDice (Entry)
  reset (Button)

Modules imported:
  tkinter
  dieGUI
  dieMultisided
  counterWP
Classes Used:
  DieGUI
  DieMultisided
  CounterWP
'''

# 1. Define imports
from tkinter import *
import counterWP
import dieMultiSided
import dieGUI

# 2. Define class
class DiceGUI(object):

  #-- Constructor --------------------------------------------------------

  # 3. Define constructor
  # Model:
  #   dice (list of DieGUI)
  # Views:
  #   inputLabel (Label)
  #   resultLabel (Label)
  #   resultValue (Label)
  #   diceLabel (Label)
  #   sum (IntVar)
  # Controls:
  #   entry (Entry)
  #   reset (Button)
  # Organizational widgets:    
  #   win (Tk)
  #   inputFrame (Frame)
  #   resultFrame (Frame)
  #   diceLabelFrame (Frame)
  #   diceFrame (Frame)    
  # Other instance variables and objects:    
  #   numberDice (int)
  #   numberCreated (int)
  #   rollCounter (CounterWP) 
  def __init__(self):

    # 4. Create main window
    self.__win = Tk()

    #--------------------------------------------------------------------------

    # 5. Create model, count variables, and counter
    self.__dice = []  # model
    self.__numberDice = 0
    self.__numberCreated = 0
    self.__rollCounter = counterWP.CounterWP() # secondary model

    #--------------------------------------------------------------------------

    # 6. Create user input frame
    self.__inputFrame=Frame(self.__win)

    # 7. Create static label and entry box for entering number of dice
    # Bind entry box to createDice event handler
    self.__inputLabel=Label(self.__inputFrame, text="Number of Dice:")
    self.__inputLabel.bind("<Return>",self.createDice)
    self.__entry=Entry(self.__inputFrame, width=6)
    self.__entry.bind("<Return>", self.createDice)

    # 8. Pack widgets into input frame
    self.__inputLabel.pack(side="left")
    self.__entry.pack(side="left")
    
    # 9. Pack input frame in the main window
    self.__inputFrame.pack()

    #--------------------------------------------------------------------------

    # 10. Create result frame
    self.__resultFrame=Frame(self.__win)

    # 11. Create reset button, set its event handler to clearRolls and its
    #       current state to 'disabled'
    self.__reset=Button(self.__resultFrame,text="Reset",command=self.clearRolls)
    self.__reset.config(state="disabled")

    # 12. Create static result Label
    self.__resultLabel=Label(self.__resultFrame,text="You rolled:")

    # 13. Create sum IntVar and initialize to 0
    self.__sum=IntVar()
    self.__sum.set(0)

    # 14. Create dynamic result value label
    self.__resultValue=Label(self.__resultFrame,textvariable=self.__sum)

    # 15. Pack widgets into result frame
    self.__reset.pack(side="left")
    self.__resultLabel.pack(side="left")
    self.__resultValue.pack(side="left")

    # 16. Pack result frame into main window
    self.__resultFrame.pack()


    #--------------------------------------------------------------------------

    # 17. Create dice label frame
    self.__diceLabelFrame=Frame(self.__win)

    # 18. Create static dice labels
    self.__diceSeparator = Label(self.__diceLabelFrame,
      text = '---------------------------')
    self.__diceLabel = Label(self.__diceLabelFrame, \
                       text = 'DICE')

    # 19. Pack dice label into dice label frame
    self.__diceLabel.pack()

    # 20. Pack dice label frame into main window
    self.__diceLabelFrame.pack()

    #--------------------------------------------------------------------------

    # 21. Create the dice Frame -- but don't pack it yet 
    # Will be packed after number of DieGUI objects to be created is known
    # (See createDice() event handler)
    self.__diceFrame=Frame(self.__win)
    
    #--------------------------------------------------------------------------

    # 22. Start the main loop
    mainloop()
    
#-- Predicates ---------------------------------------------------------

  # 23. Create Predicates

  # Check number of dice and number created count variables
  def allDiceHaveBeenCreated(self):
#    print("before comparison",self.__numberDice,self.__numberCreated)   #debug
#    if int(self.__numberDice) == int(self.__numberCreated):   #debug
#      print("after",self.__numberDice,self.__numberCreated) #debug
    return int(self.__numberDice) == self.__numberCreated

  # Compare roll count with number of dice
  # invoke getValue() (CounterWP)
  def allDiceHaveBeenRolled(self):
    return self.__rollCounter.getValue()==int(self.__numberDice)


#-- Accessors ----------------------------------------------------------

  # 24. Create accessors
  # return diceFrame (Frame) - contains all dice
  def getDiceFrame(self):
    return self.__diceFrame
  
  
  # invoke getValue() (CounterWP)
  # return count (int) of rolls this turn
  def getRollCounterValue(self):
    return self.__rollCounter.getValue()
    


#-- Mutators -----------------------------------------------------------

  # 25. Create Mutators

  def incrementNumberCreated(self):
    self.__numberCreated += 1
##    print(self.__numberCreated) #debug
##    print(self.__numberDice) #debug


  # invoke increment() (CounterWP)
  def incrementRollCounter(self):
    self.__rollCounter.increment()


  # invoke enableRoll() (DieGUI) on each die in collection
  def enableRollButtons(self):
    for each in self.__dice:
      each.enableRoll()


  # invoke getRollValue() (DieGUI)
  # invoke set() (IntVar)
  # invoke config() (Button)
  def sumRolls(self):
    # Sum all rolls by iterating over each die in collection
    # Watch out for str vs. int types
    # Set IntVar to sum
    # Enable reset button
    sumNum = 0
    for i in self.__dice:
      sumNum+=int(i.getRollValue())

    self.__sum.set(sumNum)
    self.__reset.config(state="normal")
 

  #-- EVENT HANDLERS ---------------------------------------------------
    
  # Create collection of dice requested by user
  # invoke:
  #   get() (Entry)
  #   config() (Entry)
  #   delete() (Entry)
  #   isdigit() (str)
  #   append() (list of DiceGUI)
  #   pack() (Frame)
  #   showerror() (messagebox)
  def createDice(self, event):

    # 26. Get number of dice (as string) requested by user from entry box
    self.__numberDice=self.__entry.get()

    # 27. Check that number of dice string is all digits
    if self.__numberDice.isdigit():
    
      # 28. Store as integer if it is
      numberDiceInt=int(self.__numberDice)
    
      # 29. Disable entry box
      self.__entry.config(state="disabled")

      # 30. Loop for number of dice to be created
      for i in range(numberDiceInt):
      
        # 31. Create dieGUI and append to list of dice
        self.__dice.append(dieGUI.DieGUI(self))
        
        # 32. Pack the completed dice frame into the main window  
      self.__diceFrame.pack()
      
    # 33. Otherwise, handle invalid entry
    else: 
      # 34. Warn user
      messagebox.showerror("Invalid Input","You can only input a int")
      # 35. Clear entry box
      self.__entry.delete(0,END)

  # Reset roll counter, sum, all dice
  # invoke:
  #   reset() (CounterWP)
  #   set() (IntVar)
  def clearRolls(self):

    # 36. Reset roll counter and sum
    self.__rollCounter.reset()
    self.__sum.set(0)

    # 37. Loop to reset each die in collection
    for i in self.__dice:
      i.resetDie()

    # 38. Disable reset button
    self.__reset.config(state="disabled")
    

# 39. Create instance of class
DiceGUI()
