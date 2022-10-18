#Mostrar frase sin espacios

frase1 = input("digite una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f'\nFrase final: {frase1}')
print(f'N° de caracteres: {len(frase1)}')
