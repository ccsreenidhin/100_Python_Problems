###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question:

Please write a program which count and print the numbers of each character in a string input by console.
Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""

ip = raw_input("Enter the string: ")
d={}
[d.update({i:ip.count(i)}) for i in ip]

for k,v in d.items():
    print ','.join([k,str(v)])

