# Las tuplas (tuples) son similares a las lista
# la mayor diferencia es que son inmutables

# Es buena practica utilizar un parentesis tambien para ayudar a la legibilidad
# Regresar más de un valor en una función

# los sets se inicializan con la funcion set
# add agregar y remove para eliminarlos

a = 1, 2, 3
print(type(a))

a = (1, 1, 1, 2, 3)
print(type(a))

print(a[0])

print(a.count(1))
print(a.count(2))
print(a.index(1))


a = set([1, 2, 3])
b = {3, 4, 5}

print(a)
print(b)

#Los sets no pueden tener duplicados

a.add(20)
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(b.difference(a))

a.remove(20)
print(a)
