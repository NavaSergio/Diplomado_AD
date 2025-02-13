# 26.2.1. Creación de hilos con threading
# Uso de threading.Thread para crear hilos
import threading

def tarea_hilo():
    print(f"Tarea en hilo {threading.current_thread().name}")

hilos = []
for i in range(5):
    hilo = threading.Thread(target=tarea_hilo)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

# 26.2.2. Sincronización de hilos
# Uso de Lock, RLock, Semaphore para sincronizar hilos
lock = threading.Lock()

def tarea_sincronizada():
    with lock:
        print(f"Tarea sincronizada en hilo {threading.current_thread().name}")

hilos = []
for i in range(5):
    hilo = threading.Thread(target=tarea_sincronizada)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

# 26.2.3. Comunicación entre hilos
# Uso de Queue para comunicación entre hilos
import queue

q = queue.Queue()

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

productor_hilo = threading.Thread(target=productor)
consumidor_hilo = threading.Thread(target=consumidor)

productor_hilo.start()
consumidor_hilo.start()

productor_hilo.join()
q.put(None)
consumidor_hilo.join()

# 26.2.4. Manejo de excepciones en hilos
# Uso de try, except para manejar excepciones en hilos
def tarea_con_excepcion():
    try:
        raise Exception("Error en hilo")
    except Exception as e:
        print(f"Excepción capturada: {e}")

hilo = threading.Thread(target=tarea_con_excepcion)
hilo.start()
hilo.join()