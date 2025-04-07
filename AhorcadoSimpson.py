import random
import requests


urlSimpsons = "https://thesimpsonsquoteapi.glitch.me/quotes"
respuesta = requests.get(urlSimpsons)
contenido = respuesta.json()
print(contenido)

objeto = contenido[0]

frase = objeto["quote"]
personaje = objeto["character"]

print(frase)

print("Ahorcado de los Simpsons!\n"
      "Adivina el personaje a partir de la frase.")

