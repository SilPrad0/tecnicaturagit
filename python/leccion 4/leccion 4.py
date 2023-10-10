"""
# listas
nombres = ['a', 'b', 'c', 'd', 'f', 'e']
# print(nombres[2]) #muestra elemento con num de indice
# print(nombres[-1]) #muestra el ultimo
# print(nombres[1:4]) #recupera un rango de la lista
# print(nombres[ :4]) #ir del inicio de la lista al indice
# print(nombres[3: ]) #desde el indice indicado hasta el final

# modificar un valor
nombres[3] = "abc"
# print(nombres)

for nombre in nombres: #iterar una lista
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")
#Preguntar cuantos elementos hay
#print(len(nombres))

# AGREGAR un elemento
nombres.append("hola")
#nombres.insert(3, "hola2")  # insertar en un indice especifico
nombres.remove("abc") #elimina elemento con dato str
nombres.pop() #elimina el ultimo elemento por default
del nombres[3] #elimina elemento en indice especifico
nombres.clear() #elimina todos los elementos 
del nombres #elimina la lista

#EJERCICIO1
for i in range(11):
    if i % 3 ==0:
        print(i)

#EJERCICIO2
print('rando de valores de inicio 2 y fin 6')
rango = range(2, 7)
for i in rango:
    print(i)

#EJERCICIO3
print('rango incio 3 fin 10 incremento 2')
for i in range(3, 11, 2):
    print(i)

#Tuplas
cocina = ('cuchara', 'cuchillo', 'tenedor')
#print(len(cocina))
#print(cocina[2]) #para acceder a un elemento
#print(cocina[-1]) #muestra el ultimo
#print(cocina[0:2]) #acceder a un rango
#recorrer elementos
#for cocinar in cocina:
   # print(cocinar)
    #print(cocinar, end=' ')

#Ejercicio 1
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)



# tipo set
planetas = {'Marte', 'Jupiter', 'Venus'}
#print(len(planetas)) #muestra cantidad

#revisar si un elemento existe dentro de un set
#print('Marte' in planetas)

#agregar un elemento
#planetas.add('Saturno')
#print(planetas)

#eliminar elementos, puede arrojar un error si no existe
#planetas.remove('Jupiter')
#print(planetas)
#planetas.discard('Marte') #no presenta error si hay typo, si esta mal no lo borra
#print(planetas)

#limpiar set
#planetas.clear()
#print(planetas)

#eliminar set
del planetas
print(planetas)

#diccionario
diccionario = {
    'IDE':'Integrated development enviroment',
    'POO':'programacion orientada a objetos',
    'SABD':'Sistema de administracion de base de datos'
}
#print(len(diccionario))
#print(diccionario['IDE']) #al no tener indice ingreso con el elemento

print(diccionario.get('POO'))

#modifcar elementos
diccionario['IDE'] = 'Entorno de desarrollo integrado'

#recorrer elementos
#for termino in diccionario: #recorremos solo las llaves
    #print(termino)

for termino, valor in diccionario.items():  #muestra valor con funcion
    print(termino,valor)

#otra manera de acceder
for termino in diccionario.keys():
    print(termino)

#muestra valores
for valor in diccionario.values():
    print(valor)
#agregar elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

#eliminar elemento
diccionario.pop('IDE')
print(diccionario)

#concatenar LISTAS
lista1 = [1, 2, 3, 9]
lista2 = [11, 12, 13]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 10]) #agrega varios elementos
print(lista3)
print(lista3.index(1)) #ubicar elemento, nos muestra el indice/ubicacion

#como saber cuantos valores repetidos hay en una lista
print(lista3.count(1))
#al reves
lista3.reverse()
print(lista3)

#para que una lista se multiplique sus elementos
lista3 = lista3 * 2
print(lista3)
# metodos de ordenamiento
lista3.sort() #menor a mayor
print(lista3)
lista3.sort(reverse=True) #mayor a menor
print(lista3)

# REPASO TUPLAS
tupla = (4, 'Hi', 12.4, [1, 2, 3,], 4, 'Hi')
print(tupla)

print(4 in tupla) #saber si esta el elemento, rta bool
# podemos usar en tupla: index, count, len
# se puede convertir de tupla a lista y viceversa

conjunto1 = set()
conjunto2 = set()
conjunto1.add(5)
conjunto1.add('hola')
conjunto2.add(9)
conjunto2.add("hey")
print(conjunto1 == conjunto2) #para saber si son iguales
conjunto3 = conjunto1 | conjunto2 #unir ambbos conjuntos
print(conjunto3)
conjunto3 = conjunto1 & conjunto2 #elementos en comun
print(conjunto3)
conjunto3 = conjunto1 ^ conjunto2 #no compartidos
print(conjunto3)
print(conjunto1.issubset(conjunto3)) #para saber si es subconjunto
print(conjunto3.issuperset(conjunto1)) #superconjunto
#saber si son disconexos
print(conjunto1.isdisjoint(conjunto2))
#convertir en inmutable un set
conjunto1 = frozenset


#repaso dicc
diccionarioNuevo = {"azul": "blue", "rojo" : "red", "verde" : "green", "amarillo" : "yellow"}
print(diccionarioNuevo)
del (diccionarioNuevo["azul"])
print(diccionarioNuevo)

#pueden almacenar diferente tipos de datos
diccionario2 = {"silvina": {"edad" : 25, "altura" : 1.65}, "etc": [23, 1.89]}
print(diccionario2)

seleccionArgentina = {
    10: {"nombre": "messi", "edad": 35, "altura": 1.70, "precio": "50 millones", "posicion": "extremo derecho"},
    11: {"nombre": "fideo", "edad": 34, "altura": 1.80, "precio": "12 millones", "posicion": "extremo derecho"},
    24: {"nombre": "dybala", "edad": 28, "altura": 1.77, "precio": "35 millones", "posicion": "media punta"},
    19: {"nombre": "otamendi", "edad": 34, "altura": 1.83, "precio": "3 millones", "posicion": "defensa central"},
    1: {"nombre": "armani", "edad": 35, "altura": 1.89, "precio": "3.4 millones"},
    3: {"nombre": "nidea", "edad": 23, "altura":1234, "precio": "un monton", "posicion": "el misionero"}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

#pilas usando listas
pila = [1, 2, 3]
#agregar elementos a la pile por el final
pila.append(4)
pila.append(5)
print(pila)
#sacar elementos del final
elementoBorrado = pila.pop() #elimina el ultimo y lo guarda en la variable
print(f"sacamos el elmento",[elementoBorrado])

#colas con listas
#estructuras de datos tipo fifo (first input/first output)
cola = ["sil", "etc", "ola", "eh"]
cola.append("ndea")
cola.append("otromas")
print(cola)
seRetira = cola.pop()
print(f"atendido el cliente: {seRetira}")

#EJERCICIO 1 clase 4
lista = [1, 2, 3, 4, "sil", 7, 7, 3, "sil", 5, "e"]
# conjunto = set(lista) #convertimos lista a set
# lista = list(conjunto) #convertimos set a lista
lista = list(set(lista)) #una sola linea (eficiente)
print(lista)

# ejercicio 2 / a mi maneeeeeraaa
lista1 = ["inglés", "alemán", "italiano", "francés", "español", "chino"]
lista2 = ["chino", "portugues", "letón", "japonés", "francés"]
conjunto1 = set(lista1)
conj2 = set(lista2)
conj3 = conjunto1 | conj2
print(list(conj3)) #lista de palabras en la q aparecen las dos listas unidas
print(list(conjunto1 - conj2)) #que aparecen en la primera pero no en la segunda
print(list(conj2 - conjunto1)) #aparecen en la segunda y no en la primera
conj4 = conjunto1 & conj2
print(list(conj4)) #que aparecen en ambas listas

#ejercicio 3
personajes = []
p = {"Nombre": "Aragorn", "Clase": "Guerrero", "Raza": "Dinadan del norte"}
personajes.append(p)
p = {"nombre": "Gandalf","clase": "mago", "raza": "istar"}
personajes.append(p)
p =  {"nombre": "legolas", "clase": "arquero", "raza": "elfo sindar"}
personajes.append(p)
print(personajes) ///sumar mas personajes

#raiz cuadrada
import math

numero = int(input("Digite un numero positivo:"))
while numero < 0:
    print("error, debe ser un numero positivo")
    numero
print(f'\nsu raiz cuadrada es: {math.sqrt(numero):.2f}')
"""