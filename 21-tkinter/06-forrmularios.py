from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios | Master en Python")


# Texto encabezado
encabezado = Label(ventana, text="Formularios en Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Arial", 20),
    padx=10,
    pady=10
)
encabezado.pack(side=TOP, fill=X)

ventana.mainloop()