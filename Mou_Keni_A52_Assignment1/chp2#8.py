'''
Keni Mou
Cs110-A52
kmou1@binghamton.edu

Area of a circle

Comment:
I tried some values and the results are all same as what I got by my calculator.
But it seems that I can only input integer.
If I set the radius as float, the result will be weird and incorrect. 
'''

def main():
    #Get input
    radius=input("Write down your circle's radius ^_^ ")

    #Change type
    radiusInt=int(radius)

    #Get the pi
    import math
    PI= math.pi

    #Calculate
    area=PI*(radiusInt)**2
    
    print("Your circle's area is",area)
main()

