#Crear un algoritmo que pida al usuario un número y le diga si es positivo,
#negativo o cero.


introduce = int(input("Introduce un número:\n"))

if introduce < 0:
    resultado = ("Negativo.")
elif introduce == 0:
    introduce = ("Cero")
else:
    introduce = ("Positivo")

print(f"El resultado es: {introduce}")
