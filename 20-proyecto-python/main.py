from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")

hazEl = acciones.Acciones()
accion = input("¿Qué deseas hacer?: ")

if accion == "registro":
    hazEl.registro()
    

elif accion == "login":
    hazEl.login()