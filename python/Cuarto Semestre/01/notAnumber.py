import math

a = float('Nan')
print(f'Es nan?: {math.isnan(a)}')
# Bool

valor = 0.1
resultado = bool(valor)
print(f'valor: {valor}')

# tipo str -> false '', true 'abc'
valor = 'e'
resultado = bool(valor)
print(f'valor: {valor}, resultado: {resultado}')
# colecciones
valor = [1, 2, 3]
resultado = bool(valor)
print(f'valor: {valor}, resultado: {resultado}')
# lo mismo con todas las colecciones yadayadayada

# sentencias de control
if 'f':
    print('regresa verdadero')
else:
    print('regresa falso')

# ciclos
variable = 3
while variable:
    print('regresa verdadero')
    break
else:
    print('regresa falso')