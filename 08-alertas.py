from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(
    bd=70
)

def sacarAlerta(mensaje="Hola, soy una alerta"):
    MessageBox.showinfo("Alerta", mensaje)

Button(ventana, text="Mostrar alerta", command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Quieres continuar?")

    if resultado != "yes":
        MessageBox.showinfo("Chao!!!", f"Adios, hasta luego {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("Lucas")).pack()

ventana.mainloop()