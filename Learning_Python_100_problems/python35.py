###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
2.10

Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.
"""

def dictionary(x,y):
    d = {}
    for i in range(x,y+1):
        d[i] = i**2
    print d.values()
    
dictionary(1,20)
