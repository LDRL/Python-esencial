# Comprehensions

# comprehensions son constructos que nos permiten generar secuencias a partir de otras secuencias

# List comprehension
# element for element in element_list if element_meets_condition

# Dictonary comprehension
# key for element in element_list if element_meets_condition

# Set comprehension
# element for element in element_list if element_meets_condition
import random
lista_de_numeros = list(range(100))
print(lista_de_numeros)

pares = [numero for numero in lista_de_numeros if numero % 2 == 0]
print(pares)

student_uid = [1, 2, 3]
students = ['Juan', 'Jose', 'Larsen']
students_with_uid = {uid: student for uid,
                     student in zip(student_uid, students)}

print(students_with_uid)

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1,3))

non_repeated = {number for number in random_numbers}
print(non_repeated)