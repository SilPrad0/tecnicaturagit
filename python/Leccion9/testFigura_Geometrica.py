from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, 'azul')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Calculo del area: {cuadrado1.calcular_area()}')
#MRO = method resolution order
print(Cuadrado.mro())

print(cuadrado1)

rectangulo1 = Rectangulo(3,6,'rojo')
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')
print(rectangulo1)