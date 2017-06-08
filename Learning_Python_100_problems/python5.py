###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

""" Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class StringOperation(object):
	
	def __init__(self):
	    self.string = ""
	    self.caps = ""
	    
	def getString(self):
		self.string = raw_input("Enter the String:")

	def printString(self):
		self.caps = self.string.upper()
		print self.caps

def main():
    obj = StringOperation()
    obj.getString()
    obj.printString()
    
    
if __name__ == "__main__":
    main()
