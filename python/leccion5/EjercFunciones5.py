#celsius a fahrenheit, viceversa

def c_f(celsius):
    return celsius * 9 / 5 + 32
celsius = float(input('digite el valor de celsius: '))
resultado = c_f(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

def f_c(fahrenheit):
    return fahrenheit - 32 * 9 / 5 #los parentesis resuelven primero en caso del profe, en el mio
                                   # es SIN parentesis idk why
fahrenheit = float(input('digite el valor de fahrenheit: '))
resultado1 = f_c(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado1:.2f}')