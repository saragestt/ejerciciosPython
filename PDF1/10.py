#Introducimos dos números por teclado y queremos guardar el valor mayor en
#la variable MAYOR y el número menor en la variable MENOR.

introduce1 = int(input("Introduce un numero:\n"))
introduce2 = int(input("Introduce un numero:\n"))

Mayor = 0
numero_menor = 0

if introduce1 > introduce2:
    Mayor = introduce1
elif introduce2 > introduce1:
    Mayor = introduce2

if introduce1 < introduce2:
    numero_menor = (introduce1)
elif introduce2 < introduce1:
    numero_menor = (introduce1)

print(f"El numero menor es: {numero_menor} y el numero mayor es: {Mayor}")