#Programa que cargue desde teclado una tabla de enteros de dimensión 3x4. El
#programa mostrará la fila en la que la suma de sus elementos sea mayor.

tabla = []

for i in range(3):
    filaT = ([])
    for j in range(4):
        introduce = int(input(f"Introduce los valores({i+1},{j+1}):\n"))
        filaT.append(introduce)
    tabla.append(filaT)


def filaMayor(tabla, filas, columnas):
    sumaMax = 0
    fila = 0
    for i in range(filas):
        sumaFila = 0
        for j in range(columnas):
            sumaFila += tabla[i][j]
        if sumaMax == 0 or sumaFila > sumaMax:
            sumaMax = sumaFila
            fila = i
    return fila, sumaMax

filas = 3
columnas = 4


fila, sumaMax = filaMayor(tabla, filas, columnas)

print("Matriz ingresada:")
for fila in tabla:
    print(fila)

print(f"La fila mayor es: {fila}\n"
      f"Suma total de: {sumaMax}")