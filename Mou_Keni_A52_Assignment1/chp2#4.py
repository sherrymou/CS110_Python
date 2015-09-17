'''
Keni Mou
Cs110-A52
kmou1@binghamton.edu

Day calculate

Comment:
I tried the day within 7 days, exactly 7 days and more than 7 days,
they all worked correctly. 
'''

def main():
    #Get input
    Day = input ("What day is it today? (0 is Sunday and 6 is Saturday)")
    Days = input (" How many days you want to stay?")
    
    #Change the type
    DayInt = int(Day)
    DaysInt = int(Days)
    
    #Calculate 
    ReturnDay = (DayInt + DaysInt)%7

    print (ReturnDay)
main()

