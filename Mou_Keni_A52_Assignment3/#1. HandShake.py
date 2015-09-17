'''
Keni Mou
kmou1@binghamton.edu
Assignment3, exercise1
A52
CA: Kyle Miller
'''

'''
Analysis:
count the number of handshake in the classroom

Output to monitor:
    handShake1(Float)- number calculated by foluma
    handShake2(Int) - number calculated by loop
    resultChecker(Bool) - Whether two numbers are same

Input from keyborad
    people(Int) - number of people in the classroom

Tasks allocated to Functions:
    handShakeCount:
        Calculate by fomula
    handShakeLoop:
        Calcutaed by loop
    compare:
        Check whether both results are same
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

#input number of people and calculate the handshake
#param people(Str) - how many people are there in the classroom
#param peopleInt(Int) - how many people are there in the classroom
#param handShake1(float) - the number calculated by the fomula
#param handShake2(int) - the number calculated by the loop
def main():
    #Get input
    people=input("how many people are there in the classroom? Please input a integer number greater than 1!")

    #Change the type
    peopleInt=int(people)

    #Calculate
    handShake1=handShakeCount(peopleInt)
    handShake2=handShakeLoop(peopleInt)

    #Compare the results
    resultChecker = compare(handShake1, handShake2)

    #output
    print("There will be", handShake1, "hand shakes")  #debug
    print("There will be", handShake2, "hand shakes")  #debug
    print (resultChecker)

main()
