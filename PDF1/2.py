#Programa que capture un número por teclado e indique si es par o impar.

introduce = int(input("Introduce un numero:\n"))

if introduce %2==0:
    introduce = ("Par")
else:
    introduce = ("Impar")

print(f"Es: {introduce}")