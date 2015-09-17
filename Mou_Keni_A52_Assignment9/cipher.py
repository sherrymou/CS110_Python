'''
Keni Mou
Kmou1@binghamton.edu
Assignment 9
Lab Section 52
CA Kyle Mille
'''

"""
Analysis
  to encrypt or decrypt a cipher in a file

Output to file:
  a file contained needed texts
  

Input from keyboard:
  operator(str)
  rotationKey(int)
  fileName(str)

Tasks allocated to functions:
  operationValidated: Check that requested operation is valid
  rotationKeyValidated: Check that rotation key is of form <digits> or -<digits> or +<digits>
  convertRotationKey: Convert rotation key to value usable for requested operation
  keepInBounds: Perform string modulus operation to prevent processed character
  processMessage: Encrypt or decrypt message using rotationKey
  fileNameValidated: Checks that file exists and that extension is .txt
  makeName:Generates output file name from input file name, operation requestedand rotation key
  writeToFile: write text into a file

"""    

import os.path

#Initialize constants ---------------------------------------------------------

# Mapping of valid operations to rotationKey factor
OPERATIONS = {'e':[1,"Encrypted"], 'd':[-1,"Decrypted"]}

# File processing modes
READ_MODE = 'r'
WRITE_MODE = 'w'

# Required file extension
FILE_EXT = ".txt"

# Min and limit ordinals of printable ASCII
PRINTABLE_ASCII_MIN = 32
PRINTABLE_ASCII_LIMIT = 127

# Allowable rotation key prefixes
KEY_PREFIXES = "-+"

# Functions ------------------------------------------------------------------

# Check that requested operation is valid
# param opStr (str) - operation requested
# return  True when valid, False otherwise (bool)
def operationValidated(opStr):
  return opStr in OPERATIONS

# Checks that file exists and that extension is .txt
# param name (str) - file name
# invoke isFile() from module os.path and endswith()
# return True when valid, False otherwise (bool)
def fileNameValidated(name):
  return os.path.isfile(name) and name.endswith(FILE_EXT)


# Generates output file name from input file name, 
#   operation requested and rotation key
# param fileName (str) - input file name
# param operation (str)
# param rotationKey (int)
# invoke str.split(), str.replace() and str.join()
# return output file name (str)
def makeName(fileName, operation, rotationKey):
  nameList = fileName.split(".")
  nameList[0] = nameList[0].replace(OPERATIONS['e'][1], "")
  nameList[0] = nameList[0].replace(OPERATIONS['d'][1], "")
  nameList[0] += (OPERATIONS[operation][1] + str(rotationKey))
  return ".".join(nameList)


# Check that rotation key is of form <digits> or -<digits> or +<digits>
# param rotationKeyStr (str)
# invoke str.isdigit() 
# returns:  True when valid, False otherwise (bool)
def rotationKeyValidated(rotationKeyStr):
  return str.isdigit(rotationKeyStr) or str.isdigit(rotationKeyStr[1:]) and \
           rotationKeyStr[0] in KEY_PREFIXES


# Convert rotation key to value usable for requested operation
# param  op (str) - operation requested 
# param  rotationKeyStr (str)
# invoke int()
# return encryption or decryption rotation key (int)
def convertRotationKey(op, rotationKeyStr):
  return OPERATIONS[op][0]*int(rotationKeyStr)


# Perform string modulus operation to prevent processed character 
# from going out of bounds
# param ordinal (int)
# returns adjusted ordinal of new character (int)
def keepInBounds(ordinal):
  while ordinal>=PRINTABLE_ASCII_LIMIT:
    ordinal=ordinal-PRINTABLE_ASCII_LIMIT+PRINTABLE_ASCII_MIN
  while ordinal <PRINTABLE_ASCII_MIN:
    ordinal=ordinal+PRINTABLE_ASCII_LIMIT-PRINTABLE_ASCII_MIN
  return ordinal 


# Encrypt or decrypt message using rotationKey
# param message (str)
# param rotationKey (int)
# invoke keepInBounds() 
# return processedMessage (str)
def processMessage(message, rotationKey):
  processedMessage=""
  for alpha in message:
    order=ord(alpha)+rotationKey
    while order >= PRINTABLE_ASCII_LIMIT or order<PRINTABLE_ASCII_MIN:
      order=keepInBounds(order)
    alpha=chr(order)
    processedMessage += alpha
  return processedMessage


#write text into a file
#param theFile(file)
#param theText(list)
#reutrn theFile(file)
def writeToFile(theFile,theText):
  for i in theText[:-1]:
    theFile.write(i[:-1])
    theFile.write('\n')
  theFile.write(theText[-1]) #to deal with the newline characters
  return theFile


# Main -----------------------------------------------------------------------

# Gets plain text or cipher code, operation requested (encrypt or decrypt),
#   and rotation key for Caesar cipher
# Generates cipher code or plain text
def main():
  # Describe program
  print("This program encrypts or decrypts entire files at a time using a Caesar cipher")

  #input the file name
  fileName=input("Please input your fileName, or press ENTER to quit.")
  while fileName:
    while not fileNameValidated(fileName):
      fileName=input("That file name does not appear to be valid, please try again")
      
    # get the operator
    operator=input("Please enter either 'e' to encrypt or 'd' to decrypt")
    while not operationValidated(operator):
      operator=input("That operation does not appear to be valid, please try again")
                
                
    #deal with the rotation key
    rotationKeyStr=input("Please enter the rotation Key")
    while not rotationKeyValidated(rotationKeyStr):
      rotationKeyStr=input("Invalid input! Please try agian.")

    rotationKey=convertRotationKey(operator, rotationKeyStr)

    #The crazy exception handling... 
    try: # outer try for infile open
      inFileObject = open(fileName, READ_MODE)

      try: # inner try for processing infile
        contents = inFileObject.readlines()
        convertedText=[]

        #Convert
        for i in contents:
          convertedText+=[processMessage(i, rotationKey)]


          #Write to the file
        try:  # "outer" try for outfile open
          outFileObject = open(makeName(fileName,operator,rotationKey), WRITE_MODE)
          try: # inner try to outfile processing

            #write to the file
            writeToFile(outFileObject,convertedText)

          except IOError as err: # inner exception handler for outfile processing
            print("\nProblem writing data: \n" + str(err))
          except ValueError as err:  # inner exception handler for outfile processing
            print("\nProblem writing data, wrong format or corrupted?  \n" + str(err) + '\n')
          except Exception as err: # inner exception handler for outfile processing
            print("\nData cannot be written to file: \n" + str(err) + '\n')
          finally:# will close file whether or not exception has been raised
            outFileObject.close()

        except IOError as err: # "outer" exception handler for outfile open
          print("\nExecption raised during open of output file, no write performed: \n" + str(err) + '\n')
        except Exception as err: # outer exception handler for outfile processing
          print("\nData cannot be read:  \n" + str(err) + '\n')  


      except IOError as err: # inner exception handler for infile processing
        print("\nProblem reading data: \n" + str(err))
      except ValueError as err: # inner exception handler for infile processing
        print("\nProblem processing data, wrong format or corrupted? \n" + str(err) + '\n')
      except Exception as err: # inner exception handler for infile processing
        print("\nData cannot be read:  \n" + str(err) + '\n')        
      finally:# will close file whether or not exception has been raised
        inFileObject.close()
        
    except FileNotFoundError as err:  # outer exception handler for infile open
      print("\nFile not found:  deleted or in wrong folder?  \n" + str(err) + '\n')
    except IOError as err: # outer exception handler for infile open
      print("\nException raised during open of input file, try a different file: \n" + str(err) + '\n')
    except Exception as err: # outer exception handler for infile open
      print("\nData cannot be read:  \n" + str(err) + '\n') 


    

    # Continuation read
    fileName=input("Please input your fileName, or press ENTER to quit.")

  print("You ended this program")

main()
