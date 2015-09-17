'''
Keni Mou
Kmou1@binghamton.edu
Assignment7, exercise 2
Lab Section 52
CA Kyle Mille
'''

'''
Analyze
  to build a funcion which has same function as slice

Output to monitor:
  theList(list)
  mySliceList(list)
  defaultList(list)

Input from keyboard:
  item( anything which can be contained in a list)
  sliceStartStr(str)
  sliceEndStr(str)

Tasks allocated to functions:
  mySlice: to cut a piece of list from a whole list
  numberValidation: check if they are possitive int
                     and the start one is smaller than limit one
  equalList: check whether 2 functions are same


'''


#my own slice function
#param aList(list)
#param sliceStart(int)
#param sliceLimit(int)
#return the list
def mySlice(aList,sliceStart,sliceLimit):
  newList=[]
  for index in range (sliceStart, sliceLimit):
    newList += [aList[index]]
##    print(newList) #debug
  return newList

#verify the input
#param startNumber(str)
#param endNumber(str)
#param theList(list)
#return true if they are possitive int and the start one is smaller than limit one
def numberValidation(startNumber,endNumber,theList):
  return str.isdigit(startNumber) and str.isdigit(endNumber) \
         and int(startNumber)<len(theList) and int(endNumber)<=len(theList) \
         and int(startNumber)<int(endNumber)

#compare 2 list whether they are same
#param list1(list)
#param list2(list)
#return ture if they are same
def equalList(list1,list2):
  return list1==list2

#test whether my function is right
def main():  
  item=input("Enter the first element in your list \n"\
               "OR press <Enter> to quit: ")
  #repeat asking
  while item:
    theList=[] #initial
    
    #build the list
    while item: 
      theList+=[item]
      item = input("Enter the next element in your list \n"\
                   "OR press <Enter> to finish:  ")    
    print("Your list is:", theList,'\n')

    #get the values
    sliceStartStr=input("Enter the starting index for the slice \n"\
                     "OR press <Enter> to make a new list")
    while sliceStartStr:  
      sliceEndStr=input("Enter the limit index for the slice: ")
      while not numberValidation(sliceStartStr,sliceEndStr,theList):
        print("One or both of your indices were invalid \n")

        sliceStartStr=input("Enter the starting index for the slice \n"\
                     "OR press <Enter> to make a new list")
        sliceEndStr=input("Enter the limit index for the slice: ")

      sliceStart=int(sliceStartStr)
      sliceEnd=int(sliceEndStr)
      
      #get the list use my own function
      mySliceList=mySlice(theList,sliceStart,sliceEnd)
      defaultList=theList[sliceStart:sliceEnd]

      #display
      print(mySliceList)
      print(defaultList)

      #check the result
      if equalList(mySliceList,defaultList):
        print("Success: slices are equal \n")
      else:
        print("Unsuccess \n")

      sliceStartStr=input("Enter the starting index for another slice \n"\
                          "OR press <Enter> to make a new list")
      
    item=input('\n' "Enter the first element in your list \n"\
               "OR press <Enter> to quit: ") 
    
main()
    
    
