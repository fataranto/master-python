from tkinter import *

ventana = Tk()
ventana.geometry("700x400")

texto = Label(ventana, text="Programa en Python")
texto.config(
    fg="white",
    bg="black",
    padx=50,
    pady=20,
    font=("Arial", 30)
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="Bienvenido")
texto.config(
    height=3,
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="circle"
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="Prueba 1")
texto.config(
    height=3,
    bg="pink",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="circle"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Prueba 2")
texto.config(
    height=3,
    bg="purple",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="circle"
)
texto.pack(side=LEFT, fill=X, expand=YES)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}, veo que eres de {pais}"

texto = Label(ventana, text=pruebas(nombre="Monkey", apellidos="D Luffy", pais="Wano")) # No es obligatorio usar el nombre de los parametros, pero esto me permite cambiar el orden de los parametros
texto.config(
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)




ventana.mainloop()
