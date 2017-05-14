###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

nos = [i for i in range(1000, 3001) if all(not(int(j)%2) for j in str(i))]

print nos





