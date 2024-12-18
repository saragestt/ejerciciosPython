#Programa que capture un número por teclado e indique si es par o impar

numero = int(input("Introduce un numero:\n"))

if numero % 2 == 0:
    print(f"{numero} es Par")
else:
    print(f"{numero} es Impar")