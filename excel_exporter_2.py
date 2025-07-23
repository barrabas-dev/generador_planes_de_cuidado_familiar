import os
import shutil
from openpyxl import load_workbook
from datetime import datetime


def crear_planes_cuidado_familiares(dato_nucleos: dict, planes_nucleos: dict, plantilla_path: str, salida_dir: str):
    """
    Crea un archivo Excel por cada núcleo familiar incluido en 'planes_nucleos'.
    Cada archivo contiene una única hoja, basada en una plantilla, con la información de:
    - Factores del plan familiar (desde 'planes_nucleos')
    - Miembros del núcleo (desde 'dato_nucleos')

    :param dato_nucleos: Diccionario con todos los núcleos y sus integrantes.
    :param planes_nucleos: Diccionario con los núcleos seleccionados y sus factores.
    :param plantilla_path: Ruta al archivo Excel plantilla.
    :param salida_dir: Carpeta donde se guardarán los archivos generados.
    """

    if not os.path.isfile(plantilla_path):
        raise FileNotFoundError(f"Plantilla no encontrada en la ruta: {plantilla_path}")

    os.makedirs(salida_dir, exist_ok=True)

    for nucleo_id, plan_info in planes_nucleos.items():
        if nucleo_id not in dato_nucleos:
            print(f"⚠️  Núcleo {nucleo_id} no encontrado en datos de integrantes. Se omite.")
            continue

        integrantes = dato_nucleos[nucleo_id]["integrantes"]

        # Crear copia del archivo base
        salida_path = os.path.join(salida_dir, f"{nucleo_id}.xlsx")
        shutil.copy(plantilla_path, salida_path)

        wb = load_workbook(salida_path)
        hoja = wb.worksheets[0]
        hoja.title = nucleo_id

        # Extraer información del plan
        fecha_visita = plan_info.get("Fecha de la Visita", "")
        resultado_apgar = plan_info.get("Resultado del APGAR", "")
        factores = plan_info.get("Factores identificados", {})

        # Llenar información en la hoja
        hoja["B3"] = nucleo_id  # Ejemplo de celda para el ID del núcleo
        hoja["B4"] = fecha_visita
        hoja["B5"] = resultado_apgar

        wb.save(salida_path)
        print(f"✅ Plan generado para núcleo {nucleo_id}: {salida_path}")


#test-funtion


#if __name__ == "__main__":