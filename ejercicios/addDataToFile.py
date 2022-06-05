# Funcion que recibe nombre y apellido para agregar a un archivo

def agregarNombreAArchivo(nombre, apellido):
  c = open('archivoDeNombres.txt', 'a')
  c.write(nombre + ' ' + apellido + '\n')
  c.close()

agregarNombreAArchivo('Chanchito', 'Feliz')