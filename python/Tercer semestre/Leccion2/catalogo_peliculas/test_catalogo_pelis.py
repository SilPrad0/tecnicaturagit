from dominio.peliculas import Pelicula
from servicio.catalogos_peliculas import CatalogoPeliculas as cp
opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar pelicula')
        print('2. Listar las peliculas')
        print('3. Eliminar catalogo de peliculas')
        print('4. Salir')
        opcion = int(input('Digite una opcion de menú: '))
    except Exception as e:
        print(f'Error: {e}')
        opcion = None
    if opcion == 1:
        nombre_peli = input('Digite el nombre de la pelicula: ')
        pelicula = Pelicula(nombre_peli)
        cp.agregar_peliculas(pelicula)
    elif opcion == 2:
        cp.listar_peliculas()
    elif opcion == 3:
        cp.eliminar_peliculas()
else:
    print('Adios vuelva prontos')