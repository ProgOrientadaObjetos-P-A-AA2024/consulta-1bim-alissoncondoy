class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


triangulo1 = Triangulo(5.2, 10)
triangulo2 = Triangulo(3.5, 6)


print("Área del triángulo 1:", triangulo1.calcular_area())
print("Área del triángulo 2:", triangulo2.calcular_area())

