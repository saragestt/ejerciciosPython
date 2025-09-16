#Determine el menor valor de 5 números introducidos por teclado. Considere
#que el menor valor puede repetirse. Por ejemplo: Si los números introducidos
#fueran. 14, 19, 14, 16 y 15. El menor valor introducido es 14.

lista = []
for i in range(5):
    introduce = int(input(f"Introduce {i+1}ª numero:\n"))
    lista.append(introduce)

menor = min(lista)

print(f"El numero menor es:{menor}")