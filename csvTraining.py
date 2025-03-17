import os

def crearArchivo(nombre):
    if os.path.exists(nombre):
        print("Existe")
    else:
        print("No existe")
        gestorArchivos = open(nombre, "x")


def crearInformacion(info, archivo):
    escritorArchivos = open(archivo, "a")
    escritorArchivos.write(info)


def añadirInformacion(info, archivo):
    escritorArchivos = open(archivo, "a")
    escritorArchivos.write(info + "\n")


def leerFicheros(archivo):
    lectorArchivos = open(archivo, "r")
    info = lectorArchivos.read()
    return info




