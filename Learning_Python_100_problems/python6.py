###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

""" Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

def calculation(d):
    C_val = 50
    H_val = 30
    q = ((2 * C_val * d)/ H_val)**(1/2.0)
    return int(q)



D = raw_input("Enter the nos:")
d = map(int, D.split(','))
q = map(calculation, d)
print q

