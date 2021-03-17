import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):                                
        self.drink1 = Drink("whisky", 3.40, 3)
        self.drink2 = Drink("lager", 4.10, 2)


    #@unittest.skip("Delete this line to run the test")
    def test_drink_price(self):
        self.assertEqual(3.40, self.drink1.get_price())

    #@unittest.skip("Delete this line to run the test")
    def test_get_alcohol_level(self):
        self.assertEqual(2, self.drink2.get_alcohol())