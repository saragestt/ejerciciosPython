#Programa una calculadora que me pida dos valores numéricos por teclado y la
#operación que se quiere realizar de entre las siguientes, suma, resta,
#multiplicación y división.


valor1 = float(input("Introduce el primer numero:"))
valor2 = float(input("Introduce el segundo numero:"))
operador = input("Introduce el operador(+,-,*,/):")

if operador == "+":
    print(valor1 + valor2)
elif operador == "-":
    print(valor1 - valor2)
elif operador == "*":
    print(valor1 * valor2)
else:
    print(valor1 / valor2)