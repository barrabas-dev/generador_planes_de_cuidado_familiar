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


#--------normalizador----------------------------------------------------------------------------------------------------

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

#----estas funciones se encargan de llenar la celdas desde aspectos relevantes hasta las areas de funcionamiento

def llenar_area_en_hoja(hoja, persona, celda, diccionario_area, factor_altura=18):
    """
    Llena una celda con una descripción basada en la etapa del curso de vida.

    :param hoja: hoja activa de openpyxl
    :param persona: dict con datos de la persona
    :param celda: celda donde escribir el texto
    :param diccionario_area: diccionario con textos por etapa de vida
    :param factor_altura: altura base multiplicada por el número de líneas estimadas
    """
    ruta_original = persona.get("RUTA A LA QUE PERTENECE", "")
    ruta_normalizada = normalizar_texto(ruta_original)

    texto = diccionario_area.get(ruta_normalizada)
    if texto is None:
        texto = f"No se encontró información para la ruta de vida '{ruta_original}'. Verifique los datos."

    hoja[celda] = texto
    hoja[celda].alignment = Alignment(wrap_text=True, vertical="top")

    fila = int(''.join(filter(str.isdigit, celda)))
    num_lineas = len(texto) // 90 + 1
    hoja.row_dimensions[fila].height = factor_altura * num_lineas

def llenar_desarrollo_por_etapa(hoja, persona, celda):
    desarrollo_por_etapa = {
        "primera infancia": "El paciente atraviesa un periodo clave para el desarrollo de sus habilidades motoras, cognitivas, emocionales y sociales. Es fundamental proporcionar un entorno seguro y afectivo que favorezca su crecimiento integral. La nutrición adecuada, la estimulación temprana y el fortalecimiento del vínculo familiar son esenciales. El acompañamiento en salud permite identificar necesidades y promover un desarrollo óptimo.",
        "infancia": "El paciente fortalece sus capacidades cognitivas, motoras, emocionales y sociales, consolidando habilidades que le permitirán una mayor autonomía. Es esencial promover hábitos de vida saludables, una adecuada nutrición y el desarrollo de habilidades socioemocionales. El entorno familiar y escolar debe ofrecer apoyo y estímulo constante. El seguimiento en salud facilita la detección temprana de alteraciones y favorece un desarrollo integral.",
        "adolescencia": "El paciente experimenta importantes cambios físicos, emocionales, sociales y cognitivos que marcan la transición hacia la adultez. Es fundamental promover un entorno de apoyo que fortalezca su autoestima, la toma de decisiones responsables y hábitos de vida saludables. La orientación en salud sexual y reproductiva, así como el acompañamiento emocional, son esenciales. El seguimiento integral permite prevenir riesgos y fomentar un desarrollo armónico.",
        "juventud": "El paciente consolida su identidad personal y social, y enfrenta nuevos desafíos relacionados con la autonomía, la vida laboral y las relaciones interpersonales. Es esencial promover estilos de vida saludables, el autocuidado y el bienestar emocional. La educación en salud sexual y reproductiva, así como la prevención de enfermedades crónicas y conductas de riesgo, son prioritarias. El acompañamiento integral facilita una transición saludable hacia la vida adulta plena.",
        "adultez": "El paciente busca consolidar su proyecto de vida, equilibrando las demandas personales, familiares y laborales. Es fundamental fomentar el autocuidado, la actividad física regular, una nutrición adecuada y el bienestar emocional. La prevención y el control de enfermedades crónicas cobran relevancia en esta etapa. Un acompañamiento integral en salud contribuye a mantener una buena calidad de vida y funcionalidad a lo largo de los años.",
        "vejez": "El paciente atraviesa cambios físicos, emocionales y sociales que requieren un enfoque de cuidado integral y humanizado. Es esencial promover la autonomía, la participación activa y el mantenimiento de las capacidades funcionales. La prevención de la dependencia, el manejo adecuado de enfermedades crónicas y el fortalecimiento del apoyo familiar y comunitario son prioritarios. Un acompañamiento en salud centrado en la persona contribuye a una vejez digna y con calidad de vida."
    }
    llenar_area_en_hoja(hoja, persona, celda, desarrollo_por_etapa, factor_altura=15)

def llenar_area_afectiva_en_hoja(hoja, persona, celda):
# Diccionario con las descripciones afectivas por etapa de vida
    area_afectiva = {
        "primera infancia": "Los niños pequeños necesitan vínculos seguros y afectuosos para su desarrollo.En contextos urbanos, estos lazos dependen del tiempo y calidad de atención recibida. Factores como el estrés y las largas jornadas laborales pueden afectarlos.",
        "infancia": "En esta etapa, los niños necesitan vínculos estables y afectuosos para su seguridad emocional.Las redes de apoyo urbanas pueden fortalecer estos lazos. Pero el estrés, la ausencia de cuidadores y el ritmo acelerado pueden afectarlos.",
        "adolescencia": "En la adolescencia, los vínculos afectivos son clave para el desarrollo emocional.Los adolescentes urbanos pueden crear lazos significativos con pares y adultos referentes. Pero la ausencia de cuidadores y conflictos familiares pueden generar soledad o inestabilidad.",
        "juventud": "Los jóvenes buscan vínculos afectivos profundos y estables con familia, pareja y amigos.Aunque el entorno urbano facilita el contacto social, también puede generar estrés y aislamiento. El apoyo emocional y redes sólidas son esenciales para su bienestar.",
        "adultez": "Los adultos buscan vínculos afectivos estables con pareja, familia o amigos. El entorno urbano puede afectar estos lazos por el estrés y la falta de tiempo. Aun así, mantenerlos es clave para su bienestar y equilibrio emocional.",
        "vejez": "En la vejez, los vínculos familiares y amistosos son esenciales para el bienestar emocional. Estas relaciones brindan apoyo y compañía ante pérdidas o cambios. El acompañamiento afectivo y la inclusión social fortalecen su calidad de vida."
    }
    llenar_area_en_hoja(hoja, persona, celda, area_afectiva)

def llenar_area_personal_en_hoja(hoja, persona, celda):
 # Diccionario con las descripciones personales por etapa de vida
    area_personal = {
        "primera infancia": "El desarrollo de niños y niñas en zonas urbanas se ve influenciado por un entorno acelerado y dinámicas familiares. El acceso a servicios de salud y espacios recreativos favorece su bienestar, pero factores como el poco tiempo de los cuidadores y ambientes reducidos pueden limitar su desarrollo físico y emocional.",
        "infancia": "El entorno urbano influye en el desarrollo infantil por su ritmo acelerado y dinámicas familiares. El acceso a salud y juego mejora su bienestar físico y emocional. Sin embargo, la falta de tiempo de los cuidadores y espacios limitados pueden afectarlo.",
        "adolescencia": "Los adolescentes urbanos construyen su identidad y buscan independencia. El entorno ofrece acceso a salud, cultura y deporte, favoreciendo su desarrollo. Sin embargo, enfrentan presión social, riesgos psicosociales y falta de espacios seguros.",
        "juventud": "Los jóvenes urbanos afirman su identidad, definen metas y consolidan su autonomía. El entorno les brinda acceso a salud, recreación y desarrollo personal.Pero enfrentan presiones, sobrecarga de responsabilidades y retos emocionales.",
        "adultez": "Los adultos urbanos asumen múltiples responsabilidades que impactan su bienestar. Es clave promover el autocuidado, manejo del estrés y desarrollo personal. Sin embargo, el ritmo acelerado y las demandas dificultan el equilibrio.",
        "vejez": "Las personas mayores urbanas enfrentan cambios físicos y emocionales propios de la edad. Requieren acceso a salud, recreación y apoyo para conservar su autonomía. Pero el ritmo urbano y las barreras arquitectónicas pueden afectar su bienestar."
    }
    
    llenar_area_en_hoja(hoja, persona, celda, area_personal)

def llenar_area_social_en_hoja(hoja, persona, celda):
    area_social = {
        "primera infancia": "Los infantes urbanos desarrollan habilidades sociales en jardines, parques y comunidad. Aprenden a compartir, comunicarse y relacionarse con otros. Sin embargo, el ruido y ritmo urbano pueden limitar el juego libre y la interacción tranquila.",
        "infancia": "En esta etapa, los niños amplían sus vínculos sociales fuera del hogar. El entorno urbano brinda espacios para fortalecer la convivencia y habilidades sociales. Sin embargo, la rapidez y el individualismo urbano pueden limitar relaciones y juego seguro.",
        "adolescencia": "En la adolescencia, las relaciones con pares son fundamentales para el desarrollo. El entorno urbano ofrece diversos espacios para interactuar y fortalecer lo social. No obstante, también puede haber conflictos, discriminación o vínculos poco saludables.",
        "juventud": "En la juventud, las relaciones sociales son clave y se desarrollan en diversos espacios urbanos. Estas interacciones fortalecen la comunicación y el sentido de pertenencia. Sin embargo, pueden surgir exclusión, soledad o relaciones superficiales por la vida acelerada.",
        "adultez": "Los adultos urbanos cuentan con redes sociales formales e informales que apoyan su bienestar. Estas incluyen familia, amistades, trabajo y comunidad. Sin embargo, el ritmo de vida y las obligaciones pueden limitar la calidad de estas relaciones.",
        "vejez": "Las personas mayores urbanas conservan redes de apoyo con familia, amigos y comunidad. Factores como pérdidas, movilidad reducida o aislamiento afectan sus relaciones. Es clave promover espacios de encuentro para prevenir la soledad."
    }
    llenar_area_en_hoja(hoja, persona, celda, area_social)

def llenar_area_educativa_ocupacional_en_hoja(hoja, persona, celda):
    # Diccionario con las descripciones educativa_ocupacional por etapa de vida
    area_educativa_ocupacional = {
        "primera infancia": "La educación temprana es clave para el desarrollo infantil en zonas urbanas. El acceso a centros infantiles y programas educativos favorece el aprendizaje. Sin embargo, pueden existir limitaciones como hacinamiento o falta de atención personalizada.",
        "infancia": "Los niños en edad escolar acceden a instituciones y recursos educativos en zonas urbanas. Bibliotecas y talleres fortalecen su aprendizaje y desarrollo integral. Sin embargo, la presión académica y la falta de atención personalizada pueden afectarlos.",
        "adolescencia": "La adolescencia urbana brinda acceso a educación, formación técnica y actividades extracurriculares. Muchos jóvenes exploran vocaciones o empleos informales desde esta etapa. Sin embargo, enfrentan deserción, presión académica y falta de orientación o apoyo económico.",
        "juventud": "Los jóvenes urbanos acceden a formación superior, empleo y oportunidades de emprendimiento. Esto les permite explorar distintos caminos profesionales. Sin embargo, enfrentan deserción, desempleo, informalidad y presión que impacta su bienestar.",
        "adultez": "En la adultez urbana se consolida la vida laboral y profesional. Existen oportunidades de formación, empleo y emprendimiento. Pero también surgen desafíos como la inseguridad laboral y el difícil equilibrio vida-trabajo.",
        "vejez": "En la vejez urbana, muchas personas participan en actividades educativas y comunitarias. Estas fomentan el desarrollo personal, la socialización y el sentido de pertenencia. Contribuyen al bienestar cognitivo y emocional a través del aprendizaje continuo."
    }
    llenar_area_en_hoja(hoja, persona, celda, area_educativa_ocupacional)
