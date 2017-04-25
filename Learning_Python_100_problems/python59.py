###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
Question:

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
"""

import re

email = raw_input("Enter the email: ")

cname = re.match("(\w+)@(\w+)\.(com)", email)

print cname.group(2)

