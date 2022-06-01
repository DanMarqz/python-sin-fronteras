from modulos import saludo, mascotas
from camelcase import CamelCase

saludo('Dani')
print(mascotas)

c = CamelCase()
s = 'this sentence need CamelCase'

camelcased = c.hump(s)

print(camelcased)

