###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

""" Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""

words = raw_input("Enter the words: ")
liwords = words.split(',')

print(','.join(sorted(liwords)))



