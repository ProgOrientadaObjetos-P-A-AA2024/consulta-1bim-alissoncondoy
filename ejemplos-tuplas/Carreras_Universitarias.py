carreras_universitarias = (
    "Ingeniería en Informática",
    "Medicina",
    "Administración de Empresas",
    "Derecho",
    "Arquitectura",
    "Psicología"
)

areas_carreras = (
    ("Tecnología", "Ingeniería en Informática"),
    ("Ciencias de la Salud", "Medicina"),
    ("Ciencias Sociales", "Administración de Empresas", "Derecho", "Psicología"),
    ("Arquitectura y Diseño", "Arquitectura")
)

for carrera in carreras_universitarias:
    for area, *carreras in areas_carreras:
        if carrera in carreras:
            print(f"{carrera}: {area}")


