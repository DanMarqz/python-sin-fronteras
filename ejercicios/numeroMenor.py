# function para que encuentre el numero menor de una lista

lista = [1 , 12 , 43 ,-54 , 25 , -12 , 63 , 49 , -5]

menor = 'init'

for x in lista:
  if menor == 'init':
    menor = x
  else:
    menor = x if x < menor else menor
    # Para el caso de mayor cambia el simbolo < por >
    # menor = x if x > menor else menor

print('el numero menor es', menor)