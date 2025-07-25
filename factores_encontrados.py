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
    
#-------------------------test-------------------------------------------
if __name__ == "__main__":
    resultado = "12 A 10"
    texto_completo = obtener_acuerdo_completo_apgar(resultado)

    if texto_completo:
        print(texto_completo)
    else:
        print("Resultado APGAR no válido.")