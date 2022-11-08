class Aritmetica:
    """
    el nombre de este tipo de comentario es DocString, doc de la clase en python
    """

    def __init__(self, operadorA, operadorB):
        self.operadorA = operadorA
        self.operadorB = operadorB

    def sumar(self):
        return self.operadorA + self.operadorB
    def resta(self):
        return self.operadorA - self.operadorB
    def multiplicacion(self):
        return self.operadorA * self.operadorB
    def division(self):
        return self.operadorA / self.operadorB



aritmetica1 = Aritmetica(7, 9)
print(aritmetica1.sumar())
print(f'La resta de es: {aritmetica1.resta()}')
print(f'La multiplicacion es: {aritmetica1.multiplicacion()}')
print(f'La division es: {aritmetica1.division():.2f}')