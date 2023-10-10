#ejerc6: tabla de multiplicar

numero = int(input("digite un numero: "))
lista = []
for i in range(1,11):
    lista.append((i*numero))
print(f'\nTabla de multiplicar del {numero}: \n {lista}')