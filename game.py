import json
import keyboard
with open("cards.json", "r", encoding = "utf-8") as f:
    cards = json.load(f)
with open("entity.py", "r", encoding = "utf-8") as p:
    print(p)

print(cards)#"Tovább" = merre megy tovább a játék
for e in cards:
    print(e["Sorszám"])