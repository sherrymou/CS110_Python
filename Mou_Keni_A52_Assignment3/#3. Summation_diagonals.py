'''
Keni Mou
kmou1@binghamton.edu
Assignment3, exercise3
A52
CA: Kyle Miller
'''

'''
this is the main() of #2
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
'''


import summations

def main():
    #Get input
    sides=input("How many sides are there in the polygon? Please input a integer number greater than 3.")

    #Change the type
    sidesInt=int(sides)

    #Calculate
    diagonals1=summations.diagonalCount(sidesInt)
    diagonals2=summations.diagonalLoop(sidesInt)
    diagonals3=summations.diagonalSub(sidesInt)

    #Compare the results
    resultChecker = summations.compare(diagonals1, diagonals2, diagonals3)

    #output
    print("There will be", diagonals1, "diagonals")  #debug
    print("There will be", diagonals2, "diagonals")  #debug
    print("There will be", diagonals3, "diagonals")  #debug
    print (resultChecker)

main()

