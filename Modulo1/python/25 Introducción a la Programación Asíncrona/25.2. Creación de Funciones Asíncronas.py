# 25.2.1. Definición de funciones asíncronas
# Sintaxis básica para definir funciones asíncronas con async def
async def funcion_asincrona():
    print("Inicio de la función asíncrona")
    await asyncio.sleep(1)
    print("Fin de la función asíncrona")

# 25.2.2. Uso de await en funciones asíncronas
# Uso de await para esperar la finalización de operaciones asíncronas
async def otra_funcion_asincrona():
    print("Inicio de otra función asíncrona")
    await asyncio.sleep(2)
    print("Fin de otra función asíncrona")

# 25.2.3. Uso de asyncio para manejar eventos
# Introducción al módulo asyncio
# Ejemplos de uso de asyncio para manejar eventos asíncronos
async def main():
    await asyncio.gather(funcion_asincrona(), otra_funcion_asincrona())

asyncio.run(main())