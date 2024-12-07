# Programación orientada a objetos

#  Definir una clase


class Coche:
    color = "Rojo"
    marca = "Peugeot"
    modelo = "Partner"
    velocidad = 110
    caballaje = 500
    plazas = 4

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def getVelocidad(self):
        return self.velocidad
    
    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo
    
    def setCaballaje(self, caballaje):
        self.caballaje = caballaje

    def getCaballaje(self):
        return self.caballaje

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1


    

# Crear objetos
coche = Coche()

def acelerarCoche():
    for i in range(10):
        coche.acelerar()
        print("Velocidad actual: ", coche.velocidad)

# acelerarCoche()

