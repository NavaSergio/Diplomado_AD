# 25.1.1. Introducción a la programación asíncrona
# Definición y características de la programación asíncrona: Permite ejecutar múltiples operaciones sin bloquear el hilo principal.
# Ventajas de la programación asíncrona: Mejora el rendimiento y la capacidad de respuesta en aplicaciones I/O-bound.

# 25.1.2. Diferencias entre programación síncrona y asíncrona
# Concepto de programación síncrona: Las operaciones se ejecutan una tras otra.
# Diferencias y ventajas de la programación asíncrona: Permite ejecutar múltiples operaciones simultáneamente.

# 25.1.3. Uso de async y await
# Introducción a las palabras clave async y await
# Ejemplos básicos de uso de async y await
import asyncio

async def decir_hola():
    print("Hola")
    await asyncio.sleep(1)
    print("Mundo")

asyncio.run(decir_hola())