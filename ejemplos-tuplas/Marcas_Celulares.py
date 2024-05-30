# Tupla de marcas de teléfonos móviles
marcas_celulares = (
    "Apple",
    "Samsung",
    "Huawei",
    "Xiaomi",
    "OnePlus",
    "Google"
)

categorias_celulares = (
    ("Premium", "Apple", "Samsung"),
    ("Intermedio", "Huawei", "Xiaomi", "OnePlus"),
    ("Económico", "Xiaomi", "OnePlus", "Google")
)

for categoria, *marcas in categorias_celulares:
    print(f"Categoría: {categoria}")
    print("Marcas:")
    for marca in marcas:
        print(f"- {marca}")
    print()
