

def generarMatriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            numero = int(input(f"Introduce el numero para {i} {j} "))
            fila.append(numero)
        matriz.append(fila)
    return matriz

def es_magico(filas, columnas, diagonal, diagonal_inversa):
    numero_magico = diagonal
    for suma in filas:
        if suma != numero_magico:
            return False
    for suma in columnas:
        if suma != numero_magico:
            return False
    if diagonal != diagonal_inversa:
        return False
    return True

numero = int(input("Introduce el tamaño de la matriz cuadrada: "))
matriz = generarMatriz(numero)

filas = []
for i in range(numero):
    suma_fila = 0
    for j in range(numero):
        suma_fila += matriz[i][j]
    filas.append(suma_fila)

columnas = []
for j in range(numero):
    suma_columna = 0
    for i in range(numero):
        suma_columna += matriz[i][j]
    columnas.append(suma_columna)

diagonal = 0
for i in range(numero):
    diagonal += matriz[i][i]

diagonal_inversa = 0
for i in range(numero):
    diagonal_inversa += matriz[i][numero - i - 1]

print("Matriz:")
for fila in matriz:
    print(fila)

if es_magico(filas, columnas, diagonal, diagonal_inversa):
    print("La matriz es un cuadrado mágico.")
else:
    print("La matriz NO es un cuadrado mágico.")
    print(f"Suma de filas: {filas}")
    print(f"Suma de columnas: {columnas}")
    print(f"Suma de la diagonal principal: {diagonal}")
    print(f"Suma de la diagonal inversa: {diagonal_inversa}")