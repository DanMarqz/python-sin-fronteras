def miFuncion():
  print('Mi primera funcion')

def imprimeNombre(nombre, apellido):
  print(':: El nombre completo es', nombre, apellido)
imprimeNombre('Daniel','Marquez')

# Un argumento puede recibir varios valores con el simbolo reservado *
def imprimeTupla(*tupla):
  print(':: Tupla', tupla)
  print(':: Tupla', tupla[0])
imprimeTupla('Dani','Yan','Xeryll','Xiky','Ramona')

# Si no recuerdas el orden de los argumentos, puedes definirlo con la llave de los argumentos/parametros
def nombreCompleto(apellido, nombre):
  print('::', nombre, apellido)
nombreCompleto(nombre='Yan',apellido='Flowerz')

# Puedes definir varios argumentos con ** el cual agrupa los parametros recibidos en un diccionario:
# Ejemplo, si los parametros son: (temperatura=frio, humedad=baja) y el argumento es **clima
# Puedes acceder a ellos dentro de la funcion con: clima['temperatura'], clima['humedad']
def argumentosDiccionario(**kwargs):
  print('::', kwargs['nombre'], kwargs['apellido'])
argumentosDiccionario(nombre='Yan',apellido='Flowerz')

def parametroDefinido(argumento = 'Valor por defecto'):
  print('::', argumento)
parametroDefinido('Dani')
parametroDefinido()

def funcionConLista(lista):
  for el in lista:
    print(el)
funcionConLista([1,2,3,4,5])

def concatenaNombres(lista):
  i = ''
  for el in lista:
    i = i + el + ' '
  return i

nombres = concatenaNombres(['Dani','Yan','Xeryll','Xiky','Ramona'])
print(nombres)