'''
Keni Mou
Kmou1@binghamton.edu
Lab9, Excerise 1-3
Lab Section 52
CA Kyle Mille
'''

'''
Analyze
  To compute the max rain fall, min rain fall, and average rain fall
  use readlines() method

Output to the monitor:
  maxrain(float)
  minrain(float)
  average(float)

Input from keyboard:
  filename(str)

Tasks:
  getMax
    to get the max rainfall
  getMin
    to get the min rainfall
  getAverage
    to get the average rainfall
'''

#Constants
READ="r"

#get the max rainfall
#param rainValue(float)
#param maxrain(float)
#return maxrain(float)
def getMax(rainValue,maxrain):
  if rainValue > maxrain:
    maxrain = rainValue
  return maxrain

#get the min rainfall
#param rainValue(float)
#param minrain(flaot)
#return minrain(float)
def getMin(rainValue,minrain):
  if rainValue < minrain:
    minrain = rainValue
  return minrain

#get the average rainfall
#param theSum(float)
#param theCounter(int)
#return average(flaot)
def getAverage(theSum,theCounter):
  return theSum/theCounter
  

#Get the file, compute the needed values with readlines method
def main():
  #get the file
  filename=input("Please enter file name containing rainfall data: ")
  rainfall=open(filename,READ)

  #initialization
  maxrain=0
  minrain=1000000000
  theSum=0
  theCounter=0

  #read lines and compute 
  lines=rainfall.readlines()
##  print(lines) #debug
  for line in lines:
    values=line.split()

    rainValue=float(values[1])

    maxrain=getMax(rainValue, maxrain)
    minrain=getMin(rainValue, minrain)
      
    theSum+=rainValue
    theCounter+=1

  average=getAverage(theSum, theCounter)

  #display
  print("Max rain fall is %.2f"%(maxrain), "Min rain fall is %.2f"%(minrain),'\n'\
        "The average is %.2f"%(average))
main()
