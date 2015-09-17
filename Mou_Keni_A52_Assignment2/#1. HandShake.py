'''
Keni Mou
CS10-A52
kmou1@binghamton.edu

Hand shake count

'''

def main():
    #Get input
    people=input("how many people are there in the classroom? Please input a integer number greater than 1")

    #Change the type
    peopleInt=int(people)
    
    #Calculate
    handShake=peopleInt*(peopleInt-1)/2

    #output
    print("There will be", handShake, "hand shankes")

main()
