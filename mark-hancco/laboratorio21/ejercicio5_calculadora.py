# Laboratorio 21 - Ejercicio 5
# Autor: Mark Hancco Vargas
# Colaboro: Claude AI
# Tiempo: --

class OperadorInvalidoError(Exception):
    def __init__(self, operador):
        self.operador = operador
        super().__init__(f"Operador '{operador}' no valido. Use: + - * /")

def calcular(operacion):
    partes = operacion.split()

    if len(partes) != 3:
        raise ValueError("Formato invalido. Use: 'numero operador numero'")

    num1_str, operador, num2_str = partes

    # Validar operador
    if operador not in ['+', '-', '*', '/']:
        raise OperadorInvalidoError(operador)

    # Convertir numeros
    num1 = float(num1_str)
    num2 = float(num2_str)

    # Realizar operacion
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return num1 / num2

# Pruebas
if __name__ == "__main__":
    operaciones = [
        "10 + 5",
        "20 - 8",
        "4 * 3",
        "10 / 2",
        "10 / 0",      # Division entre cero
        "abc + 5",     # Valor invalido
        "10 % 3",      # Operador invalido
    ]

    for op in operaciones:
        print(f"Operacion: {op}")
        try:
            resultado = calcular(op)
            print(f"  Resultado: {resultado}")
        except ZeroDivisionError as e:
            print(f"  Error: {e}")
        except ValueError as e:
            print(f"  Error de valor: {e}")
        except OperadorInvalidoError as e:
            print(f"  Error: {e}")
        print()
