'''
Keni Mou
Kmou1@binghamton.edu
Lab10 Exercise 2
Lab Section 52
CA Kyle Mille
'''

#param m(int)
#param n(int)
#get the common factor
def gcd(m,n):
    while m%n != 0:
      oldm = m
      oldn = n

      m = oldn
      n = oldm%oldn

    return n

  
class Fraction:

    def __init__(self,top,bottom):     
  # --------------------------------------------------------------------------
  # Constructor

  # param top (int)
  # param bottom (int)

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

 

  #param otherfraction(fraction)  
  #return the sum of two fraction
    def add(self,otherfraction):

        newnum = self.__num * otherfraction.__den + self.__den * otherfraction.__num
        newden = self.__den * otherfraction.__den

        common = gcd(newnum,newden)

        return Fraction(newnum//common,newden//common)


  # --------------------------------------------------------------------------
  # Mutators 
  #simplified fraction
    def simplify(self):
        common = gcd(self.__num, self.__den)

        self.__num = self.__num // common
        self.__den = self.__den // common



    
  # --------------------------------------------------------------------------
  # toString
    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

  # ----------------------------------------------------------------------------

def main():
  fraction1=Fraction(1,2)
  fraction2=Fraction(3,6)
  print("Test getNum", fraction1.getNum())
  print("Test getDen", fraction1.getDen())
  print("Test add", fraction1.add(fraction2))
  fraction1.simplify()
  print("Test simplify and str", fraction1)

main()
