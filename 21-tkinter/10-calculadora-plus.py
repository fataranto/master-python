"""
CALCULADORA:

"""
from tkinter import *
from tkinter import messagebox

class Calculadora:
    def __init__(self, messagebox):
        self.messagebox = messagebox
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()

    def sumar(self):
        try:
            self.resultado.set(float(self.numero1.get()) + float(self.numero2.get()))
            self.mostrarResultado()
        except:
            self.messagebox.showerror("Error", "Introduce valores correctos")

    def restar(self):
        try:
            self.resultado.set(float(self.numero1.get()) - float(self.numero2.get()))
            self.mostrarResultado()
        except:
            self.messagebox.showerror("Error", "Introduce valores correctos")

    def multiplicar(self):
        try:
            self.resultado.set(float(self.numero1.get()) * float(self.numero2.get()))
            self.mostrarResultado()
        except:
            self.messagebox.showerror("Error", "Introduce valores correctos")

    def dividir(self):
        try:
            self.resultado.set(float(self.numero1.get()) / float(self.numero2.get()))
            self.mostrarResultado()
        except:
            self.messagebox.showerror("Error", "Introduce valores correctos")

    def mostrarResultado(self):
        self.messagebox.showinfo("Resultado", f"El resultado de la operación es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")


ventana = Tk()
ventana.title("Calculadora | Master en Python")
ventana.geometry("400x400")
ventana.config(bd=70)

marco = Frame(ventana, width=300, height=250)
marco.config(
    bd=5,
    relief="solid",
    padx=15,
    pady=15
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

calculadora = Calculadora(messagebox)

Label(marco, text="Número 1:").pack()
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

Label(marco, text="Número 2:").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

Label(marco, text="").pack() # Separador

Button(marco, text="sum", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="rest", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="mult", command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="div", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()
