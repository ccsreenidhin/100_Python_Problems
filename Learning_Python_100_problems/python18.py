###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question 18
Level 3

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""

passwords = raw_input("Enter the Passwords: ").split(',')

test = {'small':0,'caps':0,'digits':0,'special':0}
p = []

for password in passwords:
    test = dict.fromkeys(test.iterkeys(),0)
    if len(password)>=6 and len(password)<=12:
        for i in password:
            if i.isalpha() and i.islower():
                test['small']+=1
            elif i.isalpha() and i.isupper():
                test['caps']+=1
            elif i.isdigit():
                test['digits']+=1
            elif i in ['$','#','@']:
                test['special']+=1
        if all(test.itervalues()):p.append(password)
        
        
for n in p:print n
