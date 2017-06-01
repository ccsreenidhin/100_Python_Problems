###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

""" Question 9
Level 2

Question??
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

print "Enter the Lines"
lines =[]
while(1):
    line = raw_input()
    if line:
        lines.append(line)
    else:
        break
        

for i in lines:print i.upper()
        


