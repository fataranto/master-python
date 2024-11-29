# Modulos por defectos de python

# modulo de fechas
import datetime

print(datetime.date.today())


fecha_completa = datetime.datetime.now()

print(fecha_completa)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("fecha personalizada: ", fecha_personalizada)

# Modulo matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))

print("Número pi: ", math.pi)

print("Redondear: ", math.ceil(6.83478))

# Modulo random

import random

print("Número aleatorio entre 15 y 67: ", random.randint(15, 67))