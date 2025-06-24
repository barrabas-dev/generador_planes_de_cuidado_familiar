print("hola mundo")
# main.py

from encuesta_reader import leer_encuesta

# esta parte se encarga de obtener un diccionario con los datos de los encuestados organizados por nuleos familiares.
ruta_archivo = "assets/encuesta.xlsx"
nucleos = leer_encuesta(ruta_archivo) 

import json

# Convertimos a un formato serializable (los dataclass se transforman en dicts primero)
serializable_dict = {
    hogar_id: {
        "hogar_id": nucleo.hogar_id,
        "integrantes": [p.datos for p in nucleo.integrantes]
    }
    for hogar_id, nucleo in nucleos.items()
}

# Guardar o imprimir como JSON bonito
print(json.dumps(serializable_dict, indent=4, ensure_ascii=False))

# -----------------------------------------------------------------------------------------------------------
from excel_exporter_1 import crear_planes_cuidado
plantilla = "assets/plantillas/plantilla_base.xlsx"
carpeta_salida = "planes_de_cuidado"

crear_planes_cuidado(serializable_dict, plantilla, carpeta_salida)

'''
----------------------------------------------------------------------------------------------------------------------------------------
#excel_exporter
from excel_exporter import ExcelExporter

# Inicializar el exportador con la plantilla
exporter = ExcelExporter("assets/plantillas/plantilla_base.xlsx")

# Datos que se quieren diligenciar en la hoja
datos = {
    "b3": "día",
    "c3": "mes",
    "d3": "año",
    "g2": "n de vivienda",
    "b5": "nombre de usuario",
    "g5": "n de documento",
    "b6": "ciudad y fecha de nacimiento",
    "g6": "edad",
    "b7": "dirección",
    "g7": "teléfono de contacto"
}

# Crear un nuevo archivo basado en la plantilla
ruta_generada = exporter.export("reporte_automático", datos)

print(f"Archivo generado en: {ruta_generada}")

--------------------------------------------------------------------------------------------------------------------------------------------
'''