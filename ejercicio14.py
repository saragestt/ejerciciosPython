
dia1 = "Hoy es lunes"
dia2 = "Hoy es martes"
dia3 = "Hoy es miercoles"
dia4 = "Hoy es jueves"
dia5 = "Hoy es viernes"
dia6 = "Hoy es sabado"
dia7 = "Hoy es domigo"
resto = "Ups! Error!"

dia_introducido = int(input("Introduce un dia de la semana(del 1 al 7):\n"))

if dia_introducido == 1:
    resultado = (dia1)
elif dia_introducido == 2:
    resultado = (dia2)
elif dia_introducido == 3:
    resultado = (dia3)
elif dia_introducido == 4:
    resultado = (dia4)
elif dia_introducido == 5:
    resultado = (dia5)
elif dia_introducido == 6:
    resultado = (dia6)
elif dia_introducido == 7:
    resultado = (dia7)
else:
    resultado = (resto)

print(f"{resultado}")


