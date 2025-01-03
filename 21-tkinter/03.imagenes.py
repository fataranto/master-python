from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x400")

Label(ventana, text="Imagenes en Tkinter").pack(anchor=W)

imagen = Image.open("./21-tkinter/imagenes/rpm.png")
# definir como integral
W, H = imagen.size
imagen = imagen.resize((W//3, H//3))


render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()
