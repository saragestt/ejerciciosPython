#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las
#dimensiones de los lados de un triángulo. El programa debe determinar que
#tipo de triangulo es, teniendo en cuenta los siguiente:
#• Si se cumple Pitágoras entonces es triángulo rectángulo
#• Si sólo dos lados del triángulo son iguales entonces es isósceles.
#• Si los 3 lados son iguales entonces es equilátero.
#• Si no se cumple ninguna de las condiciones anteriores, es escaleno

ladoA = int(input("Introduce el lado A:\n"))
ladoB = int(input("Introduce el lado B:\n"))
ladoC = int(input("Introduce el lado C:\n"))

if ladoA == ladoB  == ladoC:
    print("Es equilatero")
elif ladoA == ladoB != ladoC or ladoB ==ladoC != ladoA or ladoC == ladoA != ladoB:
    print("Es isosceles")
elif ladoA**2 + ladoB**2 == ladoC**2 or ladoB**2 + ladoC**2 == ladoA**2 or ladoC**2 + ladoA**2 == ladoB**2:
    print("Es triangulo rectangulo")
else:
    print("Es escaleno")