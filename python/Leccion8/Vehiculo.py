class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'color: '+self.color+', Ruedas: '+str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+', velocidad(km/hr): '+ str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__()+', Tipo: '+self.tipo


vehiculo = Vehiculo('rojo', 4)
print(vehiculo)
auto = Auto('azul', 4, 120)
print(auto)
bicicleta = Bicicleta('Azul', 2, 'MTB')
print(bicicleta)