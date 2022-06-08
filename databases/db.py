import mysql.connector

# Se establecen los datos de conexion a la base de datos
mydb = mysql.connector.connect(
  host='localhost',
  user='user',
  password='password',
  database='my_test'
)

cursor = mydb.cursor()

# -- CONSULTAR DATOS
cursor.execute('SELECT * FROM Usuario')
##cursor.execute('SELECT * FROM Usuario limit 2')
# Fetchall devuelve todas las instancias que encontro en la base de datos
resultado = cursor.fetchall()
# Fetchdone devuelve solo un registro
# resultado = cursor.fetchone()
print(resultado)

# Ver deficiones de las tablas
#cursor.execute('SHOW CREATE TABLE Usuario')

# -- INSERTAR DATOS
# Escribir la consulta a ejecutar y luego escribir los datos a insertar que sustituyen los %s
# sql = 'INSERT INTO Usuario (email, username, edad) values (%s, %s, %s)'
# values = ('correo@test.com','nombreUsuario', 45)

# -- ACTUALIZAR DATOS
# sql = 'UPDATE Usuario SET email = %s WHERE id = %s'
# values = ('pythonSql@mail.com', 12)

# -- ELIMINAR DATOS
# sql = 'DELETE FROM Usuario WHERE id = %s'
# values = (12, )

# Cuando ejecutamos una consulta sql, vamos a tener valores que tienen que ser reemplazados, execute recibe 2 argumentos
# Primero recibe la sentencia y la segunda los valores a reemplazar
##cursor.execute(sql, values)
# Sin embargo los datos no seran guardados hasta que se comprometan los cambios
##mydb.commit()
#print(cursor.rowcount)
