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
    """
num1 = int(input("ingrese el numero1: "))
num2 = int(input("ingrese el numero2: "))

if num1 > num2:
    print("el numero 1 es mayor")
else:
    print("el numero 2 es mayor")

#hacer el coso del libro