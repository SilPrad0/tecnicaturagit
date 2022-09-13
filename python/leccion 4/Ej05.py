# factorial de un numero positivo
numero = int(input("digite un numero: "))
while numero < 0:
    print("error -> el numero tiene que ser positivo")
    numero = int(input("digite un numero: "))
factorial = 1 #variable para factorial
for i in range(1, numero+1):
    factorial *= i
print(f'\nEl factorial de numero {numero} positivo ingresado es: {factorial}')

