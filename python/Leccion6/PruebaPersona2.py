from Persona2 import Persona2
print('creacion de objetos'.center(50, '-'))
if __name__ == '__main__':
    persona5 = Persona2('Alberto', 'Einstein', 167, 'aleman','ulm',2300)
    persona5.mostrar_detalles()
    persona5.nombre = 'Beto'
    print(persona5.mostrar_detalles())

    print(__name__)

print('eliminacion de objetos'.center(50, '-'))
del persona5