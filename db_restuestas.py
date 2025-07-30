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

#--------------Diccionario con los hallazgos, compromisos y logros por curso de edad------------------------------------

datos_por_ciclo_vida: Dict[str, Dict[str, str]] = {

    "0 a 5": {
        "ciclo": "PRIMERA INFANCIA",
        "hallazgo": (
            "Se reconocen esfuerzos familiares por atender las necesidades del niño, como la lactancia y el seguimiento de controles. "
            "Sin embargo, persisten prácticas alimentarias mejorables y asistencia irregular a controles. En el hogar, hay condiciones que podrían ajustarse para fortalecer la seguridad y la higiene, especialmente en lo respiratorio y digestivo."
        ),
        "compromiso": "Garantizar alimentación adecuada, asistir a controles, mejorar la seguridad del hogar y fortalecer prácticas de higiene.",
        "logro_trazador": "Cumplimiento del 90% de los controles de crecimiento y vacunación en 6 meses con registros clínicos actualizados.",
        "logro_intermedio": "Evaluación domiciliaria y mejoras mínimas en seguridad e higiene en un plazo de 90 días."
    },
    "6 a 11": {
        "ciclo": "INFANCIA",
        "hallazgo": (
            "Se evidencia una disposición familiar hacia el cuidado y la higiene, aunque con oportunidades para mejorar la regularidad y supervisión. "
            "Se observa consumo moderado de alimentos procesados y uso frecuente de pantallas, así como variabilidad en la actividad física. Estos factores pueden afectar el bienestar y el rendimiento escolar del niño."
        ),
        "compromiso": "Promover alimentación saludable, aumentar actividad física y supervisar hábitos de higiene.",
        "logro_trazador": "Rutinas saludables 5 días por semana con evidencia en controles o registros familiares en 6 meses.",
        "logro_intermedio": "Sesión educativa sobre alimentación, higiene y actividad física en los primeros 90 días."
    },
    "12 a 17": {
        "ciclo": "ADOLESCENCIA",
        "hallazgo": (
            "Se aprecian vínculos familiares presentes y disposición a mejorar la convivencia, aunque se identifican dificultades en la comunicación emocional. "
            "Puede haber exposición a riesgos como sustancias psicoactivas y hábitos irregulares de alimentación, sueño o autocuidado, aspectos que pueden optimizarse con acompañamiento."
        ),
        "compromiso": "Mejorar la comunicación, prevenir conductas de riesgo y establecer rutinas saludables.",
        "logro_trazador": "Mejora en comunicación y reducción de riesgos en evaluación psicosocial o médica en 6 meses.",
        "logro_intermedio": "Sesión grupal o familiar sobre comunicación, autocuidado y prevención en 90 días."
    },
    "18 a 28": {
        "ciclo": "JUVENTUD",
        "hallazgo": (
            "Se evidencia interés por el autocuidado y autonomía en muchos jóvenes, aunque persisten hábitos alimentarios irregulares y niveles variables de actividad física. "
            "La participación en controles de salud es ocasional, y pueden reforzarse el manejo del estrés y la integración en redes familiares o comunitarias de apoyo."
        ),
        "compromiso": "Mejorar alimentación, aumentar actividad física, asistir a controles y fortalecer redes de apoyo.",
        "logro_trazador": "Controles regulares y adopción de hábitos saludables documentados por 6 meses.",
        "logro_intermedio": "Participación en actividades de salud y agendamiento de controles en 90 días."
    },
    "29 a 59": {
        "ciclo": "ADULTEZ",
        "hallazgo": (
            "Muchas personas en esta etapa muestran compromiso con su familia y trabajo, aunque tienden a postergar su bienestar personal. "
            "Son comunes estilos de vida sedentarios, alimentación poco equilibrada y limitada participación en controles médicos, lo que puede afectar la salud emocional y familiar."
        ),
        "compromiso": "Reducir sedentarismo, mejorar la dieta, asistir a controles y promover el bienestar emocional.",
        "logro_trazador": "Estilo de vida activo y alimentación adecuada, reflejado en evaluaciones y registros en 6 meses.",
        "logro_intermedio": "Asistencia a control médico y actividad de bienestar emocional dentro de 90 días."
    },
    ">60": {
        "ciclo": "VEJEZ",
        "hallazgo": (
            "En esta etapa, muchas personas conservan su funcionalidad con el apoyo de su familia. Aun así, se presentan algunas limitaciones en la movilidad, hábitos alimentarios que pueden optimizarse y menor participación social. "
            "El acceso a servicios de salud puede ser intermitente, por lo que fortalecer el acompañamiento familiar y comunitario es clave."
        ),
        "compromiso": "Promover movilidad, mejorar alimentación, asegurar acceso a salud y fortalecer acompañamiento social y familiar.",
        "logro_trazador": "Mejora o mantenimiento de funcionalidad y bienestar reflejado en controles y valoración familiar en 6 meses.",
        "logro_intermedio": "Plan de actividades físicas y acompañamiento con seguimiento familiar en 90 días."
    }
}

#-------Diccionario de sobrecarga del cuidador----------

sobrecarga_cuidador = {
    True: {
        "hallazgo": "SI TIENE SOBRECARGA EL CUIDADOR",
        "compromiso": (
            "Identificar y monitorear regularmente los signos de fatiga física, emocional y mental del cuidador principal mediante herramientas clínicas, "
            "entrevistas personales y apoyo interdisciplinario, fomentando el acompañamiento familiar."
        ),
        "logro_trazador": (
            "Sensibilizar al núcleo familiar y al propio cuidador sobre los efectos de la sobrecarga a través de talleres y sesiones informativas "
            "durante los primeros seis meses del plan de intervención centrado en el bienestar del cuidador."
        ),
        "logro_intermedio": (
            "Documentar y analizar la distribución de responsabilidades de cuidado entre el cuidador principal y otros miembros de la familia, "
            "priorizando el equilibrio de cargas desde el inicio del proceso."
        )
    },
    False: {
        "hallazgo": "NO TIENE SOBRECARGA EL CUIDADOR",
        "compromiso": (
            "Promover el mantenimiento del equilibrio emocional, físico y social del cuidador a través de espacios de autocuidado, pausas activas y dinámicas "
            "familiares colaborativas que refuercen su bienestar integral."
        ),
        "logro_trazador": (
            "Fortalecer el conocimiento del cuidador y la familia sobre estrategias de prevención de la sobrecarga mediante actividades educativas continuas "
            "dentro del primer semestre del plan familiar de salud."
        ),
        "logro_intermedio": (
            "Establecer una línea base del tiempo y tipo de actividades que realiza el cuidador, con el fin de preservar una distribución saludable "
            "de sus funciones sin generar desgaste."
        )
    }
}

#-------------Diccionario actividades ludicas y deportivas-------------------------

DICT_CUIDADO_ENTORNO = {
    True: {
        "ACTIVIDADES DEPORTIVAS COMUNITARIAS": {
            "hallazgo": (
                "La familia participa activamente en actividades deportivas organizadas en su comunidad, "
                "lo que fortalece sus vínculos sociales y promueve estilos de vida saludables."
            ),
            "compromiso": (
                "Fortalecer y mantener la participación de todos los integrantes del núcleo en espacios deportivos comunitarios, "
                "aprovechando las oportunidades locales de recreación y bienestar físico."
            ),
            "logro_trazador": (
                "Consolidar una rutina semanal de participación familiar en eventos deportivos al aire libre, "
                "como caminatas, ciclorrutas, torneos o clases grupales de ejercicio."
            ),
            "logro_intermedio": (
                "Lograr que cada miembro de la familia se vincule de manera continua a una actividad física promovida por su comunidad "
                "durante al menos un mes consecutivo."
            )
        },
        "ACTIVIDADES LÚDICAS Y CULTURALES COMUNITARIAS": {
            "hallazgo": (
                "La familia demuestra interés y participación en actividades culturales, artísticas y lúdicas de su entorno comunitario, "
                "reforzando su identidad local y convivencia social."
            ),
            "compromiso": (
                "Estimular espacios familiares para el disfrute y la creación colectiva en escenarios artísticos, recreativos y culturales ofrecidos por la comunidad."
            ),
            "logro_trazador": (
                "Implementar un calendario familiar de asistencia a eventos culturales como ferias, talleres, conciertos o cine comunitario, "
                "que promueva el aprendizaje y la expresión creativa."
            ),
            "logro_intermedio": (
                "Concretar la participación activa de al menos dos integrantes de la familia en una actividad cultural organizada por la comunidad "
                "cada quince días durante un trimestre."
            )
        }
    },
    False: {
        "ACTIVIDADES DEPORTIVAS COMUNITARIAS": {
            "hallazgo": (
                "Actualmente, la familia no participa en actividades deportivas comunitarias, "
                "lo cual puede limitar sus oportunidades de interacción social y cuidado de la salud física."
            ),
            "compromiso": (
                "Motivar a la familia para explorar espacios deportivos cercanos, identificando barreras de acceso o desinterés que impidan su participación."
            ),
            "logro_trazador": (
                "Desarrollar estrategias comunitarias de inclusión deportiva para la familia, como visitas guiadas a eventos locales, "
                "alianzas con instructores barriales o acompañamiento inicial en actividades físicas."
            ),
            "logro_intermedio": (
                "Realizar un mapeo participativo de intereses y horarios disponibles de la familia para facilitar su vinculación progresiva "
                "con espacios de actividad física colectiva."
            )
        },
        "ACTIVIDADES LÚDICAS Y CULTURALES COMUNITARIAS": {
            "hallazgo": (
                "Se evidencia una baja participación familiar en espacios lúdicos y culturales de la comunidad, "
                "lo que reduce oportunidades de interacción positiva y desarrollo emocional compartido."
            ),
            "compromiso": (
                "Promover el acercamiento gradual de la familia a escenarios culturales mediante actividades accesibles, pertinentes y divertidas."
            ),
            "logro_trazador": (
                "Diseñar con la familia un plan de integración cultural que contemple experiencias sencillas como juegos tradicionales, "
                "visitas a bibliotecas, ferias o encuentros comunitarios de narración oral."
            ),
            "logro_intermedio": (
                "Facilitar la participación de la familia en al menos una actividad cultural comunitaria mensual durante tres meses consecutivos, "
                "con seguimiento y retroalimentación."
            )
        }
    }
}

#---------Diccionario para red de apoyo comunitario------------

red_apoyo_comunitario = {
    False: {
        "hallazgo": "NO CUENTA CON RED DE APOYO COMUNITARIO",
        "compromiso": (
            "Motivar la construcción de vínculos comunitarios significativos mediante la identificación de líderes vecinales, "
            "grupos de interés o espacios comunitarios que favorezcan la integración progresiva de la familia."
        ),
        "logro_trazador": (
            "Diseñar una estrategia participativa para fortalecer el sentido de comunidad y corresponsabilidad social, "
            "incluyendo actividades de integración o brigadas de apoyo vecinal en el entorno cercano."
        ),
        "logro_intermedio": (
            "Realizar un mapeo de actores comunitarios disponibles y establecer al menos una conexión inicial que facilite el "
            "acompañamiento externo en situaciones de necesidad o vulnerabilidad."
        )
    },
    True: {
        "hallazgo": "SI CUENTA CON RED DE APOYO COMUNITARIO",
        "compromiso": (
            "Reforzar la participación activa de la familia dentro de los espacios comunitarios existentes, promoviendo relaciones de colaboración "
            "y ayuda mutua frente a retos compartidos."
        ),
        "logro_trazador": (
            "Consolidar mecanismos de cooperación entre la familia y su red comunitaria, como comités vecinales, grupos de madres, "
            "juntas de acción comunal u otras formas de organización barrial."
        ),
        "logro_intermedio": (
            "Coordinar una actividad comunitaria en la que la familia tenga un rol participativo o de liderazgo, favoreciendo el fortalecimiento "
            "del tejido social y el sentido de pertenencia."
        )
    }
}

#------------Diccionario para analisis segun apgar---------------------

resultados_apgar: Dict[str, Dict[str, str]] = {
    "17 A 20": {
        "titulo": "Funcionalidad familiar adecuada",
        "acuerdo": (
            "La familia evaluada presenta una funcionalidad adecuada, con relaciones positivas y mecanismos de afrontamiento "
            "efectivos ante situaciones cotidianas. Se observa cohesión, afecto, y una adecuada comunicación entre los miembros. "
            "Se considera que no hay signos de disfunción familiar. Sin embargo, se recomienda continuar fortaleciendo los lazos "
            "familiares mediante actividades que promuevan el tiempo compartido, la escucha activa y la resolución asertiva de conflictos."
        )
    },
    "16 A 13": {
        "titulo": "Disfunción leve: prevención y fortalecimiento",
        "acuerdo": (
            "La familia presenta indicadores de leve disfunción, posiblemente relacionados con dificultades puntuales en áreas como la "
            "toma de decisiones, la comunicación o el apoyo emocional. Aunque se mantienen ciertas dinámicas funcionales, es importante "
            "intervenir con orientación psicoeducativa para evitar un deterioro progresivo. Se recomienda reforzar habilidades de comunicación, "
            "fortalecer redes de apoyo y promover espacios para el diálogo y la expresión emocional."
        )
    },
    "12 A 10": {
        "titulo": "Disfunción moderada: intervención estructurada",
        "acuerdo": (
            "Se identifica una disfunción moderada en la dinámica familiar, reflejada en una percepción de bajo apoyo, escasa adaptabilidad "
            "y dificultades en la cohesión del grupo familiar. Estas condiciones pueden afectar el bienestar emocional de sus miembros. "
            "Se sugiere una intervención psicológica estructurada, que incluya sesiones de orientación familiar, promoción de la escucha activa, "
            "solución de conflictos y establecimiento de normas claras y consensuadas."
        )
    },
    "9 O MENOS": {
        "titulo": "Disfunción severa: intervención inmediata",
        "acuerdo": (
            "El resultado obtenido indica una disfunción familiar severa, que puede estar afectando significativamente el bienestar emocional, "
            "la comunicación y el sentido de pertenencia de los miembros. Es posible que existan conflictos graves no resueltos, aislamiento emocional "
            "o fallas en el apoyo mutuo. Se recomienda una intervención inmediata desde el área psicosocial, que incluya seguimiento psicológico individual "
            "y familiar, fortalecimiento de factores protectores y remisión a otras instancias de apoyo si es necesario."
        )
    }
}


#-----------Diccionario con factores de cuidado ultimo punto----------------------------

DICT_FACTORES_CUIDADO = {
    "COMUNICACION NO ASERTIVA, USO INADECUADO DE PANTALLAS LO CUAL DIFICULTA LAS INTERACCIONES FAMILIARES": {
        "hallazgo": "Presencia de patrones de comunicación no asertiva e inadecuado uso de dispositivos electrónicos, lo que interfiere en las dinámicas familiares y limita la calidad de las interacciones interpersonales.",
        "implementacion": "Se implementarán encuentros educativos durante las visitas domiciliarias. Se promoverán prácticas de comunicación respetuosa y escucha activa entre los miembros de la familia. Además, se orientará sobre el uso equilibrado de la tecnología y la importancia de compartir tiempos sin pantallas. Se fomentará el fortalecimiento de vínculos afectivos y espacios de diálogo familiar. Todo con enfoque participativo y adaptado al contexto familiar.",
        "cierre": "Se considera finalizado el proceso cuando se evidencia una disminución de los conflictos interpersonales y una mejora en la comunicación emocional asertiva. Asimismo, se observa continuidad en las prácticas saludables adoptadas, incluyendo avances en parámetros de salud básica. El cierre también se sustenta en la apropiación de estrategias de autorregulación emocional y digital, mantenidas en el tiempo. Finalmente, se reconoce una mayor estabilidad emocional y una actitud proactiva para solicitar apoyo profesional cuando sea necesario."
    },
    "INASISTENCIA A SERVICIOS DE SALUD DENTRO DEL MARCO DE LOS SERVICIOS DE LA RUTA DE PROMOCION Y MANTENIMIENTO DE LA SALUD": {
        "hallazgo": "Baja adherencia a los servicios integrales de atención en salud en el marco de la Ruta de Promoción y Mantenimiento de la Salud, lo que limita la detección temprana, la intervención oportuna y la continuidad del cuidado.",
        "implementacion": "Se realizarán visitas domiciliarias con educación en salud adaptada a la familia. Se explicará la importancia de los controles, vacunación y prevención de enfermedades. Se identificarán barreras y se gestionarán apoyos para facilitar el acceso a los servicios. La familia será parte activa del proceso, promoviendo su corresponsabilidad. Todo se hará con enfoque comunitario y culturalmente pertinente.",
        "cierre": "Se considera cerrado cuando la familia demuestra mejoras sostenidas en la comunicación, con prácticas más asertivas y mayor disposición al diálogo respetuoso. Se observa una reducción del uso inadecuado de dispositivos electrónicos y un aumento en las interacciones presenciales de calidad. Además, la familia reconoce la importancia del equilibrio entre tecnología y convivencia. Estos cambios se evidencian de forma estable durante las visitas de seguimiento."
    },
    "RIESGO DE AISLAMIENTO SOCIAL Y DETERIORO EN SU SALUD FÍSICA Y MENTAL DEBIDO A LA FALTA DE APOYO FAMILIAR CONSTANTE Y HÁBITOS IRREGULARES DE AUTOCUIDADO": {
        "hallazgo": "Riesgo de aislamiento social y deterioro progresivo de la salud física y mental, asociado a la ausencia de redes de apoyo familiar y a la inestabilidad en prácticas regulares de autocuidado.",
        "implementacion": "Se promoverá la reconstrucción de redes de apoyo a través del acompañamiento psicosocial en visitas domiciliarias. Se fortalecerán rutinas de autocuidado mediante orientación personalizada y seguimiento periódico. Además, se fomentará la vinculación con actividades comunitarias y servicios disponibles en el territorio. La intervención buscará mejorar la estabilidad emocional y la participación activa en su proceso de cuidado. Todo se realizará con enfoque humanizado, familiar y comunitario.",
        "cierre": "Se considera cerrado cuando se evidencia una mayor participación del individuo en espacios comunitarios y sociales, así como la activación de redes de apoyo formales o informales. Se observan mejoras en las rutinas de autocuidado y un compromiso sostenido con el seguimiento de su salud física y mental. Además, se identifica mayor autonomía, estabilidad emocional y disposición para buscar ayuda oportuna. Estos avances se mantienen de forma constante durante el acompañamiento."
    },
    "ENVEJECIMIENTO, ENFERMEDADES CRÓNICAS Y CAMBIOS EMOCIONALES": {
        "hallazgo": "Presencia de procesos de envejecimiento con comorbilidades crónicas y manifestaciones emocionales asociadas a la transición del ciclo vital.",
        "implementacion": "Se implementará un plan de cuidado centrado en el acompañamiento integral durante las visitas domiciliarias. Se fortalecerá el autocuidado y la adherencia al tratamiento, así como la expresión emocional y adaptación a los cambios del ciclo vital. Se promoverá la participación en redes de apoyo comunitario y espacios de socialización. Además, se articulará con programas de atención al adulto mayor para garantizar seguimiento continuo. Todo con enfoque biopsicosocial y centrado en la dignidad del envejecimiento.",
        "cierre": "Se considera cerrado cuando la persona mayor muestra adherencia al tratamiento de sus comorbilidades, estabilidad en su estado de salud y participación activa en su proceso de autocuidado. Se evidencia aceptación progresiva de los cambios propios del ciclo vital y manejo adecuado de las emociones asociadas. Además, cuenta con acompañamiento familiar o comunitario que respalda su bienestar integral. Estos logros se mantienen durante las visitas de seguimiento y no requieren intervenciones adicionales intensivas."
    },
    "RIESGO DE MAL NUTRICIÓN": {
        "hallazgo": "Riesgo nutricional en diferentes grupos etarios, con manifestaciones de malnutrición por exceso o por déficit, asociado a prácticas alimentarias inadecuadas y desinformación nutricional.",
        "implementacion": "Se desarrollarán intervenciones educativas durante las visitas domiciliarias, enfocadas en mejorar las prácticas alimentarias y corregir desinformación nutricional. Se brindarán recomendaciones adaptadas según la edad, condición de salud y contexto familiar. Además, se promoverá el acceso a alimentos saludables y se articulará con servicios de apoyo nutricional comunitario. El seguimiento será continuo y orientado a fortalecer hábitos sostenibles. Todo con enfoque preventivo, familiar y culturalmente pertinente.",
        "cierre": "Se considera cerrado cuando los integrantes de la familia adoptan prácticas alimentarias más equilibradas, ajustadas a su grupo etario y condición de salud. Se observa mejoría en los indicadores nutricionales, ya sea por la recuperación de peso saludable o la reducción del exceso. Además, demuestran comprensión de las recomendaciones brindadas y aplican de forma autónoma hábitos de alimentación adecuados. Estos cambios se sostienen en el tiempo y se refuerzan en cada seguimiento."
    },
    "ACTIVIDADES DEPORTIVAS COMUNITARIAS": {
        "hallazgo": "No cuenta con actividades deportivas comunitarias.",
        "implementacion": "Se promoverá la activación de espacios locales para la práctica de actividad física mediante el trabajo conjunto con líderes comunitarios y entidades territoriales. Durante las visitas domiciliarias se orientará a las familias sobre la importancia del ejercicio regular para la salud física y mental. Se sugerirán rutinas sencillas que puedan realizarse en el hogar o en espacios abiertos del barrio. Además, se fomentará la organización de grupos comunitarios para caminatas, juegos o pausas activas. Todo con enfoque participativo y de promoción de la salud.",
        "cierre": "Se considera cerrado cuando la familia o sus miembros participan activamente en espacios comunitarios de actividad física o han incorporado rutinas de ejercicio en su entorno cercano. Se evidencia comprensión de los beneficios del movimiento regular para la salud y se mantiene una práctica constante, adecuada a la edad y condición física. Además, se fortalecen vínculos con la comunidad a través de estas actividades. Estos cambios se sostienen durante las visitas de seguimiento."
    },
    "ACTIVIDADES LÚDICAS Y CULTURALES COMUNITARIAS": {
        "hallazgo": "No cuenta con actividades lúdicas y culturales comunitarias.",
        "implementacion": "Se impulsará la gestión y promoción de espacios participativos en articulación con líderes locales, instituciones educativas y entidades culturales. Durante las visitas domiciliarias se motivará a las familias a participar en actividades recreativas que fortalezcan la identidad, la convivencia y el bienestar emocional. Se propondrán iniciativas sencillas como encuentros barriales, juegos tradicionales o talleres artísticos. Además, se promoverá la integración intergeneracional como herramienta de cohesión social. Todo con enfoque comunitario, participativo y culturalmente pertinente.",
        "cierre": "Se considera cerrado cuando la familia participa de manera activa en actividades lúdicas o culturales disponibles en la comunidad, o ha desarrollado espacios recreativos propios en su entorno. Se reconoce el valor de estas prácticas para fortalecer los lazos familiares, el bienestar emocional y la integración social. Además, se promueve la continuidad de estas acciones como parte de su dinámica habitual. Estos avances se mantienen de forma estable en los seguimientos realizados."
    },
    "RED DE APOYO COMUNITARIO": {
        "hallazgo": "No cuenta con red de apoyo comunitario.",
        "implementacion": "Se promoverá la identificación y fortalecimiento de vínculos con vecinos, líderes locales y actores sociales del territorio. Durante las visitas domiciliarias se orientará a la familia sobre la importancia del apoyo mutuo y la participación en espacios comunitarios. Se fomentará la vinculación con grupos organizados, comités locales o iniciativas solidarias existentes. Además, se articulará con entidades e instituciones que favorezcan la construcción de redes de cuidado. Todo con enfoque comunitario, participativo y sostenible.",
        "cierre": "Se considera cerrado cuando la familia ha logrado establecer vínculos con redes de apoyo comunitario formales o informales, como vecinos, grupos locales o instituciones del territorio. Se evidencia mayor participación en espacios comunitarios y disposición para solicitar ayuda cuando es necesario. Además, se fortalecen los lazos de solidaridad y corresponsabilidad en su entorno. Estos cambios se mantienen y se reafirman durante las visitas de seguimiento."
    }
}
