from tkinter import *

ventana = Tk()

ventana.geometry("700x400")

mi_menu = Menu(ventana, tearoff=0)
ventana.config(menu=mi_menu)

archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Abrir carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit)

editar = Menu(mi_menu, tearoff=0)
editar.add_command(label="Copiar")

seleccion = Menu(mi_menu, tearoff=0)
seleccion.add_command(label="Seleccionar todo")

mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_cascade(label="Editar", menu=editar)
mi_menu.add_cascade(label="Selección", menu=seleccion)

ventana.mainloop()