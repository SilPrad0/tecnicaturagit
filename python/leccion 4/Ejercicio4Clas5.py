#4: suman numeros pares dentro de un rango
a = int(input("digite el numero donde comenzara la suma: "))
b = int(input("digite hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a, b+1):
    if i % 2 == 0: #si par
        suma += i
print(f'\nLa suma de numeros pares dentro del rango es: {suma}')