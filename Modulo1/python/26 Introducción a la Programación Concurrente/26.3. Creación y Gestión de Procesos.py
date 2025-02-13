# 26.3.1. Creación de procesos con multiprocessing
# Uso de multiprocessing.Process para crear procesos
import multiprocessing

def tarea_proceso():
    print(f"Tarea en proceso {multiprocessing.current_process().name}")

procesos = []
for i in range(5):
    proceso = multiprocessing.Process(target=tarea_proceso)
    procesos.append(proceso)
    proceso.start()

for proceso in procesos:
    proceso.join()

# 26.3.2. Sincronización de procesos
# Uso de Lock, RLock, Semaphore para sincronizar procesos
lock = multiprocessing.Lock()

def tarea_sincronizada():
    with lock:
        print(f"Tarea sincronizada en proceso {multiprocessing.current_process().name}")

procesos = []
for i in range(5):
    proceso = multiprocessing.Process(target=tarea_sincronizada)
    procesos.append(proceso)
    proceso.start()

for proceso in procesos:
    proceso.join()

# 26.3.3. Comunicación entre procesos
# Uso de Queue, Pipe para comunicación entre procesos
q = multiprocessing.Queue()

def productor():
    for i in range(5):
        q.put(i)
        print(f"Productor: {i}")

def consumidor():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumidor: {item}")

productor_proceso = multiprocessing.Process(target=productor)
consumidor_proceso = multiprocessing.Process(target=consumidor)

productor_proceso.start()
consumidor_proceso.start()

productor_proceso.join()
q.put(None)
consumidor_proceso.join()

# 26.3.4. Manejo de excepciones en procesos
# Uso de try, except para manejar excepciones en procesos
def tarea_con_excepcion():
    try:
        raise Exception("Error en proceso")
    except Exception as e:
        print(f"Excepción capturada: {e}")

proceso = multiprocessing.Process(target=tarea_con_excepcion)
proceso.start()
proceso.join()