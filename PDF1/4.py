#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base
#y el exponente. Pueden ocurrir tres cosas:
# El exponente sea positivo, sólo tienes que imprimir la potencia.
# El exponente sea 0, el resultado es 1.
# El exponente sea negativo, el resultado es 1/potencia con el exponente
#positivo.

intro_base = int(input("Introduce la base:\n"))
intro_exponente = int(input("Introduce el exponente:\n"))

if intro_exponente > 0:
    print(f"el resultado es: {intro_base**intro_exponente}")
elif intro_exponente == 0:
    print("El resultado es: 1")
else:
    print(f"El resultado es: {1/(intro_base**intro_exponente)}")
