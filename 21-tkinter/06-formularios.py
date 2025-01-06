from tkinter import *
# from tkinter import ttk (para usar estilos, en Mac)

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
encabezado.grid(row=0, column=0, columnspan=6, sticky=W)  # Si uso grid no puedo usar pack


# Label para el campo (nombre)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5, sticky=NE)

# Campo de texto (nombre)
campo_texto = Entry(ventana) # Entry es un campo de texto (input)
campo_texto.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# Label para el campo (apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5, sticky=NE)

# Campo de texto (apellidos)
campo_texto = Entry(ventana) # Entry es un campo de texto (input)
campo_texto.grid(row=2, column=1, padx=5, pady=5, sticky=W)

# Label para el campo (descripcion)
label = Label(ventana, text="Descripción")
label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)

# Campo de texto (descripcion)
campo_grande = Text(ventana) # Entry es un campo de texto (textaera)
campo_grande.grid(row=3, column=1, padx=5, pady=5, sticky=W)
campo_grande.config(
    width=30,
    height=5,
    font=("Arial", 12),
    padx=15,
    pady=15
)

# Botón de enviar
Label(ventana).grid(row=4, column=1)  # Separador

boton = Button(ventana, text="Enviar", highlightbackground="green", fg="green", bd=1)
boton.grid(row=5, column=1, sticky=W)

boton.config(
    padx=15,
    pady=5
)


ventana.mainloop()