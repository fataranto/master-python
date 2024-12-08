# importar modulo sqlite
import sqlite3

# abrir conexión
conexion = sqlite3.connect('pruebas.db')

# crear cursor
cursor = conexion.cursor()

# crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"titulo varchar(255), "+
"descripcion text, "+
"precio int(255)"+
")")

# guardarr cambios
conexion.commit()

# insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'producto uno', 'descripción de mi producto', 250)")
conexion.commit()
"""

# borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "bueno y bonito", 700),
    ("Tablet", "plana", 400),
    ("telefono movil", "sin cables", 1700),
    ("wifi", "cableado", 100)
]

cursor.executemany("INSERT INTO productos VALUES (NULL, ?, ?, ?)", productos)
conexion.commit()

# listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
    print(producto)
    print("---------------------------")

print(cursor)

# cerrar conexión
conexion.close()