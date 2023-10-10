#no repetir caracteres

cadena = input("digite una cadena: ")
lista = []
for i in cadena:
    if i not in lista: # si el caracter no esta en la lista
        lista.append(i)  #lo agregamos a ala lsita
print(f'\nLista de caracteres sin repetidos: \n {lista}')