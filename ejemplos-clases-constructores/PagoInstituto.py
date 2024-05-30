class PagoInstituto:
    def __init__(self, n, p, b, c):
        self.nombre = n
        self.apellido = p
        self.sueldoBasico = b
        self.cedula = c
        self.sueldoTotal = 0.0
    
    def calcularSueldoTotal(self):
        self.sueldoTotal = self.sueldoBasico + (0.2 * self.sueldoBasico)
    
    def establecerNombre(self, x):
        self.nombre = x
    
    def establecerApellido(self, x):
        self.apellido = x
    
    def establecerSueldoBasico(self, x):
        self.sueldoBasico = x
    
    def establecerCedula(self, x):
        self.cedula = x
    
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerApellido(self):
        return self.apellido
    
    def obtenerSueldoBasico(self):
        return self.sueldoBasico
    
    def obtenerSueldoTotal(self):
        return self.sueldoTotal
    
    def obtenerCedula(self):
        return self.cedula
    
    def __str__(self):
        cadena = "Pago Profesores\n"
        cadena += f"Nombre: {self.obtenerNombre()}\n"
        cadena += f"Apellido: {self.obtenerApellido()}\n"
        cadena += f"Sueldo basico: {self.obtenerSueldoBasico():.2f}\n"
        cadena += f"Sueldo total: {self.obtenerSueldoTotal():.2f}\n"
        cadena += f"Cedula: {self.obtenerCedula()}\n"
        return cadena

if __name__ == "__main__":
    pago1 = PagoInstituto("Alisson", "Condoy", 350.95, "1150261665")
    pago1.calcularSueldoTotal()
    
    print(pago1)
