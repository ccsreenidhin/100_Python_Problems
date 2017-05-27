###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
Question:


The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.
"""

def febin(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return febin(n-1)+febin(n-2)
        

print febin(7)
