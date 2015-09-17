'''
Keni Mou
Kmou1@binghamton.edu
Lab9, Excerise 1-5
Lab Section 52
CA Kyle Mille
'''

'''
Analyze:
  write a temperature conversion table called tempConv.txt
  
Output to file:
  tempConv.txt
    The table will include temperatures from -300 to 212 degree Fahrenheit
    and their Celsius equivalents.

Tasks:
  fahToCel:
    conver fahrenheit to the celsius
  
'''
#Constant
WRITE="w"
START_POINT=-300
END_POINT=213

#conver fahrenheit to the celsius
#param fah(float)
#return cel(float)
def fahToCel(fah):
  return (fah-32)/1.8

#create the file
def main():
  theFile = open("tempConv.txt", WRITE)

  theFile.write("%10s \t %10s \n"%("Fahrenheit","Celsius"))

  for fah in range(START_POINT, END_POINT):
    cel=fahToCel(fah)
    theFile.write("%10.2f \t %10.2f \n"%(fah,cel))

main()
