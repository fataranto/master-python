from tkinter import *

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formulario con Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)

encabezado.grid(row=0, column=0, columnspan=12, sticky=W)
# Crear campos del formulario

#checkbox
def mostrarProfesion():
    texto = ""
    if web.get():
        texto += "Desarrollador web"
    if design.get():
        if web.get():
            texto += " y "
        texto += "Diseñador web"

    mostrar.config(
        text=texto,
        fg="white",
        bg="darkgray"
    )

web = IntVar()
design = IntVar()

Label(ventana, text="A qué te dedicas?").grid(row=1, column=0)
Checkbutton(
    ventana, 
    text="Web Dev",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)
Checkbutton(
    ventana, 
    text="Web Design",
    variable=design,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=1)

mostrar = Label(ventana)
mostrar.grid(row=3, column=0)


# Radio buttons
def marcar():
    marcado.config(text=opcion.get())

opcion = IntVar()
Label(ventana, text="Género:").grid(row=4, column=0)
Radiobutton(
    ventana, 
    text="Masculino", 
    variable=opcion,
    command=marcar,
    value=1
).grid(row=4, column=0)
Radiobutton(
    ventana, 
    text="Femenino",
    variable=opcion,
    command=marcar,
    value=2
).grid(row=4, column=1)

marcado = Label(ventana)
marcado.grid(row=5, column=0)


# OptionMenu

def seleccionar():
    seleccionado.config(text=opciones.get())

opciones = StringVar()
opciones.set("Opción 1")

Label(ventana, text="Selecciona una opción:").grid(row=6, column=0)

select = OptionMenu(
    ventana,
    opciones,
    "Opción 1",
    "Opción 2",
    "Opción 3"
).grid(row=7, column=0)

Button(ventana, text="Ver", command=seleccionar).grid(row=8, column=0)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)




ventana.mainloop()
