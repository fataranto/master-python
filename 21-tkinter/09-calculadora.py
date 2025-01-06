"""
CALCULADORA:

"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Calculadora | Master en Python")
ventana.geometry("400x400")
ventana.config(bd=70)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=250, height=250)
marco.config(
    bd=5,
    relief="solid",
    padx=15,
    pady=15
)

def sumar():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce valores correctos")

def restar():
    try:
        resultado.set(float(numero1.get()) - float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce valores correctos")

def multiplicar():
    try:
        resultado.set(float(numero1.get()) * float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce valores correctos")

def dividir():
    try:
        resultado.set(float(numero1.get()) / float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce valores correctos")

def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operación es: {resultado.get()}")
    numero1.set("")
    numero2.set("")

marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Número 1:").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Número 2:").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="+", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="-", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="*", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="/", command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()
