import unittest

from python5 import StringOperation


class TestStringOperation(unittest.TestCase):

    def setUp(self):
        self.obj = StringOperation()

    def test_getString(self):
        #string = self.obj.getString()
        string="hello world"
        self.obj.string = string
        self.obj.printString()
        self.assertEqual(self.obj.caps,string.upper())
                
        
        
if __name__ == "__main__":
        unittest.main()
        
        
    
        
    
        
    
