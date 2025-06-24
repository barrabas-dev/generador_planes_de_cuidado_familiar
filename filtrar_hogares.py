from typing import Dict, Any

def filtrar_hogares_seleccionados(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Filtra los hogares que tienen al menos un integrante con 'SELECCIONADO' en True.

    :param data: Diccionario con estructura de hogares e integrantes.
    :return: Diccionario con solo los hogares que cumplen la condición.
    """
    hogares_filtrados = {}

    for hogar_id, info_hogar in data.items():
        integrantes = info_hogar.get("integrantes", [])
        # Buscar si hay al menos un integrante seleccionado
        if any(integrante.get("SELECCIONADO", False) for integrante in integrantes):
            hogares_filtrados[hogar_id] = info_hogar

    return hogares_filtrados