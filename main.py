print("hola mundo")
from dataclasses import asdict
from encuesta_familiar_reader import leer_encuesta_familiar
from encuesta_reader import leer_encuesta

import json


# main.py

ruta_archivo_0 = "assets/encuesta.xlsx"
ruta_archivo_1 = "assets/encuesta_familiar.xlsx"

nucleo_seleccionados = leer_encuesta_familiar(ruta_archivo_1)

# Conversión a un formato completamente serializable
serializable_dict_nucleos = {clave: asdict(valor) for clave, valor in nucleo_seleccionados.items()}

# (Opcional) Imprimir el resultado
#print(json.dumps(serializable_dict, indent=2, ensure_ascii=False))
    
# esta parte se encarga de obtener un diccionario con los datos de los encuestados organizados por nuleos familiares.

nucleos = leer_encuesta(ruta_archivo_0) 

# Convertimos a un formato serializable (los dataclass se transforman en dicts primero)
serializable_dict_nucleos_datos = {
    hogar_id: {
        "hogar_id": nucleo.hogar_id,
        "integrantes": [p.datos for p in nucleo.integrantes]
    }
    for hogar_id, nucleo in nucleos.items()
}

# Guardar o imprimir como JSON bonito
#rint(json.dumps(serializable_dict_nucleos, indent=4, ensure_ascii=False))

# -----------------------------------------------------------------------------------------------------------
from excel_exporter_2 import crear_planes_cuidado_familiares
plantilla = "assets/plantillas/formato_plan_integral_familiar.xlsx"
carpeta_salida = "planes_de_cuidado_familiares"

crear_planes_cuidado_familiares(serializable_dict_nucleos_datos, serializable_dict_nucleos, plantilla, carpeta_salida)



'''
# -----------------------------------------------------------------------------------------------------------
from excel_exporter_1 import crear_planes_cuidado
plantilla = "assets/plantillas/plantilla_base.xlsx"
carpeta_salida = "planes_de_cuidado"

crear_planes_cuidado(serializable_dict, plantilla, carpeta_salida)

'''
