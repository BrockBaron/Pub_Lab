import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):                                   
        self.customer1 = Customer("Ally", 100, 40)
        self.customer2 = Customer("Peter", 20, 32)
        
    
    #@unittest.skip("Delete this line to run the test")
    def test_customer_wallet(self):
        self.assertEqual(20, self.customer2.get_wallet())


    #@unittest.skip("Delete this line to run the test")
    def test_remove_cash(self):
        self.customer1.remove_cash(8.50)
        self.assertEqual(91.50, self.customer1.get_wallet())








