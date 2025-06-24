import os
import shutil
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from datetime import datetime


def copiar_hoja(wb, hoja_origen, nuevo_nombre):
    """
    Crea una copia de una hoja dentro del libro con un nuevo nombre.
    """
    nueva_hoja = wb.copy_worksheet(hoja_origen)
    nueva_hoja.title = nuevo_nombre
    return nueva_hoja


def crear_planes_cuidado(dato_nucleos: dict, plantilla_path: str, salida_dir: str):
    """
    Genera archivos Excel por hogar con hojas individuales por persona seleccionada.

    :param dato_nucleos: Diccionario con hogares e integrantes.
    :param plantilla_path: Ruta al archivo plantilla Excel.
    :param salida_dir: Carpeta destino para los archivos generados.
    """

    if not os.path.isfile(plantilla_path):
        raise FileNotFoundError(f"Plantilla no encontrada: {plantilla_path}")

    os.makedirs(salida_dir, exist_ok=True)

    for hogar_id, hogar_info in dato_nucleos.items():
        seleccionados = [
            p for p in hogar_info["integrantes"] if p.get("SELECCIONADO") is True
        ]

        if not seleccionados:
            continue

        # Crear archivo base desde plantilla
        hogar_filename = f"{hogar_id}.xlsx"
        hogar_path = os.path.join(salida_dir, hogar_filename)
        shutil.copy(plantilla_path, hogar_path)

        wb = load_workbook(hogar_path)
        hoja_modelo = wb.worksheets[0]  # Primera hoja como base

        # Procesar el primer seleccionado usando la hoja original
        primera_persona = seleccionados[0]
        hoja_modelo.title = primera_persona["NUMERO DE IDENTIFICACIÓN"]

        # Rellenar datos en la hoja base
        llenar_datos_en_hoja(hoja_modelo, primera_persona, hogar_info["integrantes"])

        # Para los demás seleccionados, duplicar la hoja base
        for persona in seleccionados[1:]:
            nueva_hoja = copiar_hoja(wb, hoja_modelo, persona["NUMERO DE IDENTIFICACIÓN"])
            llenar_datos_en_hoja(nueva_hoja, persona, hogar_info["integrantes"])

        wb.save(hogar_path)

    print(f"✅ Planes generados en: {salida_dir}")


def llenar_datos_en_hoja(hoja, persona, todos_integrantes):
    """
    Llena los datos de una persona en la hoja correspondiente.
    Adaptar esta función para colocar los datos en las celdas deseadas.
    """
    hoy = datetime.today()
    hoja["B3"] = hoy.day
    hoja["C3"] = hoy.month
    hoja["D3"] = hoy.year


    hoja["G2"] = persona["HOGAR"]
    hoja["B5"] = persona["NOMBRE"]
    hoja["G5"] = persona["NUMERO DE IDENTIFICACIÓN"]
    hoja["B6"] = persona["FECHA DE NACIMIENTO"].split()[0]
    hoja["G6"] = persona["EDAD"]
    hoja["B7"] = persona["Direccion"]
    hoja["G7"] = persona["TELEFONO"]


    # --- Estructura Familiar ---
    fila_inicio = 10  # donde comienza la primera fila de datos, justo debajo de los encabezados

    for i, integrante in enumerate(todos_integrantes):
        fila = fila_inicio + i
        hoja[f"A{fila}"] = integrante["NOMBRE"]
        hoja[f"B{fila}"] = integrante["EDAD"]
        hoja[f"C{fila}"] = integrante.get("PARENTESCO", "")  # dejar en blanco si no existe
        hoja[f"D{fila}"] = integrante["ESTADO CIVIL"]
        hoja[f"E{fila}"] = integrante["ESCOLARIDAD"]
        hoja[f"F{fila}"] = integrante["OCUPACION"]
        hoja[f"G{fila}"] = integrante["CONVIVE DENTRO DE LA CASA"]
