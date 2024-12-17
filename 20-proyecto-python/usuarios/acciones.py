import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nOK! Vamos a registrarte en el sistema...")

        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado correctamente")
        else:
            print(f"\nNo te has registrado correctamente, el email {usuario.email} ya existe")

    def login(self):
        print("Vale! Identifícate en el sistema...")

        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")