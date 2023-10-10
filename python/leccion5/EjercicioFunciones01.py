# ejercicio 1, funcion para sumar los valores recibidos de tipo num,
# utilizando argumentos variables args como parametro de la func, rtdo suma

def sumar_valor(*args):  # recibimos cantidad de parametros indef
    resultado = 0
    for valor in args: #iteramos cada elemento
        resultado += valor
    return resultado

#llamo funcion
print(sumar_valor(3, 5, 9, 8))
