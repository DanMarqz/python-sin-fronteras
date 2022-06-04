import os

# Eliminar archivos 
if os.path.exists('chanchito.txt'):
  os.remove('chanchito.txt')
else:
  print('El archivo no existe')

# Eliminar directorios
if os.path.exists('miCarpeta'):
  os.rmdir('miCarpeta')
  print('Directorio eliminado')
else:
  print('El directorio no existe')
