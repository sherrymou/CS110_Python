'''
Keni Mou
kmou1@binghamton.edu
Assignment3, exercise2
A52
CA: Kyle Miller
'''

'''
Analysis:
count the number of diagonals of a polygon

Output to monitor:
    diagonals1(flaot) - diagonals calculated by fomula
    diagonals2(Int) - calculated by loop method 1: calculated all the connections and subtract sides number
    diagonals3(int) - calculated by loop method 2. easier way than method 1
    resultChecker(Bool) - Whether 3 numbers are same

Input from keyborad
    sides(str) - sides of the polygon
    
Tasks allocated to Functions:
    diagonalCount:
        diagonals calculated by fomula
    diagonalSub:
        Calcutaed by loop method 1
        calculated all the connections and subtract sides number
    diagonalLoop:
        calculated by loop method 2. easier way than method 1
    compare:
        Check whether the results are same
'''
#Calculate by fomula
#param diagonals(float) - the number of diagonals
def diagonalCount(sidesInt):
    diagonals=sidesInt*(sidesInt-3)/2
    return(diagonals)

#Calculate by loop (method 1, salculated all the connections and subtract sides number)
#param diagonals(int)- the number of diagonals
#param totalConnections(int) - the number of total connections in the polygon
#param diagonals(int)-the number of diagonals
def diagonalSub(sidesInt):
    totalConnections = 0 #initial condition
    for i in range (sidesInt):
        totalConnections= totalConnections + i
    diagonals=totalConnections-sidesInt
    return diagonals

#Calculate by loop (method 2)
def diagonalLoop(sidesInt):
    diagonals= 0 #initial condition
    for i in range(sidesInt): #for every additional side in the polygon,
        diagonals=diagonals+i-1  # there will be n-2 diagonals more
    return (diagonals)

#Compare the results
def compare(value1,value2,value3):
    if value1==value2 and value1 == value3:
        return True
    else:
        return False

#input number of sides and calculate the diagonals
#param sides(Str) - how many sides are there in the polygon
#param sidesInt(Int) - how many sides are there in the polygon
#param diagonals1(flaot) - diagonals calculated by fomula
#param diagonals2(Int) - calculated by loop method 1: calculated all the connections and subtract sides number
#param diagonals3(int) - calculated by loop method 2. easier way than method 1
def main():
    #Get input
    sides=input("How many sides are there in the polygon? Please input a integer number greater than 3.")

    #Change the type
    sidesInt=int(sides)

    #Calculate
    diagonals1=diagonalCount(sidesInt)
    diagonals2=diagonalLoop(sidesInt)
    diagonals3=diagonalSub(sidesInt)

    #Compare the results
    resultChecker = compare(diagonals1, diagonals2, diagonals3)

    #output
    print("There will be", diagonals1, "diagonals")  #debug
    print("There will be", diagonals2, "diagonals")  #debug
    print("There will be", diagonals3, "diagonals")  #debug
    print (resultChecker)

main()

