#entity osztály betöltése
from entity import Entity

#az entity osztály tesztelése
player = Entity("Sanyi")
print(player)

mob = Entity("Tolvaj", 6, 7, -1)
print(mob)

if player.attack(mob):
    print("Sikeres támadas")
else:
    print("Sikertelen támadás")