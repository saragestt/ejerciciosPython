#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
#correspondiente. Si introducimos otro número nos da un error.

dia = int(input("Introduce que día es hoy (del 1 al 7): "))

if dia == 1:
    resultado = "Lunes"
elif dia == 2:
    resultado = "Martes"
elif dia == 3:
    resultado = "Miercoles"
elif dia == 4:
    resultado = "Jueves"
elif dia == 5:
    resultado = "Viernes"
elif dia == 6:
    resultado = "Sabado"
elif dia == 7:
    resultado = "Domingo"
else:
    print("Error!")

print(f"Hoy es: {resultado}")

