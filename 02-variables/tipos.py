nada = None #con mayúsculas
cadena = "soy una cadena de texto"
entero = 100
flotante = 10.2
booleano = True #con mayúsculas
array = [1,2,3,4,5]
arrayMixto = [1,"dos",3,"cuatro",5]
tuplaNoCambia = ("tupla", "no", "cambia")
diccionario = {
    "nombre": "Fabian",
    "apellido": "Taranto",
    "Tel": "635-348-873"
}
rango = range(5)

dsatoByte = b"pepe"

print(diccionario)
print(type(diccionario))

#solo es posible concatenar cadenas de texto
texto = "hola texto"
numero = 34

#print(texto + numero) -> genera error

print(texto + " " + str(numero))