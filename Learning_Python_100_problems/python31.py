###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
2.10


Question:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
"""
li = []
for i in range(2):
    li.append(raw_input("Enter the string: "))
    
    
if len(li[0]) == len(li[1]):
    print li[0]
    print li[1]
else:
    print max(li)
