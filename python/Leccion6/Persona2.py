class Persona2:
    def __init__(self, nombre, apellido, edad, nacionalidad, provincia, codigopostal):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.provincia = provincia
        self.codigopostal = codigopostal

    def  mostrar_detalles(self):
        print(f'Los datos a mostrar son lso sgtes: {self._nombre}, {self._apellido}, {self._edad}, {self._nacionalidad}, {self._provincia}, {self._codigopostal}')

    @property  #decorador
    def nombre(self): #metodo getter
       # print('utilizamos el metodo get')
        return self._nombre

    @property  # decorador
    def apellido(self):  # metodo getter
      #  print('utilizamos el metodo get')
        return self._apellido

    @property  # decorador
    def edad(self):  # metodo getter
        #print('utilizamos el metodo get')
        return self._edad

    @property  # decorador
    def nacionalidad(self):  # metodo getter
       # print('utilizamos el metodo get')
        return self._nacionalidad

    @property  # decorador
    def provincia(self):  # metodo getter
       # print('utilizamos el metodo get')
        return self._provincia

    @property  # decorador
    def codigopostal(self):  # metodo getter
       # print('utilizamos el metodo get')
        return self._codigopostal

    @nombre.setter
    def nombre(self,nombre):
       # print('utilizamos el metodoset')
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
       # print('utilizamos el metodoset')
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):
       # print('utilizamos el metodoset')
        self._edad = edad

    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
       # print('utilizamos el metodoset')
        self._nacionalidad = nacionalidad

    @provincia.setter
    def provincia(self, provincia):
        #print('utilizamos el metodoset')
        self._provincia = provincia

    @codigopostal.setter
    def codigopostal(self, codigopostal):
        #print('utilizamos el metodoset')
        self._codigopostal = codigopostal

    def __del__(self):
        print(f'Persona2: {self.nacionalidad} {self.provincia} {self.codigopostal}')
if __name__ == '__main__':
    persona1 = Persona2('Silvina', 'Prado', 25, 'argentina', 'mendoza', 5600)

    persona1.nombre = 'Pepe' #llamamos al setter
    print(persona1.nombre) #otra vez al getter
    print(persona1.mostrar_detalles())

    print(persona1.edad) #atributo read only no se pyede modificar porque no tiene el metodo set?
    #TAREAAA crear tres objetos mas con getter y setter, mostrar los cambios
    persona1.nacionalidad = 'canadiense'
    persona1.provincia = 'ontario'
    persona1.codigopostal = 3456
    print(persona1.mostrar_detalles())

    persona3 = Persona2('Felipe', 'Prado', 9, 'argentino', 'mendoza', 5600)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalles())

    print(__name__)
