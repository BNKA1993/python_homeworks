from adress import Address

class Mailing:
    
    def __init__(self, to_adress, from_adress, cost:int, track:str):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.cost = cost
        self.track = track