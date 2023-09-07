from NumerosIgualesExc import NumerosIgualesExc
resultado = None

try:
    a = 10
    b = 10

    if a == b:
        raise NumerosIgualesExc('Son nros iguales')

    resultado = a / b
except Exception as e:
    print(f'Ocurrio un error: {e}')
else:
    print('No hubo excepcion alguna')
finally:
    print('ejecucion de este bloque finally')
print(f'El resultado es: {resultado}')
print('seguimooo...')
