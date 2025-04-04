import random

import requests

apiRickyMorty = "https://rickandmortyapi.com/api/character/"

personaje = random.randint(1,826)

contenidoWeb = requests.get(f"{apiRickyMorty}{personaje}")

personaje = contenidoWeb.json()
claves = []
valores = []
for c,v in personaje.items():
    claves.append(c)
    valores.append(v)
    
nPista = random.randint(2,5)
print(f"Su {claves[nPista]} es {valores[nPista]}")