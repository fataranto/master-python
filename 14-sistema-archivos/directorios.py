import os, shutil

# Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("El directorio ya existe")

# Eliminar carpeta
#os.rmdir("./mi_carpeta")    

# Copiar carpetas
#ruta_original = "./mi_carpeta"
#ruta_nueva = "./mi_carpeta_COPIA"

#shutil.copytree(ruta_original, ruta_nueva)

# Listar archivos 
print("Contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")

for fichero in contenido:
    print("Fichero: " + fichero)

os.rmdir("./.git") 