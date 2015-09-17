'''
Keni Mou
Kmou1@binghamton.edu
Assignment10 Exercise 2
Lab Section 52
CA Kyle Mille
'''

from point import Point

#CONSTANTS
DOUBLE=2
HALF=0.5

LOC_POINT_X=3
LOC_POINT_Y=5
WIDTH=10
HEIGHT=20

CHE_POINT_X=4
CHE_POINT_Y=25


class Rectangle:
  """Rectangle class using Point, width and height"""

  # --------------------------------------------------
  # Constructor

  # param initP(Point)
  # param initW(floar)
  # param initH(floar)
  def __init__(self,initP,initW,initH):
    self.__location = initP
    self.__width = initW
    self.__height = initH

  # ----------------------------------------------------
  # Accessors

  # return width
  def getWidth(self):
    return self.__width

  # return height
  def getHeight(self):
    return self.__height

  # return perimeter
  def perimeter(self):
    return self.__width*DOUBLE + self.__height*DOUBLE

  # return diagonal
  def diagonal(self):
    diagonal = (self.__width**DOUBLE + self.__height**DOUBLE)**HALF
    return diagonal

  # return area
  def area(self):
    return self.width * self.height

  # param point(Point)
  # return true if the point is inside the rectangle
  def encloses(self, point):
    return point.getX()>self.__location.getX() and \
           point.getX() < (self.__location.getX()+ self.__width) and \
           point.getY()>self.__location.getY() and \
           point.getY() < (self.__location.getY()+ self.__height)

  # ---------------------------------------------------
  # Mutators

  # transpose
  def transpose(self):
    temp = self.__width
    self.__width = self.__height
    self.__height = temp

  # ---------------------------------------------
  # toString
  def __str__(self):
    return "Point: %s, Width: %s, Height: %s"% \
           (self.__location, self.__width, self.__height)

  
  #----------------------------------------------------------
def main():
  #create a rectangle object
  rectangle=Rectangle(Point(LOC_POINT_X,LOC_POINT_Y),WIDTH,HEIGHT)
  point=Point(CHE_POINT_X,CHE_POINT_Y)
  print("rectangle:",rectangle)

  print("Test getWidth and getHeight")
  print("Width: %s, Height: %s"% (rectangle.getWidth(),rectangle.getHeight()),'\n')

  print("Test perimeter")
  print(rectangle.perimeter(),'\n')
  
  print("Test transpose")
  rectangle.transpose()
  print(rectangle,'\n')

  print("Test diagonal")
  print(rectangle.diagonal(),'\n')
        
  print("Test encloses, point:%s"%(point))
  print(rectangle.encloses(point))

  

main()
