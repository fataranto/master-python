# Programación orientada a objetos

#  Definir una clase

class Coche:
    color = "Rojo"
    marca = "Peugeot"
    modelo = "Partner"
    velocidad = 110
    caballaje = 500
    plazas = 4

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    

# Crear objetos
coche = Coche()

def acelerarCoche():
    for i in range(10):
        coche.acelerar()
        print("Velocidad actual: ", coche.velocidad)

acelerarCoche()