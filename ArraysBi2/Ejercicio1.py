#Programa que dibuje un cuadrado mágico de orden impar introducido por el usuario.
#Un cuadrado mágico es aquel en el que sin repetir ningún número, todas las filas,
#columnas y las dos diagonales suman lo mismo.

introduce_filas = int(input("Introduce el numero de filas:\n"))
introduce_columnas = int(input("Introduce un numero columnas:\n"))


cuadrado_magico = []
for i in range(introduce_filas):
    cuadrado_magico.append([])
    for j in range(introduce_columnas):
        posicion = int(input(f"{i} - {j}: "))
        cuadrado_magico[i].append(posicion)

def esMagico(filas,columnas,diagonal,diagonalInversa):
    if diagonal != diagonalInversa:
        return False
    numero_magico = diagonal
    for suma_filas in filas:
        if suma_filas != numero_magico:
            return False
    for suma_columnas in columnas:
        if suma_columnas != numero_magico:
            return False
    return True

cuadrado = (introduce_filas,introduce_columnas)

filas = []
for i in range(introduce_filas):
    suma = 0
    for j in range(introduce_columnas):
        suma += cuadrado_magico[i][j]
    filas.append(suma)

columnas = []
for i in range(introduce_columnas):
    suma = 0
    for j in range(introduce_filas):
        suma += cuadrado_magico[j][i]
    columnas.append(suma)

diagonal = []
for i in range(introduce_filas):
    for j in range(introduce_columnas):
        if i == j:
            diagonal += introduce_filas

diagonal_inversa = []
for i in range(introduce_columnas):
    for j in range(introduce_filas):
        if diagonal_inversa [i+1][j-1]:
            diagonal_inversa += introduce_columnas

print(filas)
print(columnas)
print(diagonal)
print(diagonal_inversa)


if esMagico(filas,columnas,diagonal,diagonal_inversa):
    print("Es magico")
else:
    print("No es magico")