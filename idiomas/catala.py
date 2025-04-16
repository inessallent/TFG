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
    
    "boton_continuar": "Continuar", 
    "error_correo": "Si us plau, introdueix un correu electrònic vàlid.",
    "enviado_con_éxtio": "Enviat amb èxit!",
    "Seccion_1": "Secció 1",
    "Seccion_2": "Secció 2",
    "Seccion_3": "Secció 3",
    
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
    # Preguntes Secció 2: Coneixement sobre la IA
    "pregunta_2_1": "Has utilitzat mai la intel·ligència artificial (IA)?",
    "opciones_2_1": ["Sí, molt sovint", "Sí, de tant en tant", "Mai"],

    "pregunta_2_2": "Si has utilitzat la IA, per a què la fas servir principalment? (Pots seleccionar més d’una resposta).",
    "opciones_2_2": ["Ús personal", "Estudi acadèmic", "Feina", "Altres"],

    "pregunta_2_3": "En quin àmbit utilitzes més sovint la IA?",
    "opciones_2_3": ["Art i disseny", "Ciències (Matemàtiques, Física, Biologia, ...)", "Ciències socials (Economia, Història, ...)", "Humanitats (Llengua, literatura, idiomes, ...)", "Negocis i finances", "Altres"],

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
