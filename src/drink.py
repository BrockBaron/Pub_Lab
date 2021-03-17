class Drink:
    def __init__(self, name, price, alcohol):
        self.name = name
        self.price = price
        self.alcohol = alcohol
        

    def get_price(self):
        return self.price

    def get_alcohol(self):
        return self.alcohol
