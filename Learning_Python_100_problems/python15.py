###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

no = int(raw_input("Enter the no: "))

val=0
x = 4

for i in range(x):
    y=0
    for j in range(i+1):
        y += (no*(10**j))
    val+=y

print val
