class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad
    def calc_volumen(self):
        return self.ancho * self.alto * self.profundidad
ancho = int(input(f'Digite el ancho: '))
alto = int(input(f'Digite el alto: '))
profundidad = int(input(f'Digite la profundidad: '))
cubo1 = Cubo(ancho, alto, profundidad)
print(f'El volumen del cubo es: {cubo1.calc_volumen()}')