class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        
        self.drinks_list = []
        
    def get_drink_by_name(self, name):
        for drink in self.drinks_list:
            if drink.name == name:
                return drink