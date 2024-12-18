#Crea un algoritmo que pida un numero y diga al usuario si es positivo, negativo o cero

numero = int(input("Introduce un numero:\n"))

if numero > 0:
    resultado = "Positivo"

elif numero < 0:
    resultado = "Negativo"

elif numero == 0:
    resultado = "0"

print(f"El resultado es: {resultado}")