class Rectangulo:
    """
    crear rectangulo, 2 atributos, altura y base
    calcular area = base * altura -> ingresadas por el usuario, objetos: 3
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def area(self):
        return self.base * self.altura
base = int(input("digite la base: "))
altura = int(input("digite la altura: "))
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.area()}')


