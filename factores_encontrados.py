from typing import Optional
from db_restuestas import acuerdos_apgar

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
    
#-------------------------test-------------------------------------------

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
if __name__ == "__main__":
    resultado = "12 A 10"
    texto_completo = obtener_acuerdo_completo_apgar(resultado)

    if texto_completo:
        print(texto_completo)
    else:
        print("Resultado APGAR no válido.")
'''