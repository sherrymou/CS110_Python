'''
Keni Mou
Kmou1@binghamton.edu
Lab5. Exercise 1
Lab Section 52
CA Kyle Mille
'''

'''
Analysis
    Use 3n+1 sequence, count the number of loops until it stop,
    and draw a graph to show it.
    Then give the max number of iteration

Output to monitor:
    i(int)- The number of iterations to get to 1 from the value i
    count(int)- how many iterations
    maxSoFar(int) - the max count number
    result(int) - the number related to maxSoFar
    
Output to window:
    a coordinates and a graph which is describe the i respected to count

Tasks allocated to Functions:
    drawAxis:
        draw the coordinates

    seq3np1
        calculate the 3n+1 sequence from n, terminating when it reaches 1,
        and count the iterations
        
    graphDraw
        graph the number of iterations

    maxChecker
        to determine whether the the current number
        is greater than the max number so far
'''
import turtle

#CONSTANTS
RANGE_START=1
RANGE_END=51
X_AXIS=50
Y_AXIS=120
SEQ_CONSTANT1=2  #the constant according to the function
SEQ_CONSTATN2=3  #the constant according to the function
DOT_SIZE=5

#draw the coordinates
def drawAxis(t):
    t.goto(0,Y_AXIS)
    t.goto(0,0)
    t.goto(X_AXIS,0)
    t.up()

#Calculate the 3n+1 sequence from n, terminating when it reaches 1
#And count the iterations
#param count(int)-to count the number of iteration
def seq3np1(n):
    count=0 # initial condition
    while n != 1:
        if n % SEQ_CONSTANT1 == 0:        # n is even
            n = n // SEQ_CONSTANT1
        else:                            # n is odd
            n = n * SEQ_CONSTATN2 + 1
        count=count+1
    return count

#graph the number of iterations
#param x(int)-the x axis value, reflect the number "i"
#param y(int)-the y axis value, reflect the number "count"
def graphDraw(t,start,end):
    x=0 #initial condition
    for i in range (start,end):
        y=seq3np1(i)
        t.goto(x,y)
        t.dot(DOT_SIZE)
        x=x+1
        
#to determine whether the the current number is greater than the max#
def maxChecker(maxNumber,checkNumber):
    return maxNumber<checkNumber

#to calculate the 3n+1 sequence, show the number of iteration,
#and graph a related diagram, them give the max number of iteration
#and the number which is related to the max number of iteration.
#param maxSoFar(int) - the max count number
#param result(int) - the number related to maxSoFar
def main():
    #set up turtle       
    alex=turtle.Turtle()
    wn=turtle.Screen()
    wn.setworldcoordinates(0,0,X_AXIS,Y_AXIS)

    #draw the axis               
    drawAxis(alex)
    
    maxSoFar=0#initial condition
    #use a loop to calculate a range of numbers
    #and get the max number of iteration
    for i in range(RANGE_START,RANGE_END):
        count=seq3np1(i)
        if maxChecker(maxSoFar,i):
          maxSoFar=count
          result=i
        print ("The number of iterations to get to 1 from the value",i, "is",count)
    print("The greatest number of iteration were", maxSoFar,"for",result)

    graphDraw(alex,RANGE_START,RANGE_END)

main()
  
