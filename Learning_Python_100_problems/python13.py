###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""

sentence = raw_input("Enter the sentence: ")
l=0
d=0

for i in sentence:
    if i.isdigit():d+=1
    elif i.isalpha(): l+=1
    
print 'LETTERS', l, '\nDIGITS', d







