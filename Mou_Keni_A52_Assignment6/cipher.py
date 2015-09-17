'''
Keni Mou
Kmou1@binghamton.edu
Assignment 6, Exercise 1
Lab Section 52
CA Kyle Mille
'''

"""
Analysis
  to encrypt or decrypt a cipher

Output to monitor:
  processedMessage(str)

Input from keyboard:
  operator(str)
  rotationKey(int)

Tasks allocated to functions:
  operationValidated: Check that requested operation is valid
  rotationKeyValidated: Check that rotation key is of form <digits> or -<digits> or +<digits>
  convertRotationKey: Convert rotation key to value usable for requested operation
  keepInBounds: Perform string modulus operation to prevent processed character
  processMessage: Encrypt or decrypt message using rotationKey

"""    


#Initialize constants ---------------------------------------------------------

OPERATIONS = "edED"
DECRYPT_STR= "Dd"
ENCRYPT = 1
DECRYPT = -1

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
  rotationKey=int(rotationKeyStr)
  if op in DECRYPT_STR:
    rotationKey = DECRYPT * rotationKey
  else:
    rotationKey = ENCRYPT * rotationKey

##  print (rotationKey) #debug
  return rotationKey


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
# invoke
#        keepInBounds() 
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
      


# Main -----------------------------------------------------------------------

# Gets plain text or cipher code, operation requested (encrypt or decrypt),
#   and rotation key for Caesar cipher
# Generates cipher code or plain text
def main():
  # Describe program
  print("This program encrypts or decrypts messages " + \
        "using a Caesar cipher")

  # Priming read and repeat
  operator=input("Please enter either 'e' to encrypt or 'd' to decrypt \n"\
                 "or press ENTER to quit")
  while operator !="" :
    while not operationValidated(operator):
      operator=input("Invalid input! Please enter either 'e' or 'd'")
                
    # Get remaining inputs, validate and convert as necessary
                
    #deal with the rotation key
    rotationKeyStr=input("Please enter the rotation Key")
    while not rotationKeyValidated(rotationKeyStr):
      rotationKeyStr=input("Invalid input! Please try agian.")

    rotationKey=convertRotationKey(operator, rotationKeyStr)

    #input the message
    message=input("Please input your message")
                
    # Encrypt or decrypt contents of file
    processedMessage=processMessage(message, rotationKey)

    # Display result
    print("Your prosecced message is \n",\
           processedMessage, '\n')

    # Continuation read
    operator=input("Please enter either 'e' to encrypt or 'd' to decrypt \n"\
                 "or press ENTER to quit")

  print("You ended this program")

main()
