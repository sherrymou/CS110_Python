'''
Keni Mou
Kmou1@binghamton.edu
Assignment11 Part3
Lab Section 52
CA Kyle Mille
'''

'''
Notes:  should be accompanied by labeled sketch of GUI interface
        This GUI lives inside its parent's window, so it doesn't have its own
        all names start with self.__

Provides control and view GUI for DieMultiSided model
Models single multi-sided die that can be rolled

Model:
  die (DieMultiSided)
Views:
  rollValueLabel (Label)
  rollValue (StringVar)
Controllers:
  dieLabel (Label)
  numSidesEntryBox (Entry)
  rollButton (Button)
Organizational widgets:    
  parentFrame (Frame)
  dieFrame (Frame)
Other instance objects:    
  parent (DiceGUI) - owner of this instance
  rollValue (StringVar)
Classes Used:
  BadArgument
  DieMultiSided
'''

# 1. define imports
from tkinter import *
import dieMultiSided

# 2. define class
class DieGUI:
  
#-- Constructor ---------------------------------------------------------------
  
  # 3. define constructor, parent parameter
  # param parent GUI (DiceGUI) - owner of this instance
  def __init__(self, parent):

    # 4. Create null model for now (so we have a reference for later)
    
    self.__die =None # Will be created from dieStr.DieMultiSided(sides) 

    # 5. Get parent GUI object and get parent frame from it
    # This objects widgets will live in parent frame or window
    self.__parent = parent
    self.__parentFrame = self.__parent.getDiceFrame() 

    # 6. Create frame for this die
    self.__dieFrame = Frame(self.__parentFrame)

    # 7. Create static label and entry box for creating die
    self.__rollValueLabel=Label(self.__dieFrame, text="Sides")
    self.__numSidesEntryBox=Entry(self.__dieFrame,width=5)
    
    # Bind entry box to createDie event handler
    # User must specify number of sides before creation
    self.__numSidesEntryBox.bind('<Return>', self.createDie)
    
    # 8. Create button controller
    # set event handler to rollDie
    self.__rollButton=Button(self.__dieFrame, text = "Roll",command=self.rollDie)
    self.__rollButton.config(state="disabled")
    
    # 9. Create and set up StringVar and dynamic label viewer
    # Initialize StringVar to '  '
    self.__rollValue=StringVar()
    self.__rollValue.set("  ")
    self.__dieLabel=Label(self.__dieFrame, textvariable=self.__rollValue)

    # 10. Pack the widgets into the dieFrame
    self.__rollValueLabel.pack(side="left")
    self.__numSidesEntryBox.pack(side="left")
    self.__rollButton.pack(side="left")
    self.__dieLabel.pack(side="left")
    
    # 11. Pack the dieFrame into the parent frame
    self.__dieFrame.pack()

#-- Accessors -----------------------------------------------------------------

  #  12. Create Accessors
  
  # return dieFrame (Frame)
  def getFrame(self):
    return self.__dieFrame


  # invoke get() (StringVar)  
  # return rollValue (StringVar)
  def getRollValue(self):
    rollValue=str(self.__die.getValue())
    return rollValue


#-- Mutators ------------------------------------------------------------------

  # 13. Create Mutators
    
  # Reset before next turn
  # invoke:
  #  reset() (DieMultiSided)
  #  set() (StringVar)
  #  __str__() (DieMultiSided)
  #  enableRoll() (self)
  def resetDie(self):
    self.__die.reset()
    self.__rollValue.set(" ")
    self.enableRoll()

  # Enable rollButton after all dice have been created and after each turn
  # invokes:
  #  config (Button)
  def enableRoll(self):
    self.__rollButton.config(state='normal')
    

  #-- EVENT HANDLERs ----------------------------------------------------------

  # Create die with given number of sides
  # invoke:
  #   get() (Entry)
  #   config() (Entry)
  #   __isValid()  (DieGUI)
  #   __str__() (DieMultiSided)
  #   incrementNumberCreated() (DiceGUI)
  #   allDiceHaveBeenCreated() (DiceGUI)
  #   enableRollButtons() (DiceGUI)
  def createDie(self, event):
    # 14. Get number of sides on die string from entry box
    rollValueStr=self.__numSidesEntryBox.get()

    try:
      # 15. Check for invalid entry (e.g.,number of sides str isn't all digits)
      # and if so, Raise BadArgument exception
      
      if not dieMultiSided.isValid(rollValueStr):
        raise dieMultiSided.BadArgument
      
      # 16. Create model and disable entry box
      self.__die=dieMultiSided.DieMultiSided(int(rollValueStr))
      self.__numSidesEntryBox.config(state = 'disabled')

      # 17. Let parent know that another die has been created
      self.__parent.incrementNumberCreated()
#      print("line 156") #debug
      
      # 18. Have parent enable all roll buttons if all dice have been created
      if self.__parent.allDiceHaveBeenCreated():
#        print("line 160") #debug
        self.__parent.enableRollButtons()
#        print("line 162") #debug
        
    # 19. invalid entry
    except dieMultiSided.BadArgument as err:  
      # 18. Warn user, clear entry box
      messagebox.showerror(err.getTitle(), str(err)) 
    
  # Roll die, set value, increment parent's roll counter, disable button
  # Sum rolls if all other dice have been rolled
  # invoke:
  #   roll() (DieStr)
  #   set() (StringVar)
  #   __str__() (DieMultiSided)
  #   config() (Button)
  #   incrementRollCounter() (DiceGUI)
  #   allDiceHaveBeenRolled() (DiceGUI)
  #   sumRolls() (DiceGUI)
  def rollDie(self):
    # 19. Roll the die and set the StringVar with the die value
    self.__die.roll()
    rollValue=str(self.__die.getValue())
    self.__rollValue.set(rollValue)

    # 20. Let parent know that die has been rolled and disable roll button
    self.__parent.incrementRollCounter()
    self.__rollButton.config(state='disabled')
    
    # 21. Have parent sum the rolls if all dice have been rolled
    if self.__parent.allDiceHaveBeenRolled():
      self.__parent.sumRolls()

 
'''
# -----------------------------------------------------------------------------

# Test Class
# Write minimal parent GUI class for testing purposes
class Parent:
  def __init__(self):
    # Create window and test widget frame
    self.__win = Tk()
    self.__parentWidgets = Frame(self.__win)

    # Create labels and IntVar for sum (of one die)
    self.__sumLabel = Label(self.__parentWidgets, text = 'sum')
    self.__sumVar = IntVar()
    self.__sumVar.set(0)
    self.__sumValue = Label(self.__parentWidgets, textvariable = self.__sumVar)

    # Pack widgets, pack frame
    self.__sumLabel.pack(side = 'left')
    self.__sumValue.pack(side = 'left')
    self.__parentWidgets.pack()

    # Create frame for die GUI, create die GUI   
    self.__diceFrame = Frame(self.__win)
    self.__die = DieGUI(self)

    # Pack frame for die GUI
    self.__diceFrame.pack()

    # Start listener
    mainloop()
    
  # ---------------------------------------------------------------------------
  # Write stubbed versions of all necessary parent GUI methods
  # For testing purposes there will only be one die GUI at a time, so write as
  #   little code as possible

  # return the frame that will hold the die GUIE
  def getDiceFrame(self):
  #  print(1)
    return self.__diceFrame

  # Only one will be created
  def incrementNumberCreated(self):
  #  print(2)
    return 1

  # Only one will be rolled per turn
  def incrementRollCounter(self):
  #  print(3)
    return 1

  # return True since the only one has been rolled
  def allDiceHaveBeenRolled(self):
  #  print(4)
    return True

  # return True since the only one has been created  
  def allDiceHaveBeenCreated(self):
  #  print(5)
    return True

  # turn is over after one roll
  def enableRollButtons(self):
  #  print(6)
    self.__die.enableRoll()

  # only one has been rolled
  def sumRolls(self):
  #  print(7)
    self.__sumVar.set(int(self.__die.getRollValue().strip()))
    self.enableRollButtons()


# -----------------------------------------------------------------------------

# Write main() tester class to create parent GUIS to exercise one at a time
def main():
  reg1 = Parent() # create 4-sided die
  # Press <Enter> after entering 4 in the entry box
  # Keep on rolling until you are satisfied that it generates all values from
  #   1-4 inclusive and only those values
  # Click the x in the right-hand corner of the window when you are satisfied
  
  reg2 = Parent() # create 6-sided die
  # Press <Enter> after entering 6 in the entry box
  # Keep on rolling until you are satisfied that it generates all values from
  #   1-6 inclusive and only those values
  # Click the x in the right-hand corner of the window when you are satisfied
  
  reg3 = Parent() # create 12-sided die
  # Press <Enter> after entering 12 in the entry box
  # Keep on rolling until you are satisfied that it generates all values from
  #   1-12 inclusive and only those values
  # Click the x in the right-hand corner of the window when you are satisfied
  
  bad  = Parent() # create 3-sided die
  # Press <Enter> after entering 3 in the entry box
  # It should not be possible to create a die with less than 4 sides
  # Click the x in the right-hand corner of the window when you are satisfied  

main()


'''

  
