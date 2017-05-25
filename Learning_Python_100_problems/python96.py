###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question:

Please write a program which accepts a string from console and print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld
"""

ip = raw_input("Enter the string: ")

print ''.join([i for i in ip if ip.index(i)%2==0 or ip.index(i)==0])

print ip[::2]
