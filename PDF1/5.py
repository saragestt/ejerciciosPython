#Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘género’ y muestre
#el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor
#o igual a dieciocho y el género es ‘F’. En caso de que se cumpla lo mismo,
#pero el sexo sea ‘M’,debe imprimir ‘ACEPTADO’. Si no se cumplen dichas
#condiciones se debe mostrar ‘NO ACEPTADO/A’.

nota = int(input("Introduce tu nota:\n"))
edad = int(input("Introduce tu edad:\n"))
genero = input("Introduce tu genero (M/F):\n")

if nota >= 5 and edad >=18 and genero == "F":
    print("ACEPTADA")
elif nota >= 5 and edad >=18 and genero == "M":
    print("ACEPTADO")
else:
    print("NO ACEPTADO/A")


