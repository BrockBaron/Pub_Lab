import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):                                    #setUp defines a overide of the unit test so it can run before each test and test what we want.
        self.pub = Pub('The Prancing Pony', 100.00)
    
    def test_pub_has_name(self):                                # a test must start eith "test"
        self.assertEqual('The Prancing Pony', self.pub.name)
        
        
        
        
        
        
        