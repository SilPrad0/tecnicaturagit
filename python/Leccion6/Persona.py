class Persona: #creamos una clase
    def __init__(self, nombre, apellido, edad, *args, **kwargs):  #se lo llama init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre}, {self.apellido}, {self.edad}, la direcion es: {self.args}, Los datos importantes son: {self.kwargs}')


persona1 = Persona('silvina', 'prado', 25)

print(f'Objeto1: {persona1.nombre}, {persona1.apellido}, Edad: {persona1.edad}')

persona2 = Persona('Felipe', 'Prado', 9)
print(f'El objeto2 de la clase persona: {persona2.nombre}, {persona2.apellido}, Edad: {persona2.edad}')

persona1.nombre = 'eeee'
persona1.apellido = 'aaaa'
persona1.edad = 22
print(f'Objeto1 modificado: {persona1.nombre}, {persona1.apellido}, Edad: {persona1.edad}')

persona1.mostrar_detalle() # la referencia se pasa de manera automatica
persona2.mostrar_detalle()
persona3 = Persona('Lula', 'da silva', 20, 'brasil', 34, 'aaa',234, Altura=1.32, Peso=46, CFavorito='Azul')
print(persona3.mostrar_detalle())