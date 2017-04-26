###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
2.10

Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
"""

def listofno(a,b):
    li =[]
    for i in range(a,b+1):
        li.append(i**2)
    print li[:5]
        
        
        
listofno(1,20)
