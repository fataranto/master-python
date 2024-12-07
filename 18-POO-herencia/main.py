import clases

persona = clases.Persona()
persona.setNombre("Fabian")
persona.setApellidos("Taranto")
persona.setAltura(1.70)
persona.setEdad(90)

print(f"Nombre: {persona.getNombre()}, apellido: {persona.getApellidos()}, edad: {persona.getEdad()}, altura: {persona.getAltura()}")