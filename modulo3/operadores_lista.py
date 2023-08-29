import random
# suma
# a = [1, 2]
# b = [2,3]
# a +b #[1,2,2,3]

# multiplicacion

# agregar un elemento a la final de la lista utilizar append

a = [1]
a.append(2)  # [1,2]

# para eliminar el ultimo elemento de la lista utilizar pop
a = [1, 2]
b = a.pop()
print(a)  # [1]
print(b)  # 2

# para ordenar una lista, podemos utilizar el metodo sort
a = [3, 8, 1]
a.sort()  # [1,3,8]

# eliminacion
# del
# funciona con slices

a = [1, 2, 3]
del a[-1]

# si se sabe que elemento eliminar pero no el indice
# remove


a = list(range(0, 100, 2))
b = list(range(0, 10))

c = a + b
b = b * 2

fruits = list()
fruits.append('apple')

fruits.append('banana')
len(fruits)

fruits.append('Kiwi')

some_fruit = fruits.pop()



random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(0,15))

print(random_numbers)

ordered_numbers = sorted(random_numbers)
print(ordered_numbers)