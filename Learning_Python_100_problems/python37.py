###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
2.10

Question:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
"""

def listofno(a,b):
    li =[]
    for i in range(a,b+1):
        li.append(i**2)
    print li
        
        
        
listofno(1,20)
