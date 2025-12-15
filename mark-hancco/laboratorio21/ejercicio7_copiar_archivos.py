# Laboratorio 21 - Ejercicio 7
# Autor: Mark Hancco Vargas
# Colaboro: Claude AI
# Tiempo: --

def copiar_texto(origen, destino):
    """Copia archivos de texto"""
    try:
        with open(origen, 'r', encoding='utf-8') as f_origen:
            contenido = f_origen.read()

        with open(destino, 'w', encoding='utf-8') as f_destino:
            f_destino.write(contenido)

        print(f"Archivo de texto copiado: {origen} -> {destino}")
        return True
    except FileNotFoundError:
        print(f"Error: Archivo '{origen}' no encontrado")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def copiar_binario(origen, destino):
    """Copia archivos binarios"""
    try:
        with open(origen, 'rb') as f_origen:
            contenido = f_origen.read()

        with open(destino, 'wb') as f_destino:
            f_destino.write(contenido)

        print(f"Archivo binario copiado: {origen} -> {destino}")
        return True
    except FileNotFoundError:
        print(f"Error: Archivo '{origen}' no encontrado")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# Pruebas
if __name__ == "__main__":
    # Crear archivo de prueba
    with open("archivo_prueba.txt", "w") as f:
        f.write("Este es un archivo de prueba.\nLinea 2.\nLinea 3.")

    # Copiar texto
    print("--- Copiando archivo de texto ---")
    copiar_texto("archivo_prueba.txt", "copia_texto.txt")

    # Verificar
    with open("copia_texto.txt", "r") as f:
        print(f"Contenido copiado:\n{f.read()}")

    # Copiar binario (usamos el mismo archivo como ejemplo)
    print("\n--- Copiando archivo binario ---")
    copiar_binario("archivo_prueba.txt", "copia_binario.txt")

    # Verificar
    with open("copia_binario.txt", "rb") as f:
        print(f"Bytes copiados: {len(f.read())} bytes")
