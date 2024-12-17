import mysql.connector


def conectar():
    database = mysql.connector.connect(
        host= "localhost",
        user="root",
        passwd="root",
        port=8889,
        database='master_python'
    )

    cursor = database.cursor(buffered=True) #buffered=true es para cargar la consulta en memoria

    return [database, cursor]

