'''
Keni Mou
CS110-A52
kmou1@binghamton.edu

Number of diagonals inside a polygon

'''

def main():
    #Get input
    numberOfSides=input("How many sides are there in the polygon? Please input a integer number greater than 3.")

    #Change the type
    sidesInt=int(numberOfSides)

    #Calculate
    diagonals=sidesInt*(sidesInt-3)/2

    #output
    print ("There are", diagonals, "diagonals")

main()
