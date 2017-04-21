###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
Question:

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
"""



def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i
            
            
n = int(raw_input("Enter the no: "))

x = ((n-2)/2)+1

fn = even(n) 
print ','.join([str(fn.next()) for i in range(x)])


