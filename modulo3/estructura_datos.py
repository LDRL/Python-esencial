# Lista

# Las listas son mutables a diferencia de los strings
# las listas se inicia con [] o con la funcion list

import copy

countries = ['Mexico', 'Venezuela', 'Colombia', 'Argentina']
ages = [12, 18, 24, 34, 50]
wiights = [12, 18, 24, 34, 50]
receta = ['Ensalda', 2, 'lechugas', 5, 'jitomates']

countries[0] = 'Ecuador'

global_countries = copy.copy(countries)

countries[0] = 'Guatemala'

print(countries)
print(global_countries)

for country in countries:
    print(country)