# Laboratorio 21 - Ejercicio 3
# Autor: Mark Hancco Vargas
# Colaboro: Claude AI
# Tiempo: --

import math

class Figura:
    def area(self):
        pass

    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f"Rectangulo(base={self.base}, altura={self.altura})"

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def __str__(self):
        return f"Triangulo(base={self.base}, altura={self.altura})"

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Circulo(radio={self.radio})"

# Pruebas
if __name__ == "__main__":
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
