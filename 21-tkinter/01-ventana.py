# Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path

# Crear la ventana raiz
ventana = Tk()

# Configurar la ventana
ventana.geometry("800x600") # Tamaño de la ventana

# bloquear el tamaño de la ventana
ventana.resizable(0,0)

# Titulo de la ventana
ventana.title("Hola Mundo")

# Comprobar si un archivo existe
ruta_icono = os.path.abspath('./imagenes/favicon.ico')

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./21-tkinter/imagenes/favicon.ico')

# Cambiar el icono de la ventana
ventana.iconbitmap(ruta_icono)

# Mostar texto en la ventana
texto = Label(ventana, text=ruta_icono)
texto.pack()



# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()

