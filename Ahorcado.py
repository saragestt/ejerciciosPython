import random
import requests

def obtener_personajes():
    url = "https://rickandmortyapi.com/api/character"
    respuesta = requests.get(url)
    datos = respuesta.json()
    personajes = [personaje['name'] for personaje in datos['results']]
    return personajes

def juego():
    personajes = obtener_personajes()

    palabra = random.choice(personajes).lower()
    adivinadas = "_" * len(palabra)
    intentos = 6

    print("Ahorcado Rick y Morty!")
    print("Adivina el personaje: " + " ".join(adivinadas))

    while intentos > 0:
        letra = input("Introduce una letra: ").lower()

        if letra in palabra:
            adivinadas = "".join([letra if palabra[i] == letra else adivinadas[i] for i in range(len(palabra))])
            print("Bien! El personaje es: " + " ".join(adivinadas))
        else:
            intentos -= 1
            print(f"No está! Te quedan {intentos} intentos.")

        if "_" not in adivinadas:
            print("Has ganado!")
            break

    if intentos == 0:
        print(f"Has perdido! El personaje era: {palabra}")

juego()