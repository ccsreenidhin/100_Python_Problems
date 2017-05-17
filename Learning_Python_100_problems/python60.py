###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
Question:

Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
"""

words = [i for i in raw_input("Enter the line: ").split(' ') if i.isdigit()]

print words


        
