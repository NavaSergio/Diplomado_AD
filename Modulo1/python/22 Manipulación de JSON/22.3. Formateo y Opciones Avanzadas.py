# 22.3.1. Formateo de JSON
# Uso de parámetros como indent, separators, sort_keys en json.dumps()
datos = {"nombre": "María", "edad": 28, "ciudad": "Bilbao"}
json_string = json.dumps(datos, indent=4, separators=(',', ': '), sort_keys=True)
print(f"JSON formateado:\n{json_string}")

# 22.3.2. Manejo de tipos de datos no estándar
# Uso de default en json.dumps() para manejar tipos de datos no estándar
def serializar_fecha(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"Tipo no serializable: {type(obj)}")

from datetime import datetime
datos = {"nombre": "Carlos", "fecha": datetime.now()}
json_string = json.dumps(datos, default=serializar_fecha)
print(f"JSON con fecha serializada: {json_string}")

# 22.3.3. Uso de json.JSONEncoder y json.JSONDecoder
# Creación de encoders y decoders personalizados
class FechaEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

datos = {"nombre": "Elena", "fecha": datetime.now()}
json_string = json.dumps(datos, cls=FechaEncoder)
print(f"JSON con fecha serializada usando JSONEncoder: {json_string}")