'''
Keni Mou
Kmou1@binghamton.edu
Lab10 Exercise 1
Lab Section 52
CA Kyle Mille
'''

import math

# Point class for representing and manipulating
# x,y coordinates. 
class Point:
  # --------------------------------------------------------------------------
  # Constructor

  # param initX (int)
  # param initY (int)
  def __init__(self, initX = 0, initY = 0):
    self.__x = initX
    self.__y = initY

  # --------------------------------------------------------------------------
  # Accessors

  # return value of x (int)
  def getX(self):
    return self.__x

  # return value of y (int)
  def getY(self):
    return self.__y

  # return distance from origin (float)
  def computeDistanceFromOrigin(self):  
    return ((self.__x ** 2) + (self.__y ** 2)) ** 0.5

  # return distance from other point (float)
  def computeDistanceFromPoint(self, otherP):
    dx = (otherP.getX() - self.__x)
    dy = (otherP.getY() - self.__y)
    return math.sqrt(dy**2 + dx**2)

  # return x reflection (Point)
  def createXReflection(self):
    return Point(self.__x, self.__y * -1)

  ## param otherPoinst(Point)
  # return slope to point (float)
  # Note exception handling!
  def computeSlopeFromPoint(self, otherPoint):
    try:
      slope = (self.__y - otherPoint.getY()) / (self.__x - otherPoint.getX())
    except ZeroDivisionError:
      slope = None  
    return slope

  # return slope from origin (float)
  def computeSlopeFromOrigin(self):    
    slope = self.computeSlopeFromPoint(Point(0, 0))
    return slope

  ## param ohterPoint(Point)
  # return y-intercept of line (float)
  def computeYIntercept(self, otherPoint): 
    return self.__y - (self.computeSlopeFromPoint(otherPoint) * self.__x)

  ## param ohterPoint(Point)
  # return coefficients of line (tuple)
  def getLineTo(self, otherPoint):
    slope = self.computeSlopeFromPoint(otherPoint)
    intercept = self.computeYIntercept(otherPoint)
    return (slope, intercept)

  # --------------------------------------------------------------------------
  # Mutators 
   
  # param dx (int)
  # param dy (int)
  def move(self, dx, dy):
    self.__x += dx
    self.__y += dy
    
  # --------------------------------------------------------------------------
  # toString

  # return string representation of Point object (str)
  def __str__(self):
    return "\n(x:%d, y:%d)" % (self.__x, self.__y)

# ----------------------------------------------------------------------------  


# Create point objects and exercise methods
def main():
  #test..
  point1=Point(2,3)
  point2=Point(5,6)
  
  print("Test get x and y", point1.getX(),point1.getY())
  print("Test computeDistanceFromOrigin", point1.computeDistanceFromOrigin())
  print("Test computeDistanceFromPoint", point1.computeDistanceFromPoint(point2))
  print("Test createXReflection", point1.createXReflection())
  print("Test computeSlopeFromOrigin", point1.computeSlopeFromOrigin())
  print("Test computeSlopeFromPoint", point1.computeSlopeFromPoint(point2))
  print("Test computeYIntercept", point1.computeYIntercept(point2))
  print("Test getLineTo", point1.getLineTo(point2))
  print("Test move and str")
  point1.move(4,5)
  print(point1)
    
main()
