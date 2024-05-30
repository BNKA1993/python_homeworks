class User:
    
    __age = 0;
    
    def __init__(self, name):
        print("Я создался")
        self.username = name
    
    def sayName(self):
        print("Меня зовут ", self.username)
        
    def sayAge(self):
        print(self.__age)
    
    def setAge(self, newAge):
        self.__age = newAge
        
    def addCard(self, card):
        self.card = card
        
    def getCard(self):
        return self.card