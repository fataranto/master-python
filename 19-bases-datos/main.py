import mysql.connector

database = mysql.connector.connect(
    host= "localhost",
    user="root",
    passwd="root",
    port=8889,
    database='master_python'
)

#print(database)

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

"""
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""



# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int (10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print (table)


#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")

coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Mercedes', 'Clase C', 35000)
]

# cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)


database.commit()

cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall()


print("------todos los coches--------")
for coche in result:
    print(coche)