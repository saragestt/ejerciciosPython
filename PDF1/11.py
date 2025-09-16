#Capturamos tres números por teclado y debemos ordenarlos de mayor a menor.


Lista = []
for i in range(3):
    numeros = int(input(f"Introduce el numero {i+1}: "))
    Lista.append(numeros)

Lista.sort(reverse=True)

print(f"Ordenados de mayor a menor: {Lista}")

