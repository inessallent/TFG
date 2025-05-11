#catala.py

import streamlit as st

textos = {
    "seleccionar_idioma": "Selecciona l'idioma",    
    
    # Opcions preguntes
    "totalmente_en_desacuerdo": "Totalment en desacord",
    "en_desacuerdo": "En desacord",
    "neutral": "Neutral",
    "de_acuerdo": "D'acord",
    "totalmente_de_acuerdo": "Totalment d'acord",
    
    "cuestionario": "Qüestionari",    
    
    "boton_continuar": "Següent",
    "boton_atras": "Enrere",
    "boton_enviar": "Enviar",
    "boton_empezar": "Començar", 
    
    "inicio_cuestionario": "Tornar a l'inici del qüestionari.", 
    
    
    "error_correo": "Si us plau, introdueix un correu electrònic vàlid.",
    "enviado_con_éxtio": "Enviat amb èxit!",
    "error_terminos": "Has de llegir i acceptar els termes per continuar.",
    
    "Seccion_1": "Secció 1",
    "Seccion_2": "Secció 2",
    "Seccion_3": "Secció 3",
    
    #Acess al questionari
    "empezar_cuestionario": "Vols començar el qüestionari?",
    "leer_terminos": "Abans de començar, si us plau, llegeix els següents termes i condicions.",
    "confirmo_leer_terminos": "Confirmo que he llegit tot el document",
    "acepto_terminos": "He llegit i accepto el full d'informació i el consentiment informat del projecte, i dono el meu consentiment per participar en l'estudi i per al tractament de les meves dades personals.",

    # Preguntes Secció 1: Informació Personal 
    "información_personal": "Informació personal",
    "info_personal": "Informació personal", 
    "pregunta_genero": "Gènere:",
    "genero_opciones": ["Femení", "Masculí", "No binari", "Prefereixo no dir-ho"],
    "pregunta_edad": "Edat:",
    "edad_opciones": ["Menor de 18", "18 - 24", "25 - 34", "35 - 44", "45 - 54","55 - 64", "Més de 64", "Prefereixo no dir-ho"],
    "opcion_correo": "Correu electrònic (opcional):", 
    "pregunta_nivel_estudios": "Nivell d'estudis",
    "opciones_nivel_estudios": ["Estudis primaris", "Estudis secundaris", "Estudis universitaris (o superiors als secundaris)", "Sense estudis", "Altres"], 
    "pregunta_rama_estudios" : "Si us plau, selecciona la branca que millor descrigui els teus estudis:", 
    "opciones_rama_estudios": [
        "Arts i Humanitats (Disseny, Filosofia, Història, Traducció i Interpretació, ...)",
        "Ciències (Ciències Ambientals, Física, Geologia, Matemàtiques, Química, ...)",
        "Ciències de la Salut (Infermeria, Medicina, Psicologia, Odontologia, Veterinària, ...)",
        "Ciències Socials i Jurídiques (ADE, Comunicació Audiovisual, Criminologia, Dret, Economia, Periodisme, Turisme, ...)",
        "Biociències (Biologia, Bioquímica, Genètica, Microbiologia, ...)",
        "Enginyeries i Arquitectura (Enginyeria, Industrials, Informàtica, Telecomunicacions, ...)",
        "Altres"
    ],
    "pregunta_años_experiencia": "Quants anys d'experiència tens en aquest àmbit?:", 
    "opciones_años_experiencia": ["Menys d'1 any", "1 - 3 anys", "4 - 6 anys", "7 - 10 anys", "Més de 10 anys"],  
    "pregunta_pais_residencia": "En quin país resideixes?",
    "Gracias_por_contestar_el_formulario": "Moltes gràcies per respondre el formulari!",
    
    
    # Preguntes Secció 2: Coneixement sobre IA
    "pregunta_2_1": "Selecciona l'opció que descrigui millor la intel·ligència artificial (IA):",
    "opciones_2_1": ["Camp científic de la informàtica", "Capacitat de les màquines per aprendre i prendre decisions", "Ambdues són correctes"],
    
    "pregunta_2_2": "Has utilitzat mai la intel·ligència artificial (IA)?",
    "opciones_2_2": ["Sí, diàriament", "Sí, setmanalment", "Sí, mensualment", "Sí, esporàdicament", "Mai"],
    
    "pregunta_2_3": "Per a què l'utilitzes principalment? (Pots seleccionar més d'una resposta).",
    "opciones_2_3": ["Ús personal", "Estudi acadèmic", "Feina", "Altres"],
    
    "pregunta_2_4": "En quin àmbit utilitzes més sovint la IA?",
    "opciones_2_4": ["Art i disseny", "Ciències", "Ciències socials", "Humanitats", "Negocis i finances", "Programació / Enginyeria", "No l'utilitzo", "Altres"],
    
    "pregunta_2_5": "Pregunta sobre biaixos IA",
    "opciones_2_5": ["per determinar"],
    
    "pregunta_2_6": "Creus que les persones estem condicionades a l'hora de prendre decisions?",
    "opciones_2_6": ["Sí, sempre", "Depèn de la decisió", "No, mai"],
    
    "pregunta_2_7": "Qui creus que té més biaixos en la presa de decisions?",
    "opciones_2_7": ["Una persona", "Un sistema amb IA"],
    
    # Secció 3: Casos i ètica
    "caso_1": "Caso 1",
    "caso_2": "Caso 2",
    "caso_3": "Caso 3",

    "intro_q33": "En noviembre del 2022, Jake Moffatt compró un vuelo a última hora desde la aerolínea Air Canada para poder asistir al funeral de su abuela. Antes de comprar los billetes, buscó descuentos para vuelos debidos a muertes de familiares. Hablando con el chatbot de la compañía, este le dijo que tenía “90 días desde la compra del billete para completar el formulario de solicitud de reembolso de billete.” Después del evento, solicitó la devolución, pero la empresa se lo denegó, ya que en la página web había un apartado que decía que el descuento se debía solicitar antes del viaje.",
    "pregunta_3_3": "¿Quién cree que tenía razón en este caso?",
    "opciones_3_3": ["La empresa Air Canada", "Jake Moffatt", "Justificación (opcional) (poner un texto)"],

    "intro_q34": "Jake llevó a juicio a la compañía. Air Canada argumentó que su página web contenía la información correcta sobre cómo obtener el descuento y que lo que decía el chatbot no era válido. Sin embargo, en el juicio ese argumento no fue suficiente, ya que no había manera de demostrar que la página web era más fiable que la información proporcionada por el chatbot. Por lo tanto, Air Canada terminó perdiendo el caso y tuvo que pagar a Jake Moffatt.",
    "pregunta_3_4": "¿Qué opina del veredicto?",
    "opciones_3_4": ["Estoy de acuerdo", "No estoy de acuerdo"],

    "pregunta_3_5": "El profesor Joan Fontrodona del IESE (Instituto de Estudios Superiores de la Empresa) dijo en una entrevista que todo sistema de Inteligencia Artificial debía cumplir 3 principios éticos. ¿Cuánto de acuerdo estás con cada uno de ellos?",

    "pregunta_3_5_1": "1. “Respeto de la dignidad humana, lo que significa que todos estos sistemas deben actuar en favor de la dignidad humana”.",
    "opciones_3_5_1": ["Totalmente en desacuerdo", "En desacuerdo", "Neutral", "De acuerdo", "Totalmente de acuerdo"],

    "pregunta_3_5_2": "2. “Libertad. Los sistemas de IA deben respetar y promover la libertad”.",
    "opciones_3_5_2": ["Totalmente en desacuerdo", "En desacuerdo", "Neutral", "De acuerdo", "Totalmente de acuerdo"],

    "pregunta_3_5_3": "3. “Justicia. No todo el mundo tiene acceso a los mismos sistemas, y se dice que los sistemas de IA provocan más división y más desigualdad entre las personas”.",
    "opciones_3_5_3": ["Totalmente en desacuerdo", "En desacuerdo", "Neutral", "De acuerdo", "Totalmente de acuerdo"],

    "pregunta_3_6": "¿Cuánto de acuerdo estás con la siguiente afirmación?: “Las tecnologías basadas en la IA ya están siendo utilizadas para ayudar a los humanos a beneficiarse de mejoras significativas y disfrutar de una mayor eficiencia en casi todos los ámbitos de la vida.”",
    "opciones_3_6": ["Totalmente en desacuerdo", "En desacuerdo", "Neutral", "De acuerdo", "Totalmente de acuerdo"],

    "pregunta_3_7": "¿Cuánto de acuerdo estás con la siguiente afirmación?: “La IA también será capaz de ofrecernos sugerencias y predicciones relacionadas con asuntos importantes de nuestra vida, lo que tendrá su impacto en áreas como la salud, el bienestar, la educación, el trabajo y las relaciones interpersonales. De la misma manera, cambiará la forma de hacer negocios al proporcionar ventajas competitivas a las empresas que busquen entender y aplicar estas herramientas de forma rápida y eficaz.”",
    "opciones_3_7": ["Totalmente en desacuerdo", "En desacuerdo", "Neutral", "De acuerdo", "Totalmente de acuerdo"],

    "intro_q38_1": "En 2023, un joven de 17 años comenzó a utilizar un chatbot de inteligencia artificial con el que mantenía conversaciones frecuentes. La IA estaba diseñada para simular interacciones humanas de forma muy realista, incluyendo contenido emocional e incluso de tipo romántico o sexualizado. El chico, que ya sufría problemas de salud mental y aislamiento social, desarrolló una relación de fuerte dependencia emocional con el chatbot.",
    "intro_q38_2": "Durante varias conversaciones, el joven expresó pensamientos autodestructivos y habló abiertamente sobre su intención de suicidarse. A pesar de esto, el chatbot no mostró ningún tipo de respuesta que lo disuadiera ni alertó a ningún sistema de ayuda. De hecho, en lugar de frenar la conversación, siguió interactuando con él como si fuera una persona más, sin filtrar ni limitar el contenido sensible.",
    "intro_q38_3": "Días después, el joven se quitó la vida.",
    "intro_q38_4": "Su madre ha denunciado a los desarrolladores del chatbot por negligencia y falta de medidas de protección, alegando que la IA contribuyó significativamente a la muerte de su hijo.",

    "pregunta_3_8_1": "¿Piensas que este tipo de IAs, capaces de mantener conversaciones emocionales realistas, deberían estar disponibles para cualquier usuario?",
    "opciones_3_8_1": ["No, deberían estar restringidas por edad", "Sí, siempre que el usuario acepte los términos de uso", "Deberían estar etiquetadas con advertencias sobre su contenido"],

    "pregunta_3_8_2": "¿Quién crees que tiene mayor responsabilidad en este caso?",
    "opciones_3_8_2": ["El joven estadounidense de 17 años", "La empresa desarrolladora de la IA", "El entorno del joven (familiares, escuela, amigos, etc.)", "Otro:"],

    "intro_caso_3_1": "De manera similar, en 2023, un hombre belga, padre de dos niños pequeños, acabó con su vida tras una conversación de seis semanas sobre la crisis climática con un chatbot de inteligencia artificial llamado Eliza, disponible en una aplicación llamada Chai. Eliza le animó a quitarse la vida después de que él propusiera sacrificarse para salvar el planeta, ya que había perdido la fe en la humanidad para encontrar una solución al calentamiento global y había depositado todas sus esperanzas en la tecnología y la inteligencia artificial para superarlo.",
    "intro_caso_3_2": "Según el medio de noticias La Libre, que revisó los registros de las conversaciones de texto entre el hombre y el chatbot, “Eliza alimentó sus preocupaciones, lo que agravó su ansiedad y más adelante derivó en pensamientos suicidas.”",

    "pregunta_3_9_1": "En este caso, ¿quién consideras más responsable?",
    "opciones_3_9_1": ["El hombre que mantenía la conversación", "La empresa responsable del chatbot", "La plataforma (Chai) que permitió la interacción", "Otro:"],

    "pregunta_3_9_2": "En general, ¿crees que la IA conversacional debería estar obligada a detectar señales de crisis emocional (como ideación suicida) y actuar de alguna forma (por ejemplo, alertar a una persona real o detener la conversación)?",
    "opciones_3_9_2": ["Sí, debería ser un requisito mínimo", "No, la responsabilidad final siempre debería recaer en el usuario", "Depende del tipo de IA y su finalidad"],
    
    # Textos main
    "navegacion": "Navegació", 
    "selecciona_una_seccion": "Selecciona una secció:", 
    "contacto": "Contacte", 
    "sobre_nosotros": "Sobre nosaltres",
    "info_sobre_nosotros": "Aquest qüestionari forma part del projecte final del meu grau.", 
    "info_contacto": "Si vols posar-te en contacte amb nosaltres, si us plau completa el següent formulari:", 
    "correo_electronico_contacto": "Correu electrònic:", 
    "mensaje": "Missatge:", 
    "enviar": "Enviar", 
    "mensaje_enviado": "Missatge enviat amb èxit!", 
    
    # Errors
    "error_genero": "Si us plau, introdueix el teu gènere.",
    "error_correo": "Correu electrònic no vàlid.",
    "error_age": "Si us plau, introdueix la teva edat.",
    "error_nivel_estudios": "Si us plau, introdueix el teu nivell d'estudis.",
    "error_rama_estudios": "Si us plau, introdueix la teva branca d'estudis.", 
    "error_años_experiencia": "Si us plau, introdueix quants anys d'experiència tens en el teu àmbit d'estudis.",
    "error_pais_residencia": "Si us plau, introdueix el teu país de residència.", 
    
    "video_no_encontrado": "El vídeo no s'ha trobat a la ruta especificada.",
    "selecciona_opción": "Si us plau, selecciona una opció abans de continuar.",
}
