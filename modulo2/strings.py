# Las cadenas son secuencias
# Las secuencias se pueden acceder a través de un indice
# Tienen una longitud
# Los caracteres que componen un string se reutilizan a lo largo del programa

country = 'colombia'
print(len(country))

## direccion de memoria con id
second_letter = country[1]
print(second_letter)
print(id(second_letter))