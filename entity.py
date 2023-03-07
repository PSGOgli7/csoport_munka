import random

class Entity:
    def __init__(self, name, hp=0, dex=0, luck= 0, AT= 20):
        if hp == 0:
            self.hp = self.duplakocka() + 12
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
        self.AT = AT
        self.name = name
    
    def __repr__(self):
        if self.luck == -1:
            return f"{self.name}, Életerő: {self.hp}, Ügyesség: {self.dex}"    
        return f"{self.name}, Életerő: {self.hp}, Ügyesség: {self.dex}, Szerencse: {self.luck}"

    def gethp(self):
        return self.hp

    def getdex(self):
        return self.dex

    def getluck(self):
        return self.luck

    def hplevonas(self, szam):
        self.szam = szam
        self.hp = self.hp - szam

    def dexlevonas(self, szam):
        self.szam = szam
        self.dex = self.dex - szam

    def lucklevonas(self,szam):
        self.szam=szam
        self.luck = self.luck - szam

    def ATconfig(self, szam):
        self.szam=szam
        self.AT = self.AT + szam

    def attack(self, other):
        while self.hp > 0 and other.hp > 0:
            tamadoero1 = self.duplakocka() + other.dex
            tamadoero2 = self.duplakocka() + self.dex
            if tamadoero2 > tamadoero1:
                other.hp = other.hp -2
                print(f"Megsebezted az ellenfeled. Vesztett 2 életerőt. (Életereje: {other.hp})")
                #Szeretnéd felhasználni a szerencsédet?
                if other.hp > 0 and self.kerdes("Szeretnéd próbára tenni a szerencsédet?"):
                    if self.tryluck():
                        other.hp = other.hp -2
                        print(f"Szerencséd volt. Vesztett még 2 életerőt. (Életereje: {other.hp})")
                    else:
                        other.hp = other.hp +1
                        print(f"Balszerencséd volt. Visszakapott 1 életerőt. (Életereje: {other.hp})")
            if tamadoero2 < tamadoero1:
                self.hp = self.hp -2
                print(f"Az ellenfeled megsebzett téged. Veszítettél 2 életerőt. (Életerő: {self.hp})")
                #Szeretnéd felhasználni a szerencsédet?
                if self.hp > 0 and self.kerdes("Szeretnéd próbára tenni a szerencsédet?"):
                    if self.tryluck():
                        self.hp = self.hp +1
                        print(f"Szerencséd volt. Visszakaptál 1 életerőt. (Életerő: {self.hp})")
                    else:
                        self.hp = self.hp -1
                        print(f"Balszerencséd volt. Vesztettél még 1 életerőt. (Életerő: {self.hp})")
        if self.hp > 0:
            print("Az ellenfeled meghalt.")
            return True
        else:
            print("Meghaltál. A játéknak vége.")
            return False
                
    
    def tryluck(self):
        szerencse1 = self.duplakocka() <= self.luck
        self.luck = self.luck -1
        return szerencse1
    
    def duplakocka(self):
        return random.randrange(1, 6) + random.randrange(1, 6)

    def kerdes(self, kerdes1):
        valasz = input(kerdes1 + " (Igen vagy Nem)")
        return valasz.lower() == "igen"
