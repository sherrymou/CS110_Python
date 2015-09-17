'''
Keni Mou
kmou1@binghamton.edu
Assignment3, exercise3
A52
CA: Kyle Miller
'''

'''
this is the main() of #1
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
'''
import summations
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
    handShake1=summations.handShakeCount(peopleInt)
    handShake2=summations.handShakeLoop(peopleInt)

    #Compare the results
    resultChecker = summations.compare(handShake1, handShake2)

    #output
    print("There will be", handShake1, "hand shakes")  #debug
    print("There will be", handShake2, "hand shakes")  #debug
    print (resultChecker)

main()

