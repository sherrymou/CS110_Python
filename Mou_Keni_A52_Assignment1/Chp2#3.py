'''
Keni Mou
Cs110-A52
kmou1@binghamton.edu

Waiting time calculate

Comment:
I tried the time within 24 hours, more than 24 hours and exactly 24 hours.
And they all worked rightly. 
'''

def main ():
    #Get input
    currentTime = input (" What's the current time? " )
    waitingTime = input (" Number of ours to wait? ")
    
    #Change the type
    currentTimeInt = int (currentTime)
    waitingTime = int (waitingTime)
    
    #Calculate
    alarm = (currentTimeInt + waitingTime)%24
    
    print (alarm)
    
main()
    
