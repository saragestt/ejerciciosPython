#Crear un algoritmo que pida al usuario un número y le diga si es positivo,
#negativo o cero.

inserta_numemro = int(input("Introduce un numero:\n"))

if inserta_numemro == 0:
    resultado = ("cero")
elif inserta_numemro <0:
    resultado = ("negativo")
else:
    resultado = ("positivo")

print(f"Es: {resultado}")

