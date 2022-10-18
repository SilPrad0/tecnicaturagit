#funcion con *args para multiplicar, argumentos variables

def multiplicar_valores(*numeros):
    resultado = 1 #con ceero no se puede multiplicar nada
    for numero in numeros:
        resultado *= numero
    return resultado
print(multiplicar_valores(3, 5, 6, 0)) #argumentos
