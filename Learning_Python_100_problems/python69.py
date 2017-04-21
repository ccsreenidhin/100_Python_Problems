###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
Question:

Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
"""

def divis(n):
    for i in range(n):
        if i%5==0 and i%7==0:
            yield i
            
li =[]        
for i in divis(50):
    li.append(str(i))
    
print ','.join(li)
   
