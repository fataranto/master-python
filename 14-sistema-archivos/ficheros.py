from io import open
import pathlib
import shutil
import os
import os.path

# abrir

#archivo = open(pathlib.Path().absolute() + "fichero_texto.txt", "a+")


ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
#archivo = open(ruta, "a+")
#archivo = open(ruta, "r")

# Escribir
#archivo.write("******soy un texto metido desde pyhton*******\n")

# Leer contenido
# contenido = archivo.read()
# print(contenido)

# Leer contenido y guardarlo en una lista
#lista = archivo.readlines()


#Cerrar archivo
#archivo.close()

#print(lista)

# copiar
#ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
#ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_copia.txt"

#shutil.copyfile(ruta_original, ruta_nueva)

# mover o renombrar
#ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto_copia.txt"
#ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_copia_NUEVO.txt"

#shutil.move(ruta_original, ruta_nueva)

# Eliminar
#ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_copia_NUEVO.txt"
#os.remove(ruta_nueva)

# Comprobar si existe un archivo
#print(os.path.abspath("./"))

if os.path.isfile(os.path.abspath("./") + "/fichero_texto.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")

