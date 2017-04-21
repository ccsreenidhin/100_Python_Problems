###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
"""

no = int(raw_input("Enter the no: "))

series = [0,1]
series += [series.append(series[-1]+series[-2]) for i in range(no-1)]

print filter(lambda x: x!= None, series)
