###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question:

Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
"""

class Person:
    def __init__(self):
        self.gender = "Unknown"
    def getgender(self):
        return self.gender
    
 
class Male(Person):
    def __init__(self):
        self.gender = "Male"
    def getgender(self):
        return self.gender
    
    
class Female(Person):
    def __init__(self):
        self.gender = "Female"
    def getgender(self):
        return self.gender
        
        
male = Male()
female = Female()
person = Person()

print male.getgender()
print female.getgender()
print person.getgender()

