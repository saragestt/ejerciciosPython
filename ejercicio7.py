#Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es
#bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto
#que también sea divisible por 400.

pide_año = int(input("Introduce un año:\n"))

if pide_año %4 == 00 and pide_año %100 != 0 or pide_año %400 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")