###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
Question:

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
"""


email = raw_input("Enter email: ")
user = ''
for i in email:
    if i == '@':
        user = email[:email.index(i)]
        
print user
        
