# Laboratorio 21 - Ejercicio 9
# Autor: Mark Hancco Vargas
# Colaboro: Claude AI
# Tiempo: --

import threading
import asyncio
import multiprocessing
import time
import random

def consulta_db(nombre, tiempo):
    """Simula consulta a base de datos"""
    print(f"[{nombre}] Iniciando consulta...")
    time.sleep(tiempo)
    print(f"[{nombre}] Consulta completada en {tiempo}s")
    return f"Resultado de {nombre}"

async def consulta_db_async(nombre, tiempo):
    """Simula consulta asincrona"""
    print(f"[{nombre}] Iniciando consulta...")
    await asyncio.sleep(tiempo)
    print(f"[{nombre}] Consulta completada en {tiempo}s")
    return f"Resultado de {nombre}"

def ejecutar_con_hilos():
    """Ejecuta consultas usando hilos"""
    print("\n=== USANDO HILOS (threading) ===")
    tiempos = [random.randint(1, 5) for _ in range(3)]
    inicio = time.time()

    hilos = []
    for i, t in enumerate(tiempos):
        h = threading.Thread(target=consulta_db, args=(f"Consulta{i+1}", t))
        h.start()
        hilos.append(h)

    for h in hilos:
        h.join()

    total = time.time() - inicio
    print(f"Tiempo total con hilos: {total:.2f}s")
    return total

async def ejecutar_con_async():
    """Ejecuta consultas usando asyncio"""
    print("\n=== USANDO ASYNCIO ===")
    tiempos = [random.randint(1, 5) for _ in range(3)]
    inicio = time.time()

    await asyncio.gather(
        consulta_db_async("Consulta1", tiempos[0]),
        consulta_db_async("Consulta2", tiempos[1]),
        consulta_db_async("Consulta3", tiempos[2])
    )

    total = time.time() - inicio
    print(f"Tiempo total con asyncio: {total:.2f}s")
    return total

def ejecutar_con_procesos():
    """Ejecuta consultas usando procesos"""
    print("\n=== USANDO PROCESOS (multiprocessing) ===")
    tiempos = [random.randint(1, 5) for _ in range(3)]
    inicio = time.time()

    procesos = []
    for i, t in enumerate(tiempos):
        p = multiprocessing.Process(target=consulta_db, args=(f"Consulta{i+1}", t))
        p.start()
        procesos.append(p)

    for p in procesos:
        p.join()

    total = time.time() - inicio
    print(f"Tiempo total con procesos: {total:.2f}s")
    return total

if __name__ == "__main__":
    print("Simulacion de 3 consultas a base de datos remota")
    print("Tiempo de cada consulta: 1-5 segundos (aleatorio)")

    # Hilos
    t_hilos = ejecutar_con_hilos()

    # Asyncio
    t_async = asyncio.run(ejecutar_con_async())

    # Procesos
    t_procesos = ejecutar_con_procesos()

    # Resumen
    print("\n=== RESUMEN ===")
    print(f"Hilos:    {t_hilos:.2f}s")
    print(f"Asyncio:  {t_async:.2f}s")
    print(f"Procesos: {t_procesos:.2f}s")
