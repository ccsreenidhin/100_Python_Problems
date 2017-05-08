###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
2.10

Question:
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
"""
def listofno(a,b):
    tup =(a,)
    for i in range(a+1,b+1):
        val = i**2
        tup +=(val,)
    print tup
        
        
        
listofno(1,20)
