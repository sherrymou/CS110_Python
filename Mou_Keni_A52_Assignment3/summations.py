'''
Keni Mou
kmou1@binghamton.edu
Assignment3, exercise3
A52
CA: Kyle Miller
'''

'''
This is the module 
'''

'''
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

    handShakeCount:
        Calculate by fomula
    handShakeLoop:
        Calcutaed by loop
    compare:
        Check whether both results are same
'''

'''
diagonals part
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

'''
hand shake part
'''

#Calculate by fomula
#param handShake(Int)- how many times handshake happens
def handShakeCount(peopleInt):
    handShake=peopleInt*(peopleInt-1)/2
    return(handShake)

#Calculate by loop
def handShakeLoop(peopleInt):
    handShake=0 #initial condition
    for i in range(peopleInt): #for every additional people in the classroom,
        handShake=handShake+i  # there will be n-1 handshakes more
    return handShake

#Compare the two results
def compare(value1,value2):
    if value1==value2:
        return True
    else:
        return False
