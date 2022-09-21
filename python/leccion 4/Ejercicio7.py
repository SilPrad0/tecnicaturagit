#Adivina el numero, generar un nro aleatorio entre 1 - 100
#pedir numeros indicando segun mayor o menor. termina cuando se acierta

import random
aleatorio = random.randint(0,100)
contador = 0
while True:
    numero = int(input("digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print('\tNo es el numero, digite un numero menor')
    elif numero < aleatorio:
        print('\tNo es el numero, digite un numero mayor')
    else:
        print(f'Felicidades, acertaste el nmero {aleatorio}')