#funciones
#definimos la funcion
def mi_funcion(): #para identificarla usamos parentesis
    print("hola")

mi_funcion() #llamo la funcion

# desempaquetado de listass o list unpacking
def show(name, lastName):
    print(name+''+lastName)
person = ["Silvina", "Prado"]
show(person[0], person[1])  #pasamos uno por uno los datos de la lista a la func
show(*person) #lo mismo de diferente manera todo junto
person2 = ("Silvina", "Prado") #unpack una tupla
show(*person2)
person3 = {"lastName": "Prado", "name": "sil"}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
else:
    print("esto se termina")

# lista de comprension
names = ["pepe", "papa", "raa", "qee"]
alongP = [p for p in names if p[0] == 'p'] #condicion-- regresa una nueva lista
print(alongP)

bottleC = [{"name": "quilmes", "country": "arg"},
           {"name": "corona", "country": "mx"}]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de argumentos (funciones




#palabra return en funciones

def sumar(a , b):
    return a + b
resultado = sumar(78, 22)
print(f'el resultado de la suma es: {resultado}')

def sumar2(a = 0, b = 0): #valor por default
    return a + b
resultado2 = sumar2()
print(f'Resulltado: {resultado2}')
print(f'resultado: {sumar2(22, 550)}')

# argumentos, var en funciones
def listasNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listasNombres("ernesto", "sil", "eejej")
listasNombres("marcos","pepe","etc")