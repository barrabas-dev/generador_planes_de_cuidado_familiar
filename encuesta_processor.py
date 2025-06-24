# encuesta_processor.py

import pandas as pd
from typing import List, Dict


# Definición de clase para representar un Paciente
class Paciente:
    def __init__(self, datos: Dict[str, str]):
        # Almacena todos los datos como strings
        for campo, valor in datos.items():
            setattr(self, campo.lower().replace(" ", "_"), valor)

    def __repr__(self):
        return f"Paciente(nombre={getattr(self, 'nombre', 'N/A')}, hogar={getattr(self, 'hogar', 'N/A')})"


# Clase para representar un núcleo familiar
class NucleoFamiliar:
    def __init__(self, identificador: str):
        self.identificador = identificador  # Corresponde al valor en la columna "HOGAR"
        self.pacientes: List[Paciente] = []

    def agregar_paciente(self, paciente: Paciente):
        self.pacientes.append(paciente)

    def __repr__(self):
        return f"NucleoFamiliar(id={self.identificador}, pacientes={len(self.pacientes)})"


# Diccionario base de encabezados esperados
encuesta_dict = {
    "HOGAR": None,
    "NOMBRE": None,
    "TIPO DE ID": None,
    "NUMERO DE IDENTIFICACIÓN": None,
    "GENERO": None,
    "EDAD": None,
    "EPS": None,
    "REGIMEN": None,
    "FECHA DE NACIMIENTO": None,
    "ESTADO CIVIL": None,
    "ESCOLARIDAD": None,
    "OCUPACION": None,
    "SELECCIONADO": None,
    "CONVIVE DENTRO DE LA CASA": None,
    "RUTA A LA QUE PERTENECE": None,
    "TELEFONO": None,
    "Direccion": None,
    "CITOLOGÍA- ADN VPH": None,
    "MAMOGRAFIA - ECM": None,
    "TAMIZAJE CA DE COLON": None,
    "TAMIZAJE CA DE PROSTATA": None,
    "DESPARASITACION ANTIHELMITICA": None,
    "PLANIFICACION FAMILIAR": None,
    "TAMIZAJE ANEMIA Y HEMOGLOBINA": None,
    "TAMIZAJE RIESGO CARDIOVASCULAR": None,
    "VACUNACIÓN": None,
    "VALORACIÓN ODONTOLOGÍA": None,
    "CONSULTA DE CONTROL (RIAS)": None,
    "TOMA DE LABORATORIOS SEGUN RIA": None
}


def procesar_encuesta(path_excel: str) -> List[NucleoFamiliar]:
    """
    Procesa la encuesta desde un archivo Excel, agrupando pacientes por núcleo familiar.

    :param path_excel: Ruta al archivo .xlsx
    :return: Lista de objetos NucleoFamiliar
    """

    # Lee el archivo de Excel usando pandas
    # header=2 indica que la fila 3 de Excel (índice 2) contiene los encabezados reales
    df = pd.read_excel(path_excel, header=2, dtype=str)  # Todos los datos como strings



    # Aseguramos que solo se usen las columnas esperadas
    columnas_validas = list(encuesta_dict.keys())
    df = df[columnas_validas]  # Esto también valida el archivo contra los campos requeridos

    # Diccionario para agrupar por núcleos familiares (por ID de HOGAR)
    nucleos_dict: Dict[str, NucleoFamiliar] = {}

    # Iteramos sobre cada fila para construir pacientes y asignarlos a su núcleo
    for _, fila in df.iterrows():
        datos = fila.fillna("").to_dict()  # Convierte a dict y reemplaza NaN por string vacío
        paciente = Paciente(datos)
        hogar_id = datos["HOGAR"]

        # Creamos el núcleo familiar si no existe aún
        if hogar_id not in nucleos_dict:
            nucleos_dict[hogar_id] = NucleoFamiliar(hogar_id)

        # Agregamos el paciente al núcleo correspondiente
        nucleos_dict[hogar_id].agregar_paciente(paciente)

    # Retornamos la lista de núcleos familiares
    return list(nucleos_dict.values())
