'''
Keni Mou
kmou1@binghamton.edu
Lab4
A52
Kyle Miller
'''

'''
Estimates pi using Monte Carlo simulation
Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 4x4 square
Input from keyboard:
  numberDarts (int)
Tasks allocated to functions:
  setUpDartboard()
  drawLine() - to draw axes
  drawSquare() - to outline dartboard
  inCircle() - determine if dot is in circle
  montePi() - simulation algorithm  
'''

import turtle
import math
import random

# param grapher (Turtle)
# param width (int)
# param topLeftX (int)
# param topLeftY (int)
def drawSquare(grapher,width,topLeftX,topLeftY):
  grapher.up()
  grapher.goto(topLeftX,topLeftY)
  grapher.down()
  SIDES=4
  ANGEL=90
  for i in range (SIDES):
    grapher.forward(width)
    grapher.left(ANGEL)
  grapher.up()
  

# Draws line given turtle and endpoints
# param grapher (Turtle)
# param xStart (int)
# param yStart (int)
# param xEnd (int)
# param yEnd (int)
def drawLine(grapher,xStart,yStart,xEnd,yEnd):
  grapher.goto(xStart,0)
  grapher.down()
  grapher.goto(xEnd,0)
  grapher.up()
  grapher.goto(0,yStart)
  grapher.down()
  grapher.goto(0,yEnd)
  grapher.up()

# Sets up 4X4 area with x- and y-axis to simulate dartboard
# param board - window that will simulate board
# param grapher - turtle that will do drawing
def setUpDartboard(board,grapher):
  
  # Draw board
  BOARD_WIDE=2
  board.setworldcoordinates(-BOARD_WIDE,-BOARD_WIDE,BOARD_WIDE,BOARD_WIDE)
  
  SQUARE_WIDE=2
  POINT_POSITION=-1
  drawSquare(grapher,SQUARE_WIDE,POINT_POSITION,POINT_POSITION)

  # Draw x- and y-axes
  drawLine(grapher,-BOARD_WIDE,-BOARD_WIDE,BOARD_WIDE,BOARD_WIDE)

# (Predicate Function)
# Determines whether or not dart falls inside unit circle with center at 0,0
# param dart (Turtle)
# return True if in circle, False if not
def inCircle(dart):
  distance= dart.distance(0,0)
  RADIUS=1
  return distance<= RADIUS


# Algorithm for Monte Carlo simulation
# param numberDarts (int)
# param dart (Turtle)
# return approximation of pi (float)
def montePi(numberDarts,dart):
  # Initialize inCircleCount
  insideCount=0 
  
  # Loop for numberDarts
  for i in range(numberDarts):
  
    # Get random coordinate and position dart
    randx = random.random()
    randy = random.random()
    x = random.choice([randx,-randx])
    y = random.choice([randy,-randy])
    
    # Draw red dot if in circle, blue dot if not
    dart.goto(x,y)
    if inCircle(dart):
      dart.color("red")
      dart.dot(3) #easy to look
      insideCount=insideCount+1
    else:
      dart.color("blue")
      dart.dot(3)

  # return approximation of pi
  radio=4 #coming with the problem
  pi=insideCount/numberDarts*radio
  return pi


#Performs Monte Carlo simulation to generate approximation of Pi
def main():
  # Get number of darts for simulation from user
  numberDartsStr= input("How many darts in the board?")
  numberDarts=int(numberDartsStr)#change formate
  print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")

  #Create window, turtle, set up window as dartboard
  wn = turtle.Screen()
  fred = turtle.Turtle()
  fred.up()
  
  setUpDartboard(wn,fred)
  
  # Update animation periodically instead of for each throw
  wn.tracer(500)

  #Conduct simulation and print result
  pi=montePi(numberDarts,fred)
  print("The approximate value of pi is",pi)
  #Keep the window up until dismissed
  wn.exitonclick()


main()
