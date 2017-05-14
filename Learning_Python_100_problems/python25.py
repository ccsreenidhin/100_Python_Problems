###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.
"""

class example:
    value = 0
    def __init__(self, value):
        self.value = value
        
    def valupdater(self):
        self.value+=1
        
    def valprinter(self):
        print self.value
        

obj = example(3)
obj.valprinter()
obj.valupdater()
obj.valprinter()
