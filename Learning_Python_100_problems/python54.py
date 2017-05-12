###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################
"""
7.2

Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""

class Shape:
    area = 0
    
    def areas(self):
        return self.area 
    
    
class Square(Shape):
    
    def __init__(self, l):
        self.length = l
        
    def areas(self):
        self.area = self.length**2
        return self.area
        
        
obj = Shape()
objs = Square(5)

print obj.areas()
print objs.areas()


