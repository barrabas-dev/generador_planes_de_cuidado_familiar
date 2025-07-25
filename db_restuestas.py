from typing import Dict
#celda e:17 seguimiento, acuerdo
# Diccionario con acuerdos según los rangos de resultado APGAR
acuerdos_apgar: Dict[str, Dict[str, str]] = {
    "17 A 20": {
        "titulo": "Fortalecimiento de capacidades y liderazgo familiar",
        "acuerdo": (
            "Se fortalecerán las capacidades del núcleo familiar para sostener prácticas saludables de "
            "alimentación, higiene, autocuidado y asistencia regular a servicios de salud. Además, se promoverá "
            "el liderazgo familiar en la comunidad, la participación en espacios colectivos y el desarrollo de "
            "redes de apoyo solidarias, reconociendo su rol activo en la promoción del bienestar integral y la "
            "consolidación de vínculos afectivos positivos."
        )
    },
    "16 A 13": {
        "titulo": "Mejoramiento de hábitos y organización familiar",
        "acuerdo": (
            "Se brindará acompañamiento para mejorar hábitos cotidianos de cuidado, promoviendo una comunicación "
            "más efectiva, la organización de rutinas familiares, el cumplimiento de controles de salud y la "
            "distribución de responsabilidades en el hogar. Estas acciones buscan fortalecer el funcionamiento "
            "familiar, reducir tensiones y fomentar un entorno protector que favorezca el desarrollo de sus "
            "integrantes."
        )
    },
    "12 A 10": {
        "titulo": "Intervención para la mejora de vínculos y convivencia",
        "acuerdo": (
            "Se implementará un plan de intervención familiar con énfasis en el fortalecimiento de vínculos, el "
            "manejo de conflictos y la reorganización de roles. Se facilitará el acceso a servicios sociales y "
            "de salud, así como la participación en espacios psicoeducativos para mejorar la convivencia, la "
            "toma de decisiones compartida y el establecimiento de normas básicas de funcionamiento."
        )
    },
    "9": {
        "titulo": "Abordaje integral y restitución de derechos",
        "acuerdo": (
            "Se gestionará un abordaje integral e intensivo que priorice la protección de los miembros más "
            "vulnerables del núcleo familiar, mediante intervenciones psicosociales, jurídicas y de salud. Se "
            "orientará a la familia hacia la reconstrucción de sus relaciones internas, el restablecimiento de "
            "condiciones mínimas de cuidado y la articulación con instituciones que garanticen la restitución "
            "de derechos y la contención emocional."
        )
    }
}


#celda -fortalezas de la familia

fortalezas_apgar: Dict[str, Dict[str, str]] = {
    "17-20": {
        "FORTALEZA 1": "Los miembros de la familia expresan libremente sus emociones, positivas y negativas. Esta comunicación emocional fortalece los vínculos afectivos y promueve la comprensión, la aceptación y la escucha activa.",
        "FORTALEZA 2": "Existe un diálogo abierto donde se valoran todas las opiniones. La familia resuelve conflictos de forma pacífica, con comprensión mutua y trabajo colaborativo ante desacuerdos cotidianos.",
        "FORTALEZA 3": "La familia se reorganiza de forma efectiva ante cambios o dificultades, tomando decisiones conjuntas y buscando apoyo externo si es necesario. Mantienen una actitud resiliente.",
        "FORTALEZA 4": "Todos los miembros se sienten respaldados y emocionalmente seguros, especialmente en momentos difíciles. El apoyo constante crea un ambiente confiable y protector."
    },
    "16-13": {
        "FORTALEZA 1": "Aunque hay disposición, existen dificultades ocasionales para expresar emociones, lo que puede generar malentendidos y limitar la conexión emocional.",
        "FORTALEZA 2": "Se intenta mantener la comunicación, pero los desacuerdos pueden generar tensiones. A veces se evita abordar los problemas directamente, lo que impide acuerdos duraderos.",
        "FORTALEZA 3": "La familia intenta reorganizarse ante situaciones adversas, aunque con dificultades para manejar el estrés. Puede haber incertidumbre que afecta el funcionamiento familiar temporalmente.",
        "FORTALEZA 4": "Hay reconocimiento del apoyo mutuo, pero no siempre es constante. Pueden surgir sentimientos de soledad o falta de contención emocional en momentos críticos."
    },
    "12-10": {
        "FORTALEZA 1": "La expresión emocional es limitada. Frecuentemente se evitan conversaciones sobre emociones, lo que debilita la empatía y la conexión afectiva.",
        "FORTALEZA 2": "La comunicación es ineficaz. Los conflictos suelen escalar y resolverse de forma poco saludable. Prevalece el silencio, la evasión o reacciones impulsivas.",
        "FORTALEZA 3": "Hay desorganización y poca coordinación frente a dificultades. Las decisiones son fragmentadas, y algunos miembros experimentan sobrecarga emocional.",
        "FORTALEZA 4": "Varios miembros no se sienten apoyados o seguros. En momentos difíciles, puede faltar contención, generando vulnerabilidad emocional, especialmente en los más sensibles."
    },
    "9": {
        "FORTALEZA 1": "Existe una profunda dificultad para compartir emociones. Esto genera aislamiento emocional, resentimientos acumulados y desconexión afectiva.",
        "FORTALEZA 2": "Los conflictos se evitan o se manejan de forma destructiva. No hay espacios seguros de diálogo y la falta de respeto y escucha deteriora la dinámica familiar.",
        "FORTALEZA 3": "La familia no logra reorganizarse ni apoyarse mutuamente ante adversidades. El afrontamiento es individual y caótico, lo que perpetúa una sensación de crisis.",
        "FORTALEZA 4": "El sentimiento de protección es muy bajo. En situaciones difíciles, los miembros se sienten desatendidos, lo que impacta su salud emocional y física."
    }
}

#--------------Diccionario de respuestas por factores----------------------------------------

factores_dict: Dict[str, Dict[str, str]] = {
    "COMUNICACION NO ASERTIVA, USO INADECUADO DE PANTALLAS LO CUAL DIFICULTA LAS INTERACCIONES FAMILIARES": {
        "hallazgo_identificado": (
            "Presencia de patrones de comunicación no asertiva e inadecuado uso de dispositivos electrónicos, "
            "que interfieren en las dinámicas familiares y afectan la calidad de las interacciones interpersonales."
        ),
        "compromiso_concertado": (
            "Promover espacios cotidianos de diálogo efectivo en el entorno familiar mediante la implementación "
            "de prácticas de comunicación asertiva y la delimitación consensuada de horarios para el uso de dispositivos electrónicos, "
            "con el fin de fortalecer los vínculos afectivos y la salud emocional del hogar."
        ),
        "logro_trazador": (
            "Implementación sostenida de rutinas familiares con al menos una hora diaria sin uso de dispositivos electrónicos, "
            "con evidencia de mejora en la convivencia familiar en un periodo de 6 meses, verificada mediante seguimiento comunitario o visitas domiciliarias."
        ),
        "logro_intermedio": (
            "Participación de al menos un miembro de la familia en una sesión educativa o actividad orientada a fortalecer "
            "la comunicación familiar y el uso saludable del tiempo, dentro de los próximos 90 días."
        ),
       
    },

    "INASISTENCIA A SERVICIOS DE SALUD DENTRO DEL MARCO DE LOS SERVICIOS DE LA RUTA DE PROMOCION Y MANTENIMIENTO DE LA SALUD": {
        "hallazgo_identificado": (
            "Baja adherencia a los servicios integrales de atención en salud dentro de la Ruta de Promoción y Mantenimiento de la Salud, "
            "lo cual limita la detección temprana, la intervención oportuna y la continuidad del cuidado."
        ),
        "compromiso_concertado": (
            "Asegurar la vinculación efectiva de todos los miembros del grupo familiar a actividades preventivas y de control de salud, "
            "conforme al curso de vida, mediante la programación, asistencia y seguimiento de atenciones estipuladas por la Resolución 3280 de 2018."
        ),
        "logro_trazador": (
            "Cumplimiento de los controles de salud correspondientes al ciclo vital de cada integrante del núcleo familiar dentro de los próximos 9 meses, "
            "verificado mediante registros clínicos o historia familiar consolidada."
        ),
        "logro_intermedio": (
            "Agendamiento y cumplimiento de al menos una consulta preventiva (médica, odontológica, de enfermería o nutricional) "
            "por integrante familiar en un plazo de hasta 90 días, con acompañamiento del equipo territorial si se requiere."
        ),
        
    },

    "RIESGO DE AISLAMIENTO SOCIAL Y DETERIORO EN SU SALUD FÍSICA Y MENTAL DEBIDO A LA FALTA DE APOYO FAMILIAR CONSTANTE Y HÁBITOS IRREGULARES DE AUTOCUIDADO": {
        "hallazgo_identificado": (
            "Riesgo de aislamiento social y deterioro progresivo de la salud física y mental, asociado a la ausencia de redes de apoyo familiar "
            "y a la inestabilidad en prácticas regulares de autocuidado."
        ),
        "compromiso_concertado": (
            "Fortalecer redes de apoyo familiares y comunitarias mediante la participación activa en espacios sociales y actividades colectivas, "
            "favoreciendo la interacción, el bienestar emocional y el sentido de pertenencia."
        ),
        "logro_trazador": (
            "Integración del individuo o grupo familiar a al menos un espacio comunitario (grupo de apoyo, actividad de salud mental o programa local), "
            "con participación activa durante un periodo mínimo de 4 meses, verificado mediante seguimiento comunitario."
        ),
        "logro_intermedio": (
            "Contacto inicial y vinculación con al menos un recurso de apoyo institucional o comunitario en un plazo máximo de 60 días, "
            "con registro por parte del equipo de salud sobre el inicio de dicha participación."
        ),
        
    },

    "ENVEJECIMIENTO, ENFERMEDADES CRÓNICAS Y CAMBIOS EMOCIONALES": {
        "hallazgo_identificado": (
            "Presencia de procesos de envejecimiento con comorbilidades crónicas y manifestaciones emocionales asociadas a la transición del ciclo vital."
        ),
        "compromiso_concertado": (
            "Asegurar la continuidad del seguimiento clínico y funcional del adulto mayor, garantizando controles médicos, uso adecuado de tratamientos "
            "y atención a su situación emocional y familiar para mejorar su calidad de vida."
        ),
        "logro_trazador": (
            "Estabilidad clínica de enfermedades crónicas con mejora funcional y emocional percibida por el usuario o cuidador "
            "en un periodo de 9 meses, respaldada por evaluación médica o comunitaria."
        ),
        "logro_intermedio": (
            "Asistencia a control médico integral del adulto mayor dentro de los próximos 60 días, con actualización del plan de tratamiento "
            "y orientación sobre autocuidado en el hogar."
        ),
        
    },

    "RIESGO DE MAL NUTRICIÓN": {
        "hallazgo_identificado": (
            "Riesgo nutricional en distintos grupos etarios, evidenciado por malnutrición por exceso o por déficit, asociado a prácticas alimentarias inadecuadas "
            "y desinformación sobre nutrición."
        ),
        "compromiso_concertado": (
            "Promover cambios progresivos en la alimentación familiar mediante orientación práctica sobre consumo adecuado de alimentos locales y accesibles, "
            "favoreciendo una dieta equilibrada y culturalmente apropiada."
        ),
        "logro_trazador": (
            "Mejora en indicadores nutricionales básicos (peso, talla, IMC, perímetro abdominal, según corresponda) en un periodo de 6 a 9 meses, "
            "verificada mediante controles periódicos de seguimiento."
        ),
        "logro_intermedio": (
            "Asistencia a una consulta de valoración nutricional o participación en una charla educativa sobre alimentación saludable "
            "dentro de los próximos 90 días, con implementación de al menos una recomendación práctica en el hogar."
        ),
        
    },

    "plantilla_sin_hallazgos": 
            "Tras la valoración integral familiar, no se evidencian hallazgos negativos y el estado de salud general es adecuado. "
            "El entorno físico es seguro e higiénico, y las relaciones interpersonales dentro del núcleo familiar son armónicas. "
            "Se realizará educación sobre hábitos de vida saludable (alimentación balanceada, actividad física, higiene del sueño y manejo del estrés). "
            "También se abordará la importancia de la comunicación asertiva y la adherencia a controles médicos. "
            "La familia mostró disposición para participar en el proceso educativo y se programará seguimiento según necesidad."
     
}

