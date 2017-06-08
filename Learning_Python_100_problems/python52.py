###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
7.2

Question:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return (self.radius**2)*(22/7.0)
        
        

obj = Circle(7)
print obj.area()
