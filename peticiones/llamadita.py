import requests

url = "https://thesimpsonsquoteapi.glitch.me/quotes"

contenidoWeb = requests.get(f"{url}")

url = contenidoWeb.json()