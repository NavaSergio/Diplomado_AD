# 26.1.1. Introducción a la programación concurrente
# Definición y características de la programación concurrente: Es un paradigma que permite ejecutar múltiples tareas aparentemente simultáneamente.
# Ventajas de la programación concurrente: Mejora el rendimiento en tareas I/O-bound y CPU-bound.

# 26.1.2. Diferencias entre concurrencia y paralelismo
# Concepto de concurrencia: Múltiples tareas en progreso al mismo tiempo.
# Concepto de paralelismo: Múltiples tareas ejecutándose simultáneamente en múltiples núcleos de CPU.
# Diferencias y similitudes entre concurrencia y paralelismo: Ambos mejoran el rendimiento, pero la concurrencia es más sobre la gestión de tareas.

# 26.1.3. Uso de threading y multiprocessing
# Introducción a los módulos threading y multiprocessing
# Ejemplos básicos de uso de threading y multiprocessing
import threading
import multiprocessing

def tarea_threading():
    print(f"Tarea en hilo {threading.current_thread().name}")

def tarea_multiprocessing():
    print(f"Tarea en proceso {multiprocessing.current_process().name}")

# Uso de threading
thread = threading.Thread(target=tarea_threading)
thread.start()
thread.join()

# Uso de multiprocessing
process = multiprocessing.Process(target=tarea_multiprocessing)
process.start()
process.join()