from typing import Optional
from db_restuestas import acuerdos_apgar, factores_dict

#-----------------------------------------------------------------------------------------------------
def obtener_acuerdo_completo_apgar(resultado: str) -> Optional[str]:
    """
    Retorna un string único estructurado con el título y el texto del acuerdo según el resultado APGAR.

    Parámetros:
        resultado (str): Resultado del APGAR como string ('17-20', '16-13', '12-10', '9').

    Retorna:
        str: Título seguido del contenido del acuerdo, separados por doble salto de línea.
        None: Si el resultado no es válido.
    """


    acuerdo_info = acuerdos_apgar.get(resultado)

    if acuerdo_info:
        titulo = acuerdo_info["titulo"]
        acuerdo = acuerdo_info["acuerdo"]
        return f"{titulo}:\n\n{acuerdo}"
    else:
        return None
    
#------------------------------------------------------------------------------------------------

from typing import Optional
from db_restuestas import resultados_apgar

def obtener_resultado_completo_apgar(resultado: str) -> Optional[str]:
    """
    Retorna un string estructurado con el título y el texto descriptivo del resultado APGAR.

    Parámetros:
        resultado (str): Resultado del APGAR como string ('17 A 20', '16 A 13', '12 A 10', '9 O MENOS').

    Retorna:
        str: Título seguido del contenido descriptivo, separados por doble salto de línea.
        None: Si el resultado no es válido.
    """
    resultado_info = resultados_apgar.get(resultado)

    if resultado_info:
        titulo = resultado_info["titulo"]
        acuerdo = resultado_info["acuerdo"]
        return f"{titulo}:\n\n{acuerdo}"
    else:
        return None



#----------------------------------------------------------------------

from typing import Tuple
 # Diccionario base con las fortalezas según rango de calificación APGAR
from db_restuestas import fortalezas_apgar

def obtener_fortalezas_apgar(calificacion: str) -> Tuple[str, str, str, str]:
    """
    Retorna una tupla con las descripciones de fortalezas familiares según la calificación APGAR.

    Parámetros:
        calificacion (str): Calificación APGAR en formato string. Ejemplos válidos:
                            "17 A 20", "16 A 13", "12 A 10", "9"

    Retorna:
        tuple[str, str, str, str]: Tupla con las cuatro fortalezas asociadas a la calificación.

    Lanza:
        ValueError: Si la calificación ingresada no es reconocida.
    """

    # Normalizar el string recibido para que coincida con las claves del diccionario
    calificacion_normalizada = (
        calificacion.strip()       # Elimina espacios iniciales/finales
                  .replace(" ", "") # Quita espacios intermedios
                  .replace("A", "-") # Reemplaza 'A' por guion para coincidir con el formato del diccionario
    )

    try:
        fortalezas = fortalezas_apgar[calificacion_normalizada]
    except KeyError:
        raise ValueError(
            f"Calificación APGAR '{calificacion}' no reconocida. "
            "Use valores como '17 A 20', '16 A 13', '12 A 10' o '9'."
        )

    try:
        # Retorna las fortalezas en orden
        return (
            fortalezas["FORTALEZA 1"],
            fortalezas["FORTALEZA 2"],
            fortalezas["FORTALEZA 3"],
            fortalezas["FORTALEZA 4"],
        )
    except KeyError as e:
        # Esto captura errores si faltan claves internas inesperadamente
        raise ValueError(f"Datos incompletos para la calificación '{calificacion_normalizada}': falta {e}")
    

#------------------funcion para agregar textos en cuidado de salud familiar-------------------------------------------------------------

from typing import Dict, Tuple, List

def generar_textos_factores(
    datos_nucleo: Dict[str, Dict],
    factores_dict: Dict[str, Dict[str, str]]
) -> Tuple[str, str, str, str]:
    """
    Genera una tupla con los textos correspondientes a hallazgo, compromiso, logro trazador y logro intermedio,
    basados en los factores marcados como `True` o `False` en los datos del núcleo familiar.

    Si ninguno de los factores clave está marcado como `True`, se retorna un texto general sin hallazgos y los demás campos vacíos.

    :param datos_nucleo: Diccionario que contiene los datos del núcleo familiar, incluyendo factores con valores booleanos.
    :param factores_dict: Diccionario maestro con los textos asociados a cada factor.
    :return: Tupla con 4 cadenas de texto (listas para celdas de Excel): hallazgo_identificado, compromiso_concertado,
             logro_trazador, logro_intermedio.
    """

    # Lista de factores de interés (se ignoran los demás)
    factores_clave = [
        "COMUNICACION NO ASERTIVA, USO INADECUADO DE PANTALLAS LO CUAL DIFICULTA LAS INTERACCIONES FAMILIARES",
        "INASISTENCIA A SERVICIOS DE SALUD DENTRO DEL MARCO DE LOS SERVICIOS DE LA RUTA DE PROMOCION Y MANTENIMIENTO DE LA SALUD",
        "RIESGO DE AISLAMIENTO SOCIAL Y DETERIORO EN SU SALUD FÍSICA Y MENTAL DEBIDO A LA FALTA DE APOYO FAMILIAR CONSTANTE Y HÁBITOS IRREGULARES DE AUTOCUIDADO",
        "ENVEJECIMIENTO, ENFERMEDADES CRÓNICAS Y CAMBIOS EMOCIONALES",
        "RIESGO DE MAL NUTRICIÓN"
    ]

    # Inicializamos listas para acumular los textos correspondientes
    hallazgos = []
    compromisos = []
    trazadores = []
    intermedios = []

    # Extraemos los factores del núcleo (ej: datos_nucleo['H0001']['factores'])
    factores_reportados = datos_nucleo.get('factores', {})


    # Recorremos los factores de interés
    for factor in factores_clave:
        if factores_reportados.get(factor) is True:
            info = factores_dict.get(factor, {})
            # Se agregan los textos con saltos de línea para formato en celdas Excel
            hallazgos.append(info.get("hallazgo_identificado", ""))
            compromisos.append(info.get("compromiso_concertado", ""))
            trazadores.append(info.get("logro_trazador", ""))
            intermedios.append(info.get("logro_intermedio", ""))

    # Si no se encontró ningún factor con True, usamos plantilla sin hallazgos
    if not hallazgos:
        texto_sin_hallazgos = factores_dict.get("plantilla_sin_hallazgos", "")
        return (texto_sin_hallazgos, "", "", "")
    
    # Se concatenan los textos con saltos de línea para mayor claridad
    return (
        "\n\n".join(hallazgos),
        "\n\n".join(compromisos),
        "\n\n".join(trazadores),
        "\n\n".join(intermedios),
    )

#-----------------------------------------------------------------------
from typing import List, Dict, Tuple, Any
from db_restuestas import datos_por_ciclo_vida


def generar_tuplas_integrantes(
    integrantes: List[Dict[str, Any]],
    datos_por_ciclo_vida: Dict[str, Dict[str, str]]
) -> List[Tuple[str, int, str, str, str, str]]:
    """
    Genera una lista de tuplas con información personalizada por integrante,
    según su edad y el ciclo de vida correspondiente.

    Cada tupla contiene:
    (nombre, edad, hallazgo_con_ciclo, compromiso, logro_trazador, logro_intermedio)
    """

    def normalizar_edad(edad) -> int:
        try:
            return int(edad)
        except (ValueError, TypeError):
            return -1  # Edad inválida

    def determinar_ciclo(edad: int) -> str:
        if 0 <= edad <= 5:
            return "0 a 5"
        elif 6 <= edad <= 11:
            return "6 a 11"
        elif 12 <= edad <= 17:
            return "12 a 17"
        elif 18 <= edad <= 28:
            return "18 a 28"
        elif 29 <= edad <= 59:
            return "29 a 59"
        elif edad >= 60:
            return ">60"
        else:
            return "desconocido"

    resultado: List[Tuple[str, int, str, str, str, str]] = []

    for persona in integrantes:
        nombre = persona.get("NOMBRE", "Sin nombre")
        edad_str = persona.get("EDAD", "")
        edad = normalizar_edad(edad_str)
        ciclo_clave = determinar_ciclo(edad)

        if ciclo_clave in datos_por_ciclo_vida:
            datos_ciclo = datos_por_ciclo_vida[ciclo_clave]
            ciclo = datos_ciclo["ciclo"]
            hallazgo = f"{ciclo}: {datos_ciclo['hallazgo']}"
            compromiso = datos_ciclo["compromiso"]
            logro_trazador = datos_ciclo["logro_trazador"]
            logro_intermedio = datos_ciclo["logro_intermedio"]

            resultado.append((nombre, edad, hallazgo, compromiso, logro_trazador, logro_intermedio))
        else:
            print(f"⚠️ Edad inválida o fuera de rango para {nombre}: {edad_str}")

    return resultado

#----------funcion para generar textos de sobrecarga del cuidador------------------------------

from typing import Dict, Tuple
from db_restuestas import sobrecarga_cuidador

def generar_texto_sobrecarga_unico(datos_nucleo: Dict[str, Dict]) -> Tuple[str, str, str, str]:
    """
    Genera una tupla de textos (hallazgo, compromiso, logro trazador, logro intermedio)
    basada únicamente en el valor booleano del factor 'SOBRECARGA DE CUIDADOR'.

    :param datos_nucleo: Diccionario del núcleo familiar con la clave 'factores' que incluye el factor de sobrecarga.
    :return: Tupla de textos (hallazgo, compromiso, logro trazador, logro intermedio).
    """
    # Extrae el valor booleano del factor
    factores = datos_nucleo.get("factores", {})
    valor_sobrecarga = factores.get("SOBRECARGA DE CUIDADOR")

    # Usa el diccionario correspondiente
    info = sobrecarga_cuidador.get(valor_sobrecarga)

    # Si no hay valor válido, retorna textos vacíos
    if not info:
        return ("", "", "", "")

    return (
        info["hallazgo"],
        info["compromiso"],
        info["logro_trazador"],
        info["logro_intermedio"]
    )

#----funcion para generar textos sobre actividades ludicas y deportivas

from typing import Dict, Tuple

def generar_textos_cuidado_entorno(
    datos_nucleo: Dict[str, Dict],
    diccionario: Dict[bool, Dict[str, Dict[str, str]]]
) -> Tuple[str, str, str, str]:
    """
    Genera una tupla con los textos de hallazgo, compromiso, logro trazador e intermedio
    para actividades comunitarias, según el valor True/False de cada actividad.

    Siempre incluye tanto actividades deportivas como lúdicas y culturales, usando los textos
    correspondientes al valor booleano en 'datos_nucleo["factores"]'.
    """

    actividades = [
        "ACTIVIDADES DEPORTIVAS COMUNITARIAS",
        "ACTIVIDADES LÚDICAS Y CULTURALES COMUNITARIAS"
    ]

    hallazgos = []
    compromisos = []
    trazadores = []
    intermedios = []

    factores = datos_nucleo.get("factores", {})

    for actividad in actividades:
        valor = factores.get(actividad, False)
        textos = diccionario[valor].get(actividad, {})

        hallazgos.append(textos.get("hallazgo", ""))
        compromisos.append(textos.get("compromiso", ""))
        trazadores.append(textos.get("logro_trazador", ""))
        intermedios.append(textos.get("logro_intermedio", ""))

    return (
        "\n\n".join(hallazgos),
        "\n\n".join(compromisos),
        "\n\n".join(trazadores),
        "\n\n".join(intermedios),
    )


#---Funcion para red de apoyo unico-------------------------
from typing import Dict, Tuple
from db_restuestas import red_apoyo_comunitario

def generar_texto_red_apoyo_unico(datos_nucleo: Dict[str, Dict]) -> Tuple[str, str, str, str]:
    """
    Genera una tupla de textos (hallazgo, compromiso, logro trazador, logro intermedio)
    basada únicamente en el valor booleano del factor 'RED DE APOYO COMUNITARIO'.

    :param datos_nucleo: Diccionario del núcleo familiar con la clave 'factores' que incluye el factor de red de apoyo.
    :return: Tupla de textos (hallazgo, compromiso, logro trazador, logro intermedio).
    """
    # Extrae el valor booleano del factor
    factores = datos_nucleo.get("factores", {})
    valor_red_apoyo = factores.get("RED DE APOYO COMUNITARIO")

    # Usa el diccionario correspondiente
    info = red_apoyo_comunitario.get(valor_red_apoyo)

    # Si no hay valor válido, retorna textos vacíos
    if not info:
        return ("", "", "", "")

    return (
        info["hallazgo"],
        info["compromiso"],
        info["logro_trazador"],
        info["logro_intermedio"]
    )


#-------------------------test-------------------------------------
def main():
    try:
        datos_nucleo = {
            'factores': {
                "RED DE APOYO COMUNITARIO": True,
                }
        }

        # Usando el diccionario DICT_CUIDADO_ENTORNO definido antes
        hallazgo, compromiso, trazador, intermedio = generar_texto_red_apoyo_unico(datos_nucleo)

        print(hallazgo)
        print(compromiso)
        print(trazador)
        print(intermedio)

    
    except ValueError as e:
        # Manejo de errores: entrada inválida o datos incompletos
        print(f"Error: {e}")


if __name__ == "__main__":
    main()




'''
def main():
    
    try:
        nucleo_ejemplo = {
            "factores": {
                 "SOBRECARGA DE CUIDADOR": True
                }
            }

        resultado = generar_texto_sobrecarga_unico(nucleo_ejemplo)
        print(resultado)

    
    except ValueError as e:
        # Manejo de errores: entrada inválida o datos incompletos
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

'''

'''
def main():
    
    try:
        integrantes = [
            {
                "HOGAR": "H0124",
                "NOMBRE": "Ana victoria daza gelvez",
                "TIPO DE ID": "C.C",
                "NUMERO DE IDENTIFICACIÓN": "27877132",
                "GENERO": "femenino",
                "EDAD": "73",
                "EPS": "COOSALUD",
                "REGIMEN": "SUBSIDIADO",
                "FECHA DE NACIMIENTO": "1951-11-29 00:00:00",
                "ESTADO CIVIL": "soltera",
                "ESCOLARIDAD": "",
                "OCUPACION": "",
               
            },
            {
                "HOGAR": "H0124",
                "NOMBRE": "Gladys  mariela rozo gafaro",
                "TIPO DE ID": "C.C",
                "NUMERO DE IDENTIFICACIÓN": "27737835",
                "GENERO": "femenino",
                "EDAD": "54",
                "EPS": "COOSALUD",
                "REGIMEN": "SUBSIDIADO",
                "FECHA DE NACIMIENTO": "1970-12-07 00:00:00",
                "ESTADO CIVIL": "soltera",
                "ESCOLARIDAD": "",
                "OCUPACION": "",
            
            }
        ]
    
        tuplas = generar_tuplas_integrantes(integrantes, datos_por_ciclo_vida)

        for t in tuplas:
            print(t)
       
    except ValueError as e:
        # Manejo de errores: entrada inválida o datos incompletos
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


'''

#----------------------------------------------
'''
def main():
    
    try:
        # Calificación APGAR ingresada por algún sistema externo, usuario o archivo
        datos = {
            
                'fecha_visita': (15, 6, 2025),
                'resultado_apgar': '17 A 20',
                'factores': {
                    'COMUNICACION NO ASERTIVA, USO INADECUADO DE PANTALLAS LO CUAL DIFICULTA LAS INTERACCIONES FAMILIARES': True,
                    'INASISTENCIA A SERVICIOS DE SALUD DENTRO DEL MARCO DE LOS SERVICIOS DE LA RUTA DE PROMOCION Y MANTENIMIENTO DE LA SALUD': False,
                    'RIESGO DE AISLAMIENTO SOCIAL Y DETERIORO EN SU SALUD FÍSICA Y MENTAL DEBIDO A LA FALTA DE APOYO FAMILIAR CONSTANTE Y HÁBITOS IRREGULARES DE AUTOCUIDADO': False,
                    'ENVEJECIMIENTO, ENFERMEDADES CRÓNICAS Y CAMBIOS EMOCIONALES': True,
                    'RIESGO DE MAL NUTRICIÓN': False,
                    'ACTIVIDADES DEPORTIVAS COMUNITARIAS': False,
                    'ACTIVIDADES LÚDICAS Y CULTURALES COMUNITARIAS': False,
                    'RED DE APOYO COMUNITARIO': False,
                    'SOBRECARGA DE CUIDADOR': False
                        }
            
        }

        tupla_textos = generar_textos_factores(datos, factores_dict)
       

        def imprimir_textos_celda(textos: Tuple[str, str, str, str]) -> None:
            """
            Imprime los cuatro textos contenidos en una tupla, uno por uno con su respectiva etiqueta.
            
            :param textos: Tupla con los textos a imprimir (hallazgo, compromiso, logro trazador, logro intermedio).
            """
            etiquetas = [
                "🟡 HALLAZGO IDENTIFICADO:",
                "🟠 COMPROMISO CONCERTADO:",
                "🟢 LOGRO TRAZADOR:",
                "🔵 LOGRO INTERMEDIO:"
            ]

            for etiqueta, contenido in zip(etiquetas, textos):
                print(etiqueta)
                print(contenido if contenido else "[Sin contenido]")
                print("-" * 80)  # Separador visual


        imprimir_textos_celda(tupla_textos)
       
    except ValueError as e:
        # Manejo de errores: entrada inválida o datos incompletos
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

'''
#-----------------------------------------------------------------------------------------
'''   
def main():
    try:
        # Calificación APGAR ingresada por algún sistema externo, usuario o archivo
        calificacion = "16 A 13"

        # Obtener fortalezas asociadas a la calificación
        fortalezas = obtener_fortalezas_apgar(calificacion)

        # Imprimir resultados
        print("Fortalezas identificadas:")
        for i, fortaleza in enumerate(fortalezas, 1):
            print(f"1: {fortaleza}")

    except ValueError as e:
        # Manejo de errores: entrada inválida o datos incompletos
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
''' 

#---------------------------------------------------------------------


'''
if __name__ == "__main__":
    resultado = "12 A 10"
    texto_completo = obtener_acuerdo_completo_apgar(resultado)

    if texto_completo:
        print(texto_completo)
    else:
        print("Resultado APGAR no válido.")
'''