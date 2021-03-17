class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        
        self.drunkenness = 0

    def get_wallet(self):
        return self.wallet

    def remove_cash(self, amount):
        self.wallet -= amount
        
        
    
        
        
        
        
        
        
        
    