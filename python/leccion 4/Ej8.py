# menu interactivo
saldo = 1000
while True
    print("\t.:Menu:.")
    print("1.Ingresar dinero en la cuenta")
    print("2.Retirar dinero de la cuenta")
    print("3.Mostrar dinero disponible")
    print("4.Salir")
    opcion = int(input("digite una opcion del menu: "))
    print()
    if opcion == 1:
        extra = float(input("cuanto dinero desesa ingresar -> "))
        saldo += extra
        print(f'Dinero disponible: ${saldo}')
    elif opcion == 2:
        retirar = float(input("cuanto dinero desea retirar ->"))
        if retirar > saldo:
            print("no tiene dinero para retirar")
        else:
            saldo -= retirar
            print(f'Dinero disponible: {saldo}')
    elif opcion == 3:
