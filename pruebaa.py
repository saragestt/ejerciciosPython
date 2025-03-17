from csvTraining import añadirInformacion, crearArchivo, leerFicheros

def crearUsuario():
    nombre = input("Introduce tu nombre: ")
    numero = int(input("Introduce tu numero: "))
    email = input("Introduce tu email: ")
    return f"{nombre};{numero};{email}"



while input("¿Desea continuar(s/n)?").lower() == "s":
    añadirInformacion(crearUsuario(),"Agenda")


print(leerFicheros("Agenda"))








