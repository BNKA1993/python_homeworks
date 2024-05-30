class Card:
    number = "0000 0000 0000 0000"
    valideDate = "01/99"
    holder = "unknown"
    
    def __init__(self, number, date, holder):
        self.number = number
        self.valideDate = date
        self.holder = holder
    def pay(self, amount):
        print("С карты ", self.number, "списали ", amount)