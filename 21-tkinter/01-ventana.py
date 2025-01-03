# Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title = "Master en Python"
        self.icon = "./imagenes/favicon.ico"
        self.icon_alt = "./21-tkinter/imagenes/favicon.ico"
        self.size = "750x450"
        self.resizable = False

    def cargar(self):
        # Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Configurar la ventana
        ventana.geometry(self.size) # Tamaño de la ventana

        # bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)

        # Titulo de la ventana
        ventana.title(self.title)

        # Comprobar si un archivo existe
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Cambiar el icono de la ventana
        ventana.iconbitmap(ruta_icono)

        # Mostar texto en la ventana
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()

# Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola soy un texto")
programa.addTexto("Soy otro texto")
programa.mostrar()

