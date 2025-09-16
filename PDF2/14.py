#Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que
#seleccionamos la opción de “Salir


op1 = 1
op2 = 2
op3 = 3
op4 = 4
op5 = 5

print("--------------Menú--------------")
print("            1.Llamar")
print("        2.Enviar mensaje")
print("            3.Camara")
print("            4.Radio")
print("            5.Salir")
print("--------------------------------")


escoger_opcion = int(input("Selecciona una opción (del 1 al 5):\n"))

while escoger_opcion == 1 or escoger_opcion == 2 or escoger_opcion == 3 or escoger_opcion == 4:
    print("Cargando...")
    escoger_opcion = int(input("Selecciona una opción (del 1 al 5):\n"))

if escoger_opcion == 5:
    print("!Hasta pronto!")

while escoger_opcion >5 or escoger_opcion == 0:
    print("¡ERROR!")
    escoger_opcion = int(input("Selecciona un opción (del 1 al 5):\n"))