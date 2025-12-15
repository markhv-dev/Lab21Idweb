# Laboratorio 21 - Ejercicio 4
# Autor: Mark Hancco Vargas
# Colaboro: Claude AI
# Tiempo: --

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado.")
            return True
        else:
            print(f"Libro '{self.titulo}' no disponible.")
            return False

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto.")
            return True
        else:
            print(f"Libro '{self.titulo}' ya estaba disponible.")
            return False

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' de {self.autor} ({self.anio}) - {estado}"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, tamano_mb):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.tamano_mb = tamano_mb

    def prestar(self):
        print(f"Libro digital '{self.titulo}' ({self.formato}) accedido. Siempre disponible.")
        return True

    def __str__(self):
        return f"[Digital] '{self.titulo}' de {self.autor} ({self.anio}) - {self.formato}, {self.tamano_mb}MB - Siempre disponible"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def listar_libros(self):
        print("\n=== CATALOGO DE BIBLIOTECA ===")
        for libro in self.libros:
            print(f"  - {libro}")
        print()

    def buscar_por_autor(self, autor):
        resultados = [l for l in self.libros if autor.lower() in l.autor.lower()]
        print(f"\nLibros de '{autor}':")
        for libro in resultados:
            print(f"  - {libro}")
        return resultados

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro.prestar()
        print(f"Libro '{titulo}' no encontrado.")
        return False

# Pruebas
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Crear libros fisicos
    libro1 = Libro("Cien anos de soledad", "Gabriel Garcia Marquez", 1967)
    libro2 = Libro("El amor en los tiempos del colera", "Gabriel Garcia Marquez", 1985)
    libro3 = Libro("1984", "George Orwell", 1949)

    # Crear libros digitales
    digital1 = LibroDigital("Python Crash Course", "Eric Matthes", 2019, "PDF", 15)
    digital2 = LibroDigital("Clean Code", "Robert Martin", 2008, "EPUB", 8)

    # Agregar a biblioteca
    for libro in [libro1, libro2, libro3, digital1, digital2]:
        biblioteca.agregar_libro(libro)

    # Listar todos
    biblioteca.listar_libros()

    # Prestar libro fisico
    print("--- Prestando libro fisico ---")
    biblioteca.prestar_libro("1984")

    # Prestar libro digital 5 veces
    print("\n--- Prestando libro digital 5 veces ---")
    for i in range(5):
        biblioteca.prestar_libro("Python Crash Course")

    # Intentar prestar libro ya prestado
    print("\n--- Intentando prestar libro ya prestado ---")
    biblioteca.prestar_libro("1984")

    # Buscar por autor
    print("\n--- Buscando por autor ---")
    biblioteca.buscar_por_autor("Gabriel Garcia Marquez")

    # Listar estado final
    biblioteca.listar_libros()
