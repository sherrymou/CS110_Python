'''
Keni Mou
Kmou1@binghamton.edu
Assignment10 Exercise 1
Lab Section 52
CA Kyle Mille
'''

#Constants
NUM1=54
NUM2=42
DEN1=12
DEN2=24


class Fraction:
  
  # --------------------------------------------------------------------------
  # Constructor

  # param top (int)
  # param bottom (int)
  def __init__(self,top,bottom):     
    self.__num = top        #the numerator is on top
    self.__den = bottom     #the denominator is on the bottom

  # --------------------------------------------------------------------------
  # Accessors

  #return numerator
  def getNum(self):
    return self.__num

  #return denominator
  def getDen(self):
    return self.__den
  
  #get the common factor
  def __gCD(self):
    m = self.__num
    n = self.__den
    while m % n != 0:
      oldm = m
      oldn = n

      m = oldn
      n = oldm% oldn

    return n

  #to invoke +
  #param otherfraction(Fraction)  
  #return the sum
  def __add__(self,otherfraction):
    return self.add(otherfraction)

  #param otherfraction(Fraction)
  #return sum of two fractions
  def add(self, otherfraction):
    newnum = self.__num * otherfraction.getDen() + self.__den * otherfraction.getNum()
    newden = self.__den * otherfraction.getDen()
    fraction = Fraction(newnum, newden)
    fraction.simplify()

    return fraction


  # param otherfraction(Fraction)
  # return ture if both fraction are equal to each other, false otherwise. 
  def isEqualTo(self, otherfraction):
    self.simplify()
    otherfraction.simplify()
    return self.__den() == otherfraction.getDen and self.__num == otherfraction.getNum()
    


  # --------------------------------------------------------------------------
  # Mutators
  
  #simplified fraction
  def simplify(self):
    common = self.__gCD()

    self.__num = self.__num // common
    self.__den = self.__den // common

  # --------------------------------------------------------------------------
  # toString
  def __str__(self):
    return str(self.__num) + "/" + str(self.__den)

  # ----------------------------------------------------------------------------

def main():
  fraction1=Fraction(NUM1,DEN1)
  fraction2=Fraction(NUM2,DEN2)
  print("Fraction1:%s , Fraction2:%s"%(fraction1, fraction2))
  
  print("Test getNum for fraction1", fraction1.getNum())
  print("Test getNum for fraction2", fraction2.getNum())
  print("Test getDen for fraction1", fraction1.getDen())
  print("Test getDen for fraction2", fraction2.getDen())
  
  print("Test add", fraction1.add(fraction2))
  print("Test __add__", fraction1+fraction2)

  fraction1.simplify()
  fraction2.simplify()
  print("Test simplify", fraction1,fraction2)

main()
