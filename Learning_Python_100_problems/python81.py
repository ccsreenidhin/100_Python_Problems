###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""

import zlib

ip = raw_input("Enter the data: ")

x = zlib.compress(ip)
print x
print zlib.decompress(x)
