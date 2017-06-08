###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""


class sevengen():

    def __init__(self):
        self.limit = 1
        
    def getlimit(self):
        self.limit = int(raw_input("Enter the no: "))
        
    def __iter__(self):
        for i in range(1,self.limit):
            if i%7==0:
                yield i
                
                

obj = sevengen()
obj.getlimit()
it = iter(obj)
no = obj.limit/7
if no%7==0:
    no=no-1
    
for i in range(no):
    print it.next()   


        


