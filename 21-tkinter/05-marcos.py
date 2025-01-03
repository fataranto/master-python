from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Marcos | Master en Python")

marco = Frame(ventana, width=250, height=250)

marco.config(
    bg="lightblue",
    bd=5,
    relief="solid",
    padx=15,
    pady=15
)

marco.pack(side=RIGHT, anchor=SE)
marco.pack_propagate(False) # No ajustar el tamaño del marco al contenido

Label(marco, text="Prueba de marcos").pack(anchor=CENTER)



marco = Frame(ventana, width=250, height=250)

marco.config(
    bg="pink",
    bd=5,
    relief="solid",
    padx=15,
    pady=15
)

marco.pack(side=LEFT, anchor=SW, fill=Y, expand=YES) # colocar texto en el marco

texto = Label(marco, text="Programa en Python")
texto.config(
    fg="white",
    bg="black",
    padx=50,
    pady=20,
    font=("Arial", 30)
)
texto.pack()

ventana.mainloop()