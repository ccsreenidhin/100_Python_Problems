###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
Define a custom exception class which takes a string message as attribute.
"""

class CustomException:
    
    def __init__(self, msg):
        self.msg = msg
    

try:
    raise CustomException("error")
  
except CustomException:
    print "hi"
    
  
  
