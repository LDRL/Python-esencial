# Evaluaciones Booleanas

# Operadores de comparación
# ==
# <
# >
# <=
# >=

# Tabla de valores
# ---| ---| AND|
#   T   T   T
#   T   F   F
#   F   T   F
#   F   F   F


# ---| ---| OR|
#   T   T   T
#   T   F   T
#   F   T   T
#   F   F   F

x = 2
y = 3
a = 5
b = 7

print((x < y) and (a < b))

print((x < y) and (a > b))

print((x < y) or (a > b))

if x < y:
    print(' x es menor que y')
else:
    print(' x es mayor que y')

