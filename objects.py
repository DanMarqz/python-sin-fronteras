# # Definiendo una clase
# class Usuario:
#   def __init__(self, nombre, apellido):
#     self.nombre = nombre
#     self.apellido = apellido

#   # Metodo
#   def saludo(self):
#     print('Hola, mi nombre es', self.nombre)

# # Herencia de una clase
# class Admin(Usuario):
#   def superSaludo(self):
#     print('Hola, me llamo', self.nombre, 'y soy el administrador')

# usuario = Usuario('Daniel', 'Feliz')
# usuario.saludo()

# Cambiar el valor de una propiedad de la clase
# usuario.nombre = 'Danito'

# Eliminar una propiedad de la clase
# del usuario.nombre

# Eliminar un metodo de la clase
# del usuario.saludo()

# Eliminar una clase
# del usuario

# El hijo puede utilizar los metodos del padre, pero no al reves
# admin = Admin('Dani', 'Sudo')
# admin.saludo()
# admin.superSaludo()

class Animal:
  def __init__(self, nombre, onomatopeya):
    self.nombre = nombre
    self.onomatopeya = onomatopeya
  def saludo(self):
    print('Hola, soy un', self.tipo, 'y hago', self.onomatopeya)

class Gato(Animal):
  tipo = 'gato'
  def __init__(self, nombre, onomatopeya):
    Animal.__init__(self, nombre, onomatopeya)
    print('Hola, soy',self.nombre,'extendido')

class Perro(Animal):
  tipo = 'perro'
  def __init__(self, nombre, onomatopeya):
    super().__init__(nombre, onomatopeya)
    print('Hola, soy',self.nombre,'instanciado')

class Canario(Animal):
  tipo = 'canario'
  def __init__(self, nombre, onomatopeya):
    Animal.__init__(self, nombre, onomatopeya)
    print('Hola, soy',self.nombre,'extendido')

gato = Gato('Gato', 'Meow')
gato.saludo()

perro = Perro('Perro', 'Woau')
perro.saludo()

canario = Canario('Canario', 'Pio')
canario.saludo()