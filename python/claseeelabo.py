"""
x = 10
print(x)
print(type(x))
y = 14.5
print(y)
print(type(y))
e = True
print(type(e))
print("hola silvi")
# Strings
miGrupoFavorito = "tautumeitaswe:"
caracteristicas = "the best"
print("el grupo favorito es:", miGrupoFavorito, caracteristicas)

#numero1 = "7"
#numero2 = "8"
#print(int(numero1) + int(numero2))

# Tipos Booleanos
mibooleano = 3 > 2
print(mibooleano)

if mibooleano:
    print("el resultado es: verdadero")
else:
    print("el resultado es: falso")

# procesar entrada de usuario
# resultado = input("ingrese un numero: ") # regresa un dato tipo str
# print(resultado)

# conversion de la entrada de datos
numero1 = input("escribe el primer numero: ")
numero2 = input("escribe el segundo numero: ")
resultado = (int(numero1) / int(numero2))
print("el resultado de la suma es: ", resultado)
# operadores aritmeticos
Aaa = 514
Bbb = 48
suma = Aaa + Bbb
#print("resultado:", suma)
print(f'el resultado de la suma es: {suma}')

resta = Aaa - Bbb
print(f'el rto de la resta es: {resta}')

division = Aaa / Bbb
print(f'el rtdo blablad: {division}')

division_tipo_entero= Aaa // Bbb
print(f'divisiontipo entero: {division_tipo_entero}')


exponente = Aaa ** 2
print(f'exponente a la 2: {exponente}')

residuo = Aaa % Bbb
print(f'el residuo es: {residuo}')

# vamo aser un reptangulo
alto = int(input("escribe el alto del reptansddgoulo:"))
ancho = int(input("escribe el amcho:"))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'el area es: {area}, el perimetro es: {perimetro}')

mivar = 10
print(mivar)

# op de reasignacion
mivar = mivar + 1
print(mivar)

mivar += 1
print(mivar)

mivar -= 2
print(mivar)

mivar *= 3
print(mivar)
mivar //= 2
print(mivar)


tunumero = int(input("escribe el numero: "))
if 0<= tunumero <=5: print("el numero esta dentro")
else: print("el numero esta afuera")

#a mi maneeeera
num = int(input("escribe tu edad: "))
if 20 <= num <= 30:
    print("tu edad esta dentro del rango")
else:
    print("no esta dentro del rango")
if num >= 100:
    print("y sos muy viejo")

num1 = int(input("ingrese el numero1: "))
num2 = int(input("ingrese el numero2: "))

if num1 > num2:
    print("el numero 1 es mayor")
else:
    print("el numero 2 es mayor")

#hacer el coso del libro

# Clase para el if/else acordate de abrir una nueva file y commitear



condicion = True
if condicion == True:
    print("condicion verdadera")
elif condicion == False:
    print("falsa")
else:
    print("condicion sin especificar")



nombre = str(input("digite el nombre del libro: "))
Id = int(input("digite el id del libro: "))
precio = int(input("digite el precio del libro: "))
envioGratis = True
print("nombre:", nombre)
print("Id: ", Id)
print("precio:", precio)

# calcular estacion del año
mes = int(input("digite un mes del año (1 - 12): "))
estacion = None
if mes == 1 or mes == 2 or mes == 3:
    estacion = "Verano"
elif mes == 4 or mes == 5 or mes == 6:
    estacion = "Otoño"
elif mes == 7 or mes == 8 or mes == 9:
    estacion = "Invierno"
elif mes == 10 or mes == 11 or mes ==  12:
    estacion = "Primavera"
else:
    estacion = "error"
print(f"para el {mes} la estacion es: {estacion}")

edad = int(input("ingrese su edad: "))
oracion = None
if 0 <= edad < 10:
 oracion = "la infancia es increible y bella"
elif 10 <= edad <19:
    oracion = "cambios y estudio"
elif 20 <= edad <29:
    oracion = "amor y trabajo, ponele"
elif 30 <= edad <39:
    oracion = "lo que quieras hacer basicamente"
elif 40 <= edad <50:
    oracion = "no hay edad para nada"
elif 51 <= edad <65:
    oracion = "nunca es tarde mientras haya vida ah se inspiraba"
else:
    oracion = "etapa no descripta"
print(f"Tu edad es: {edad}, {oracion}")

# sistema de calificaciones
nota = int(input("ingrese su calificacion: "))
calif = None
if nota == 9 or nota == 10:
    calif = "A"
elif nota == 8 or nota == 9:
    calif = "B"
elif nota == 7 or nota == 8:
    calif = "C"
elif nota == 6 or nota == 7:
    calif = "D"
elif 0 <= nota <6:
    calif = "F"
else:
    calif = "error no existe"
print(f"Tu nota es: {nota}, y equivale a: {calif}")

# contador while
contador = 0
while contador <10:
    print("ejecuto ciclo while",contador)
    contador +=1

# imprimir numeros del 0 al 5
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1

minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1

#Ciclo for
cadena = "hello"
for letra in cadena:
    print(letra)
else:
    print("fin del ciclo for")

#palabra reservada break
for letra in "Alemania":
    if letra == "a":
        print(f"letra encontrada: {letra}")
        break       #solo busca una letra a
else:
        print("fin del ciclo for")

# Continue
for i in range(6):
    if i % 2 == 0:
        print(f"valor: {i}")

for i in range(6):
    if i % 2 != 0:
        continue
    print(f"valor: {i}")

#año bisiesto
año = int(input('Introduce un año: '))
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print('El año es bisiesto')
        else:
            print('El año no es bisiesto')
    else:
        print('El año es bisiesto.')
else:
    print('El año no es bisiesto.')

cantidad = int(input("digite la cantidad a sumar: "))
cont = 0
suma = 0
num = 0
while cont <cantidad:
    num = int(input("digite un numero: "))
    suma = suma + num
    cont += 1
    print(suma)

#ejercicio3
positivos = 0
cont = 0
negativo = 0
neutro = 0
num = 0
while cont < 10:
    num = int(input("digite un numero: "))
    if num > 0:
        positivos = positivos +1
    elif num <0:
        negativo = negativo +1
    elif num == 0:
        neutro = neutro +1
    cont +=1
print(f"la cantidad de positivos es: {positivos}")
print(f"la cantidad de negativos es: {negativo}")
print(f"la cantidad de nros neutros es: {neutro}")

#calificaciones
cont = 0
suma = 0
calificacion = 0
calificacionBaja = 9999
while cont < 10:
    calificacion = int(input("digite la calificacion: "))
    suma = suma + calificacion
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion
        cont += 1
promedio = suma/10
print(f"la calificacion promedio es: {promedio}")
print(f"la calificacion mas baja es: {calificacionBaja}")

# factorial de un nro
num = int(input("ingrese un numero: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f'el factorial del numero {num} es: {factorial}')
"""
# numeros pares e impares
pares = 0
impares = 0
i = +1
sumaPares = 0
sumaImpares = 0
promedioImpares = 0
cantidadTotal = int(input(f'ingrese la cantidad de numeros: \n'))
cantidadTotal +=1

while i < cantidadTotal:
    num = int(input(f'ingrese el numero {i}: '))
    if num % 2 == 0:
         pares += 1
         sumaPares += num
    else:
         impares += 1
         sumaImpares += num
         i += 1
promedioImpares = sumaImpares/impares

print(f'\nSuma de numeros pares: {sumaPares}')
print(f'Cantidad de numeros pares: {pares}')
print(f'Promedio de numeros impares: {promedioImpares}')
