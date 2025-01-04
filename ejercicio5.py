#Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘género’ y muestre
#el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor
#o igual a dieciocho y el género es ‘F’. En caso de que se cumpla lo mismo,
#pero el sexo sea ‘M’,debe imprimir ‘ACEPTADO’. Si no se cumplen dichas
#condiciones se debe mostrar ‘NO ACEPTADO/A’.

introduce_nota = int(input("Introduce la nota:\n"))
introduce_edad = int(input("Introduce la edad:\n"))
introduce_genero = input("Introduce el genero(M o F):\n")

if introduce_nota >= 5 and introduce_edad >=18 and introduce_genero == "F":
    print("ACEPTADA")
elif introduce_nota >= 5 and introduce_edad >= 18 and introduce_genero == "M":
    print("ACEPTADA")
else:
    print("NO ACEPTADO/A")
