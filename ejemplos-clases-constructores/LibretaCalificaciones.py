class LibretaNotas:
    def __init__(self, nombre_estudiante, calificacion1, calificacion2, calificacion3):
        self.nombre_estudiante = nombre_estudiante
        self.calificacion1 = calificacion1
        self.calificacion2 = calificacion2
        self.calificacion3 = calificacion3
        self.promedio = None

    def establecer_nombre_estudiante(self, nombre):
        self.nombre_estudiante = nombre

    def establecer_calificacion1(self, calificacion):
        self.calificacion1 = calificacion

    def establecer_calificacion2(self, calificacion):
        self.calificacion2 = calificacion

    def establecer_calificacion3(self, calificacion):
        self.calificacion3 = calificacion

    def calcular_promedio(self):
        self.promedio = (self.calificacion1 + self.calificacion2 + self.calificacion3) / 3

    def obtener_nombre_estudiante(self):
        return self.nombre_estudiante

    def obtener_calificacion1(self):
        return self.calificacion1

    def obtener_calificacion2(self):
        return self.calificacion2

    def obtener_calificacion3(self):
        return self.calificacion3

    def obtener_promedio(self):
        return self.promedio

    def __str__(self):
        return f"Libreta de Calificaciones\n" \
               f"Nombre del estudiante: {self.nombre_estudiante}\n" \
               f"Calificacion 1: {self.calificacion1:.2f}\n" \
               f"Calificacion 2: {self.calificacion2:.2f}\n" \
               f"Calificacion 3: {self.calificacion3:.2f}\n" \
               f"Promedio: {self.promedio:.2f}\n"



libreta1 = LibretaNotas("Alisson", 10, 9.2, 9)
libreta1.calcular_promedio()

print(libreta1)


