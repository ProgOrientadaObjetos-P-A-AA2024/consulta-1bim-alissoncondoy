class Ropa:
    def __init__(self, tipo, color, talla):
        self.tipo = tipo
        self.color = color
        self.talla = talla

    def mostrar_informacion(self):
        print("Tipo de ropa:", self.tipo)
        print("Color:", self.color)
        print("Talla:", self.talla)

ropa1 = Ropa("Camiseta", "Azul", "M")
ropa2 = Ropa("Pantalón", "Negro", "L")

print("Información de la ropa 1:")
ropa1.mostrar_informacion()
print("\nInformación de la ropa 2:")
ropa2.mostrar_informacion()
