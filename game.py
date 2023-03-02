import json
with open("cards.json", "r", encoding = "utf-8") as f:
    cards = json.load(f)
with open("entity.py", "r", encoding = "utf-8") as p:
    print(p)

json = cards
sorszam = 1
while True:
  print(json[sorszam-1]['Szöveg'])
  # válasz lehetőségek kiírása json[sorszam-1]['Tovabb'] alapján
  valasz = int(input("Válassz: "))
  #válasz ellenőrzése, hogy benne van-e a továbban
  sorszam = json[sorszam-1]['Tovabb'][valasz]