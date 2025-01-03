import usuarios.usuario as modelo
import notas.acciones as acciones

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
        print("\nVale! Identifícate en el sistema...")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto, intentalo más tarde")

    # Definir el método proximasAcciones
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Qué quieres hacer?: ")
        hazEl = acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            #vuelve a llamar a proximasAcciones
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            print("Vamos a eliminar")
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Hasta luego {usuario[1]}!")
            exit()

        else:
            print("Acción no reconocida")
            self.proximasAcciones(usuario)
