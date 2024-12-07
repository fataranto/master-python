class Coche:
    color = "Rojo"
    marca = "Peugeot"
    modelo = "Partner"
    velocidad = 110
    caballaje = 500
    plazas = 4
    __infoPrivada = "Información privada"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

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
    
    def setPlazas(self, plazas):
        self.plazas = plazas

    def getPlazas(self):
        return self.plazas

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getInfo(self):
        info = "---- Información del coche ----"
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Color: " + self.getColor()
        info += "\n Velocidad: " + str(self.getVelocidad())
        info += "\n Caballaje: " + str(self.getCaballaje())
        info += "\n Plazas: " + str(self.getPlazas())
        return info
    
    def getInfoPrivada(self):
        return self.__infoPrivada

    
