# Multiplicar dos numeros sin utilizar el simbolo de multiplicacion:
# Se definen 2 numeros (a, b), se declara un nuevo numero (c) que empieza en 0
# Iterar una cantidad de veces determinada por el primer o segundo numero y sumar el numero opuesto
# Ejemplo: si b=4, se sumaria la cantidad de veces que indique a (a=8)

def Multiply(a,b):
  c = 0

  for i in range(a):
    c += b

  print(":: Resultado ~> [" , c , "]")

a = int(input(':: [  Primer numero a multiplicar ]  '))
b = int(input(':: [ Segundo numero a multiplicar ]  '))

Multiply(a,b)