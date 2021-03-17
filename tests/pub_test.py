import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink


class TestPub(unittest.TestCase):
    
    def setUp(self):                                    #setUp defines a overide of the unit test so it can run before each test and test what we want.
        self.pub = Pub('The Prancing Pony', 100.00)
        self.customer1 = Customer("Ally", 100, 40)
        self.customer2 = Customer("Peter", 20, 32)
        self.drink1 = Drink("whisky", 3.40, 3)
        self.drink2 = Drink("lager", 4.10, 2)
        self.pub.drinks_list = [self.drink1, self.drink2]
    
    #@unittest.skip("Delete this line to run the test")
    def test_pub_has_name(self):                                # a test must start eith "test"
        self.assertEqual('The Prancing Pony', self.pub.name)
   
    #@unittest.skip("Delete this line to run the test")
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)  
    
    #@unittest.skip("Delete this line to run the test")
    def test_drink_by_name(self):
        drink = self.pub.get_drink_by_name("Whisky") 
        self.assertEqual(3.40, drink.price)   
    # def test_add_to_till(self):
    #     self.assertEqual()  
    @unittest.skip("Delete this line to run the test")       
    def test_sell_drink(self):
        self.pub.sell_drink(drink1, customer1)
        self.assertEqual()

        
     
        