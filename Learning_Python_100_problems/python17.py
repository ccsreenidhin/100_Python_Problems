###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
??
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""

d=0
w=0
while(1):
    ip = raw_input("Enter the data: ")
    if ip:
        if ip[0]=="D":
            d+=int(ip[2:])
        elif ip[0]=="W":
            w+=int(ip[2:])
    else:
        break
        
print d-w
