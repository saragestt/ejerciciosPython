#Crear un algoritmo que calcule la raíz cuadrada del número que introduzca el usuario. Si
#se introduce un número negativo, debe mostrar un mensaje de error y volver a pedirlo
#(tantas veces como sea necesario).

mete_numero = int(input("Introduce un numero:\n"))

while mete_numero < 0:
    print("Error")
    mete_numero = int(input("Introduce un numero:\n"))

print(pow(mete_numero,0.5))