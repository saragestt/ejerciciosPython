#Crear un algoritmo que calcule la raíz cuadrada del número que introduzca el
#usuario. Si se introduce un número negativo, debe mostrar un mensaje de
#error.


introduce = int(input("Introduce un numero:\n"))

if introduce > 0:
    print(pow(introduce,0.5))
else:
    print("Error!")