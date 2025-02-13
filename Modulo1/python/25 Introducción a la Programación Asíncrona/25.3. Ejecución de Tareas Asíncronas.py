# 25.3.1. Creación y ejecución de tareas asíncronas
# Uso de asyncio.create_task() para crear y ejecutar tareas asíncronas
async def tarea_asincrona():
    print("Inicio de la tarea asíncrona")
    await asyncio.sleep(1)
    print("Fin de la tarea asíncrona")

async def main():
    tarea = asyncio.create_task(tarea_asincrona())
    await tarea

asyncio.run(main())

# 25.3.2. Manejo de múltiples tareas asíncronas
# Uso de asyncio.gather() para manejar múltiples tareas asíncronas
async def tarea1():
    print("Tarea 1")
    await asyncio.sleep(1)
    print("Fin Tarea 1")

async def tarea2():
    print("Tarea 2")
    await asyncio.sleep(2)
    print("Fin Tarea 2")

async def main():
    await asyncio.gather(tarea1(), tarea2())

asyncio.run(main())

# 25.3.3. Cancelación de tareas asíncronas
# Uso de task.cancel() para cancelar tareas asíncronas
async def tarea_cancelable():
    try:
        while True:
            print("Tarea en ejecución")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Tarea cancelada")

async def main():
    tarea = asyncio.create_task(tarea_cancelable())
    await asyncio.sleep(3)
    tarea.cancel()

asyncio.run(main())