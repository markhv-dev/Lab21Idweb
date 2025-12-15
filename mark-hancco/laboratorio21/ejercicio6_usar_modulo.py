# Laboratorio 21 - Ejercicio 6
# Autor: Mark Hancco Vargas
# Colaboro: Claude AI
# Tiempo: --

from geometria import Rectangulo, Triangulo, Circulo

# Pruebas usando el modulo
if __name__ == "__main__":
    print("=== Usando modulo geometria.py ===\n")

    figuras = [
        Rectangulo(5, 3),
        Triangulo(4, 3, 3, 4, 5),
        Circulo(2)
    ]

    for fig in figuras:
        print(f"{fig}")
        print(f"  Area: {fig.area():.2f}")
        print(f"  Perimetro: {fig.perimetro():.2f}")
        print()
