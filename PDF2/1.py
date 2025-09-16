#Muestra en pantalla 15 números obtenidos de forma aleatoria. Entre un número y otro
#haz que el ordenador espere dos segundos como si estuviera pensando en obtener el
#nuevo número


import random
import time

for _ in range(15):
    print(random.randint(1, 100))
    time.sleep(2)