import json
import random
from entity import Entity

with open("cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)
with open("entity.py", "r", encoding="utf-8") as p:
    print(p)
player = Entity("sanyi")

json = cards
sorszam = 1
while True:
  print(json[sorszam-1]['Szöveg'])
  if json[sorszam-1]['Esemény'] == 'Harc':
      if "Mobcopy" in json[sorszam - 1]:
          mob = Entity("Tükörkép", player.dex, player.hp-2, -1)
      else:
        mobj = json[sorszam-1]['Mobs']['Mob1']
        mob = Entity(mobj[0], mobj[1], mobj[2], mobj[3])
      if "Mob2" in json[sorszam-1]['Mobs']:
          mobj2 = json[sorszam - 1]['Mobs']['Mob2']
          mob2 = Entity(mobj2[0], mobj2[1], mobj2[2], mobj[3])
          if not player.attack(mob2):
              break
      if not player.attack(mob):
         break
      else:
          valasz = int(input("Válassz: "))
          if len(json[sorszam - 1]['Tovabb']) <= valasz or valasz == 0:
              print('Ez nem opció.')
              continue
          sorszam = json[sorszam - 1]['Tovabb'][valasz]
  # válasz lehetőségek kiírása json[sorszam-1]['Tovabb'] alapján
  elif json[sorszam-1]['Esemény'] == 'Ugras':
      valasz = int(input("Válassz: "))
      if len(json[sorszam - 1]['Tovabb']) <= valasz:
          print('Ez nem opció.')
          continue
      if "Vege" in json[sorszam - 1]['Tovabb']:
          break
      sorszam = json[sorszam - 1]['Tovabb'][valasz]
      if "Alaphurt" in json[sorszam - 1]:
          player.hplevonas(json[sorszam - 1]['Alaphurt'][0])
      if "Szerhurt" in json[sorszam - 1]:
          player.lucklevonas(json[sorszam - 1]['Szerhurt'][0])
      if "Dexhurt" in json[sorszam - 1]:
          player.lucklevonas(json[sorszam - 1]['Dexhurt'][0])
      if "Szerencseprob" in json[sorszam - 1]:
          if player.tryluck():
              print("Siker!")
              sorszam = json[sorszam - 1]['Tovabb'][2]
          else:
              print("Nem sikerült.")
              sorszam = json[sorszam - 1]['Tovabb'][1]


      if sorszam == 49:
          if player.luck < 6:
              player.luck = 6
  #válasz ellenőrzése, hogy benne van-e a továbban

print('Vége a játéknak!')