'''
Keni Mou
Kmou1@binghamton.edu
Kristy Stevens
ksteven4@binghamton.edu
Assignment13
Lab Section 52
CA Kyle Mille
'''

'''
This program is to have the user provide min and max populations instead of a
city name, have the query select the city along with its population that meets
this criteria, and have each city/population pair be displayed in descending
order by population

Output:
  query result (str)
  
Input:
  maxima (str)
  minima (str)
  
Classes Used:
  BadArgument
  QueryWorldBD
'''

import sqlite3

# ---------------------------------------------------------------------
'''
User defined exception class (subclass of Exception)
Used to signal program that query should not be issued
'''

class BadArgument(Exception):
  
#-- Constructor --------------------------------------------------------
  
  def __init__(self):
    self.__title = 'Bad Argument'
    self.__message = 'Population should be int and the max cannot be smaller that min'

#-- Accessors ----------------------------------------------------------
    
  # return title (str)
  def getTitle(self):
    return self.__title
    
#-- to String ----------------------------------------------------------
  
  def __str__(self):
    return self.__message

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------



'''
Encapsulates a  population query sent to world database
'''
class QueryWorldDB:
  
  # Connect to database and get cursor
  # param dbName (str)
  def __init__(self, dBName):
    conn = sqlite3.connect(dBName)
    self.__cursor = conn.cursor()
    self.__min = ""
    self.__max = ""
    self.__answer = None

# -- Accessors ---------------------------------------------------------------

  def getAnswer(self):
    return self.__answer

# -- Mutators ----------------------------------------------------------------

  # param  maximum (str)
  # param  minimun (str)
  def setPopulation(self, maximum, minimum):
    self.__max = maximum.strip()
    self.__min = minimum.strip()

  # param result (list)
  def setAnswer(self):
    result = self.__cursor.fetchall()
##    print(result) #debug
    self.__answer = None if result == [] else str(result) 
    
  def isValidRange(self):
    return self.__min.isdigit() and self.__max.isdigit() and \
           int(self.__min)<=int(self.__max)
    
  
  # raises BadArgument Exception if the input is invalid
  def popQuery(self):
    if self.isValidRange():
      self.__cursor.execute("select name, population from city where population \
< ? and population > ?",\
                          (self.__max,self.__min))
    else:
      raise BadArgument()


  # Close connection to db
  def closeConnection(self):
    self.__cursor.close()

# -- toString ----------------------------------------------------------------

  # return result (str)
  def __str__(self):
    return '%s %s %s %s %s \n' % (
      ('The population between' if self.__answer else 'There is no city exist between'),
      self.__min, "and", self.__max,
      ('is'+self.__answer if self.__answer else '')
      )

  
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
 
# Find city between population range
# Only digits are allowed
def main():
  # set up connection and create cursor
  query = QueryWorldDB('worldDB')

  # get input from user (priming read)
  instructor = input("Find the city who meet the population requirment, "\
               "press Enter to continue or press any other keys to quit")
  
  
  # let user get as many results as desired
  while instructor == "":
    maxima = input("Please type the maxium population")
    minima = input("Please type the minum population")
    try:
      # set up and issue query
      query.setPopulation(maxima,minima)
      query.popQuery()
      query.setAnswer()
      # show results
      print(query)
    except BadArgument as err:
      # city input empty or malformed
      print('\n%s: %s\n' % (err.getTitle(), str(err) ))
       
    # let user enter another city (continuation read)
    instructor = input("Find the city who meet the population requirment, "\
               "press Enter to continue or press any other keys to quit")
    
  # close connection to db
  query.closeConnection()

main()
