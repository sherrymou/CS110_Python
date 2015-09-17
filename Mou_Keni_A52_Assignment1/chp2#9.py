'''
Keni Mou
Cs110-A52
kmou1@binghamton.edu

Area of a rectangle

Comment:
I tried some values and the results are all same as what I got by my calculator.
'''


def main():
    #Get input
    width=input("Write down the width of your rectangle")
    height=input("Write down the hight of your rectangle")

    #Change the type
    widthInt=int(width)
    heightInt=int(height)

    #Calculate
    area=widthInt*heightInt
    
    print("The area of your rectangle is",area)
main()
