#Modifica el ejercicio 1 de la PRÁCTICA 2_2 para que el proceso se repita 5 veces (para
#5 alumnos). Además, queremos que se muestre al final del programa la NOTA MEDIA
#DEL GRUPO. Hazlo para números reales.

numero1 = int(input("Introduce la nota del alumno 1:\n"))

if numero1 > 5 or numero1 == 5:
    resultado = "Aprobado"

elif numero1 <= 5:
    resultado = "Suspenso"

print(f"El resultado es: {resultado}")

numero2 = int(input("Introduce la nota del alumno 2:\n"))

if numero2 > 5 or numero2 == 5:
    resultado = "Aprobado"

elif numero2 <= 5:
    resultado = "Suspenso"

print(f"El resultado es: {resultado}")

numero3 = int(input("Introduce la nota del alumno 3:\n"))

if numero3 > 5 or numero3 == 5:
    resultado = "Aprobado"

elif numero3 <= 5:
    resultado = "Suspenso"

print(f"El resultado es: {resultado}")

numero4 = int(input("Introduce la nota del alumno 4:\n"))

if numero4 > 5 or numero4 == 5:
    resultado = "Aprobado"

elif numero4 <= 5:
    resultado = "Suspenso"

print(f"El resultado es: {resultado}")

numero5 = int(input("Introduce la nota del alumno 5:\n"))

if numero5 > 5 or numero5 == 5:
    resultado = "Aprobado"

elif numero5 <= 5:
    resultado = "Suspenso"

print(f"Nota media: {(numero1 + numero2 + numero3 + numero4 + numero5) / 5}")