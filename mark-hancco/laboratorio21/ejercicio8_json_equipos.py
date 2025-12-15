# Laboratorio 21 - Ejercicio 8
# Autor: Mark Hancco Vargas
# Colaboro: Claude AI
# Tiempo: --

import json

equipos = [
    {
        "nombre": "Real Madrid",
        "pais": "Espana",
        "nivelAtaque": 95,
        "nivelDefensa": 88
    },
    {
        "nombre": "Manchester City",
        "pais": "Inglaterra",
        "nivelAtaque": 94,
        "nivelDefensa": 90
    },
    {
        "nombre": "Bayern Munich",
        "pais": "Alemania",
        "nivelAtaque": 92,
        "nivelDefensa": 87
    },
    {
        "nombre": "Barcelona",
        "pais": "Espana",
        "nivelAtaque": 90,
        "nivelDefensa": 82
    },
    {
        "nombre": "Inter Milan",
        "pais": "Italia",
        "nivelAtaque": 85,
        "nivelDefensa": 89
    }
]

# Convertir a JSON y mostrar
if __name__ == "__main__":
    json_string = json.dumps(equipos, indent=4, ensure_ascii=False)
    print("=== Lista de equipos en formato JSON ===\n")
    print(json_string)

    # Guardar en archivo
    with open("equipos.json", "w", encoding="utf-8") as f:
        json.dump(equipos, f, indent=4, ensure_ascii=False)

    print("\n[Guardado en equipos.json]")
