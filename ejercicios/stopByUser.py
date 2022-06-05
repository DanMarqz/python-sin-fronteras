# Escribir una aplicacion que reciba una cantidad infinita de numeros hasta decir basta
# luego que retorne la suma de los numeros ingresados

lista = []
def stopByUser():
  inputUsuario = input(':: [ Introduzca un numero para sumar, la aplicacion acaba cuando diga "stop" ] ::\n')

  if inputUsuario == 'stop':
    print(':: La suma de los numeros ingresados es de [', sum(lista) ,'] ::')
  elif inputUsuario.isdigit():
    lista.append(int(inputUsuario))
    stopByUser()
  else: 
    print(':: [ El valor ingresado no es un numero ] ::')
    stopByUser()

stopByUser()