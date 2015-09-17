'''
Keni Mou
Kmou1@binghamton.edu
Assignment 4, Exercise 1
Lab Section 52
CA Kyle Mille
'''

'''
Analysis

Get grade from mark

Output to monitor:
    grade(str)
  
Input from keyboard:
    mark(float)

Tasks allocated to Functions:
    gradeChecker
    Check the mark, determine the mark belongs to which grade     
'''

# Constants
A_LINE = 90
B_LINE = 80
C_LINE = 70
D_LINE = 60

# Check the mark, determine the mark belongs to which grade
# param mark(float)
# param grade(str)
# return the grade of the mark
def gradeChecker(mark):
    if mark >= A_LINE:
        grade = "A"
    elif mark >= B_LINE:
        grade = "B"
    elif mark >= C_LINE:
        grade = "C"
    elif mark >= D_LINE:
        grade = "D"
    else:
        grade = "F"
    return grade


# let user input a mark and check the grade.
def main():
    print("This program is to check your grade from your mark.\n"\
        "The rule is: A(>=90), B(>=80), C(>=70), D(>=60),F(<60)")        

  # Take in user input and convert 
    markStr = input ("Please enter your mark")
    mark = float(markStr)
    
  # Compute
    grade = gradeChecker(mark)

  # Display 
    print("Your mark is ", mark, ",and your grade is ",grade)
main()
