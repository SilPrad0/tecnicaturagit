#Ejercicio 3: Funcion recursiva: imprimir numeros de 5 a 1 descend
#usando f recursivas

def imprimir_num_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_num_recursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('valor incorrecto')
numero1 = int(input('digite un numero: '))
rtdo = imprimir_num_recursivos(numero1) #tareaaa

