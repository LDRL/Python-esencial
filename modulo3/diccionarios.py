##
# Es similar a una lista en el sentido que se puede acceder a traves de indices
# en el diccionario se llaman llaves
# los indices deben de ser enteros

products = {}
products['leche'] = 23.50

print(products)

rae = {}
rae['pizza'] = 'La comida mas deliciosa del mundo'
rae['pasta'] = 'La comida mas sabroas de italia'

a = rae.get('helado', None)


#ciclar

for key in rae.keys():
    print(key)

for value in rae.values():
    print(value)

for key, value in rae.items():
    print(key, value)
