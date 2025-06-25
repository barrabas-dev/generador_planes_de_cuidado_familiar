from openpyxl.styles import Alignment
def llenar_situaciones_en_hoja(hoja, persona, celda):
    """
    Llena una celda específica con las situaciones encontradas,
    basadas en las respuestas True de la persona en BOOLEAN_COLUMNS.
    
    :param hoja: hoja de cálculo abierta con openpyxl
    :param persona: diccionario con la información de la persona
    :param celda: celda donde se escribirá el resumen (por defecto "B25")
    """

    # Definimos los campos booleanos evaluados
    BOOLEAN_COLUMNS = {
        "CITOLOGÍA- ADN VPH",
        "MAMOGRAFIA - ECM",
        "TAMIZAJE CA DE COLON",
        "TAMIZAJE CA DE PROSTATA",
        "DESPARASITACION ANTIHELMITICA",
        "PLANIFICACION FAMILIAR",
        "TAMIZAJE ANEMIA Y HEMOGLOBINA",
        "TAMIZAJE RIESGO CARDIOVASCULAR",
        "VACUNACIÓN",
        "VALORACIÓN ODONTOLOGÍA",
        "CONSULTA DE CONTROL (RIAS)",
        "TOMA DE LABORATORIOS SEGUN RIA"
    }

    # Descripciones por cada situación encontrada
    situaciones_encontradas = {
        "CITOLOGÍA- ADN VPH": "Ausencia de tamizaje cervical mediante citología",
        "MAMOGRAFIA - ECM": "Ausencia de mamografía ni autoexamen de mama",
        "TAMIZAJE CA DE COLON": "Ausencia de tamizaje para cancer de colón",
        "TAMIZAJE CA DE PROSTATA": "Ausencia de tamizaje para cancer de prostata",
        "DESPARASITACION ANTIHELMITICA": "Ausencia de desparasitacion antihelmitica",
        "PLANIFICACION FAMILIAR": "No utiliza ningún método de planificación familiar, desconocimiento de algunos métodos",
        "TAMIZAJE ANEMIA Y HEMOGLOBINA": "Ausencia de tamizaje para anemia",
        "TAMIZAJE RIESGO CARDIOVASCULAR": "Ausencia de laboratorios y exámenes para determinar el riesgo cardiovascular",
        "VACUNACIÓN": "Asquema de vacunación incompleto según RIAS",
        "VALORACIÓN ODONTOLOGÍA": "Ausencia de valoración odontológica periódica según esquema RIAS",
        "CONSULTA DE CONTROL (RIAS)": "Ausencia de consulta para valoración según curso de vida, resolución 3280",
        "TOMA DE LABORATORIOS SEGUN RIA": "Asencia de laboratorios según curso de vida, resolución 3280"
    }

    situaciones = []

    # Evaluamos las respuestas True que representan ausencia
    for campo in BOOLEAN_COLUMNS:
        if persona.get(campo) is True:
            descripcion = situaciones_encontradas.get(campo)
            if descripcion:
                situaciones.append(descripcion)

    # Construimos el string final
    #texto_final = ". ".join(situaciones) + "." if situaciones else "Sin situaciones identificadas."
    texto_final = "Presenta:\n" + "\n".join(f"- {s}" for s in situaciones) if situaciones else "Sin situaciones identificadas."


    # Escribimos el resultado en la celda especificada
    hoja[celda] = texto_final


    # Aplicar estilo de ajuste de texto (wrapText)
    hoja[celda].alignment = Alignment(wrap_text=True, vertical="top")

    # Ajustar la altura de la fila en función de la cantidad de líneas
    fila = int(''.join(filter(str.isdigit, celda)))
    num_lineas = texto_final.count("\n") + 1  # +1 por la línea "Presenta:"
    altura_aproximada = 15 * num_lineas  # puedes ajustar este factor si el texto es muy largo
    hoja.row_dimensions[fila].height = altura_aproximada


#-----------------------------------------------------------------------------------------------------------------------------------------------------
#llenar desarrollo por estapas
import unicodedata
def normalizar_texto(texto):
    """
    Elimina tildes, pasa a minúsculas y quita espacios extra.
    Ideal para comparar texto que puede tener errores de digitación.
    """
    if not isinstance(texto, str):
        return ""
    texto = texto.strip().lower()
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto


def llenar_desarrollo_por_etapa(hoja, persona, celda):
    """
    Llena una celda con el texto correspondiente al desarrollo según la etapa de vida.

    :param hoja: hoja activa (openpyxl)
    :param persona: diccionario con datos de la persona
    :param celda: celda donde escribir la descripción (por defecto "B30")
    """

    # Diccionario base con los mensajes por etapa de vida
    desarrollo_por_etapa = {
        "primera infancia": "El paciente atraviesa un periodo clave para el desarrollo de sus habilidades motoras, cognitivas, emocionales y sociales. Es fundamental proporcionar un entorno seguro y afectivo que favorezca su crecimiento integral. La nutrición adecuada, la estimulación temprana y el fortalecimiento del vínculo familiar son esenciales. El acompañamiento en salud permite identificar necesidades y promover un desarrollo óptimo.",
        "infancia": "El paciente fortalece sus capacidades cognitivas, motoras, emocionales y sociales, consolidando habilidades que le permitirán una mayor autonomía. Es esencial promover hábitos de vida saludables, una adecuada nutrición y el desarrollo de habilidades socioemocionales. El entorno familiar y escolar debe ofrecer apoyo y estímulo constante. El seguimiento en salud facilita la detección temprana de alteraciones y favorece un desarrollo integral.",
        "adolescencia": "El paciente experimenta importantes cambios físicos, emocionales, sociales y cognitivos que marcan la transición hacia la adultez. Es fundamental promover un entorno de apoyo que fortalezca su autoestima, la toma de decisiones responsables y hábitos de vida saludables. La orientación en salud sexual y reproductiva, así como el acompañamiento emocional, son esenciales. El seguimiento integral permite prevenir riesgos y fomentar un desarrollo armónico.",
        "juventud": "El paciente consolida su identidad personal y social, y enfrenta nuevos desafíos relacionados con la autonomía, la vida laboral y las relaciones interpersonales. Es esencial promover estilos de vida saludables, el autocuidado y el bienestar emocional. La educación en salud sexual y reproductiva, así como la prevención de enfermedades crónicas y conductas de riesgo, son prioritarias. El acompañamiento integral facilita una transición saludable hacia la vida adulta plena.",
        "adultez": "El paciente busca consolidar su proyecto de vida, equilibrando las demandas personales, familiares y laborales. Es fundamental fomentar el autocuidado, la actividad física regular, una nutrición adecuada y el bienestar emocional. La prevención y el control de enfermedades crónicas cobran relevancia en esta etapa. Un acompañamiento integral en salud contribuye a mantener una buena calidad de vida y funcionalidad a lo largo de los años.",
        "vejez": "El paciente atraviesa cambios físicos, emocionales y sociales que requieren un enfoque de cuidado integral y humanizado. Es esencial promover la autonomía, la participación activa y el mantenimiento de las capacidades funcionales. La prevención de la dependencia, el manejo adecuado de enfermedades crónicas y el fortalecimiento del apoyo familiar y comunitario son prioritarios. Un acompañamiento en salud centrado en la persona contribuye a una vejez digna y con calidad de vida."
    }

    # Obtener y normalizar el valor de la ruta
    ruta_original = persona.get("RUTA A LA QUE PERTENECE", "")
    ruta_normalizada = normalizar_texto(ruta_original)

    # Intentar buscar la descripción correspondiente
    descripcion = desarrollo_por_etapa.get(ruta_normalizada)

    # Si no se encuentra, dejar mensaje genérico
    if descripcion is None:
        descripcion = f"No se pudo determinar una descripción para la ruta de vida '{ruta_original}'. Verifique la información."

    # Escribir en la celda
    hoja[celda] = descripcion
    hoja[celda].alignment = Alignment(wrap_text=True, vertical="top")

    # Ajustar altura según longitud (estimación: 1 línea cada 90 caracteres)
    fila = int(''.join(filter(str.isdigit, celda)))
    num_lineas = len(descripcion) // 90 + 1
    hoja.row_dimensions[fila].height = 15 * num_lineas

