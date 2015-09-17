'''
Keni Mou
CS110- A52
kmou1@binghamton.edu

drawing
'''

def main():
    #Get input
    pointStr=input("How many points do you want to draw?")

    #Change the type
    pointInt=int(pointStr)

    #Set the constant
    lengthInt = int(50) #Easy to change in the future

    #Calculate the angels
    angelInside=(pointInt-2)*180/pointInt
    #angelOutside=360-2*60-angelInside
    angelOutside=240-angelInside

    #Set up the turtle
    import turtle
    wm=turtle.Screen()
    alex=turtle.Turtle()

    #Draw the inside polygon
    for i in range(pointInt):
        alex.forward(lengthInt)
        alex.right(180-angelInside) #In order to turn to the right direction. 

    #Draw the outside shape
    alex.left(60) #Before the loop begin, turn the point into right direction.

    for i in range(pointInt):
        alex.forward(lengthInt)
        alex.right(120)
        alex.forward(lengthInt)
        alex.left(180-angelOutside) #In order to turn to the right direction. 

main()
