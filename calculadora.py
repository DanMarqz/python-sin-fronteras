firstInput = input('::  Introduzca el primer numero a operar  ')
try:
  firstInput = int(firstInput)
except:
  firstInput = 'err'

if firstInput == 'err': 
  print('!::  Error, el valor indicado no es un numero.')
  exit()

secondInput = input('::  Introduzca el segundo numero a operar  ')
try:
  secondInput = int(secondInput)
except:
  secondInput = 'err'

if secondInput == 'err': 
  print('!::  Error, el valor indicado no es un numero.')
  exit()

simbolo = input('::  Ingrese la el simbolo de la operacion que se va a realizar [ + | - | * | / ]  ')

if simbolo == '+':
  print('::  Suma:  ', firstInput + secondInput)
elif simbolo == '-':
  print('::  Resta:  ', firstInput - secondInput)
elif simbolo == '*':
  print('::  Multiplicacion: ', firstInput * secondInput)
elif simbolo == '/':
  print('::  Division:  ', firstInput / secondInput)
else:
  print('!::  Error, el simbolo indicado no es valido.  ')