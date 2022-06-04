# 1----------------->
# El segundo parametro 'a' es append que agrega al final del archivo
# c = open('chanchito.txt', 'a')

# Agrega texto al ultimo caracter el archivo
# c.write('\nAgregamos una nueva linea al archivo')
# 1----------------->

# 2----------------->
# El segundo parametro 'w' es write que sobreescribe todo el archivo
# c = open('chanchito.txt', 'w')
# c.write('\nAgregamos una nueva linea al archivo')
# 2----------------->

# Lee cada linea del archivo
# for x in c:
#   print(x)

c.close()

x = open('chanchito.txt')
print(x.read())