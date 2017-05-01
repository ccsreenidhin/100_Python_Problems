###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

sentence =  raw_input("Enter the sentence: ")
u=0
l=0
for i in sentence:
    if i.isalpha():
        if i.isupper():u+=1
        else:l+=1
        

print 'UPPER CASE', u, '\nLOWER CASE', l
