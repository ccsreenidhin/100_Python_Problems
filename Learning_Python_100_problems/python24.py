###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question 24
Level 1

Question:
    Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function

"""

def printdoc(var):
    """ prints Python built-in functions documents for such as abs(), int(), raw_input()"""
    print abs.__doc__
    print int.__doc__
    print raw_input.__doc__
    print printdoc.__doc__
    
    
printdoc('abs')
