# Herencia: Es la posibilidad de compartir atributos y métodos
# entre clases y que diferentes clases hereden de otras

class Persona:
    """
    Clase que representa a una persona.
    Atributos:
        - nombre: Nombre de la persona.
        - apellidos: Apellidos de la persona.
        - altura: Altura de la persona.
        - edad: Edad de la persona.
    """
    def __init__(self, nombre="", apellidos="", altura=0.0, edad=0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.altura = altura
        self.edad = edad

    # Setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    # Getters
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad
    
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    

class Informatico(Persona):
    """
    lenguajes
    experiencia
    """
    
    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "He reparado tu ordenador"



    