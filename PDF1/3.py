#Crea un programa que pida al usuario dos números y muestre su división si el
#segundo no es cero, o un mensaje de aviso en caso contrario.

introduce1 = int(input("Introduce el primer numero:\n"))
introduce2 = int(input("Introduce el segundo numero:\n"))

if introduce2 == 0:
    print("Error!")
else:
    print(introduce1/introduce2)

