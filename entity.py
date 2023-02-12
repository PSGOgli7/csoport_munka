import random
class Entity:
    def __init__(self, name, hp=0, dex=0, luck= 0):
        if hp == 0:
            self.hp = random.randrange(1, 6) + random.randrange(1, 6) + 12
        else:
            self.hp = hp
        
        if dex == 0:
            self.dex = random.randrange(1, 6) + 6
        else:
            self.dex = dex
        
        if luck == 0:
            self.luck = random.randrange(1, 6) + 6
        else:
            self.luck = luck
        
        self.name = name
    
    def __repr__(self):
        if self.luck == -1:
            return f"{self.name}, Életerő: {self.hp}, Ügyesség: {self.dex}"    
        return f"{self.name}, Életerő: {self.hp}, Ügyesség: {self.dex}, Szerencse: {self.luck}"


player = Entity("Sanyi")
print(player)

mob = Entity("Tolvaj", 6, 7, -1)
print(mob)