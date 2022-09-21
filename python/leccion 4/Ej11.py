#agenda telefonica

agenda = {}
while True:
    print('\t.:Menu:.')
    print('1.Nuevo contacto')
    print("2.Borrar contacto")
    print("3.Ver contactos existentes")
    print("4.Salir")
    opcion = int(input("digite una opcion de menu: "))
    if opcion == 1:
        nombre = input("digite el nombre: ")
        telefono = input("digite el numero: ")
        print("opcion incorrecta")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("contacto agregado")
        else:
            print('ese nombre de contacto ya existe')
    elif opcion == 2:
        nombre = input("nombre de contacto: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("Ha sido eliminado")
        else:
            print("El contacto no existe")
    elif opcion == 3:
        print("Agenda de contactos")
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Telefono: {valor}')
    elif opcion == 4:
        print("blablabla")
        break
    else:
        print("opcion erronea")
    print()