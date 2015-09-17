'''
Keni Mou
Kmou1@binghamton.edu
Kristy Stevens
ksteven4@binghamton.edu
Final Project 3/7
Lab Section 52
CA Kyle Mille
'''

#This part is written by Keni

'''
Notes:
To output the strings to a file
name the file by the current time
'''
import time
import tkinter.messagebox 

WRITE_MODE="w"

def outputToFile(content):
  filename=getTime()

  #write into file handler
  try:
    outputfile = open("%s.txt"%(filename), WRITE_MODE)

    try:
      outputfile.write(content)
      tkinter.messagebox.showinfo("Message from Timer","Output successful!")

    except IOError as err: # inner exception handler for outfile processing
      print("\nProblem writing data: \n" + str(err))
    except ValueError as err:  # inner exception handler for outfile processing
      print("\nProblem writing data, wrong format or corrupted?  \n" + str(err) + '\n')
    except Exception as err: # inner exception handler for outfile processing
      print("\nData cannot be written to file: \n" + str(err) + '\n')
    finally:# will close file whether or not exception has been raised
      outputfile.close()


  except IOError as err: # "outer" exception handler for outfile open
    print("\nExecption raised during open of output file, no write performed: \n" + str(err) + '\n')
  except Exception as err: # outer exception handler for outfile processing
    print("\nData cannot be read:  \n" + str(err) + '\n')

def getTime():
  currentTime=time.strftime("%a_%d_%b_%Y_%H_%M_%S_output_from_~Timer~",\
                         time.gmtime())
  return currentTime

