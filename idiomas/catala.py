#catala.py

import streamlit as st

textos = {
    "seleccionar_idioma": "Selecciona l'idioma",    
    "totalmente_en_desacuerdo": "Totalment en desacord",
    "en_desacuerdo": "En desacord",
    "neutral": "Neutral",
    "de_acuerdo": "D'acord",
    "totalmente_de_acuerdo": "Totalment d'acord",
    "video_no_encontrado": "El vídeo no s'ha trobat a la ruta especificada.",
    "selecciona_opción": "Si us plau, selecciona una opció abans de continuar.",
    "cuestionario": "Questionari",    
    "nombre": "Nom:", 
    "info_personal": "Informació Personal", 
    "apellido": "Cognom:", 
    "pregunta_genero": "Gènere:",
    "genero_opciones": ["Femení", "Masculí", "No binari", "Prefereixo no dir-ho"],
    "pregunta_edad": "Edat:",
    "edad_opciones": ["Menys de 18", "18 - 24", "25 - 34", "35 - 44", "45 - 54", "55 - 64", "Més de 64", "Prefereixo no dir-ho"],
    "opcion_correo": "Correu Electrònic (opcional):", 
    "boton_continuar": "Continuar", 
    "error_correo": "Si us plau, introdueix una adreça de correu electrònic vàlida.",
    "enviado_con_éxtio": "Enviat amb èxit!",
    "advertencia_faltan_datos": "Si us plau, introdueix el teu nom, cognom, gènere i edat. Gràcies.", 
    
    
    "información_personal": "Informació Personal",
    "pregunta_nivel_estudio": "Nivell d'estudis",
    "opciones_nivel_estudios": ["Estudis primaris", "Estudis secundaris", "Estudis universitaris (o superiors als secundaris)", "Sense estudis", "Altres"], 
    "pregunta_sector_estudio_trabajo": "Si us plau, selecciona el sector que millor descrigui la teva feina o estudis (en el cas que siguis estudiant):", 
    "opciones_sector": ["Arts i Humanitats", "Negocis i Economia", "Ciències de la Computació i Informàtica", "Educació", "Enginyeria i Tecnologia", "Ciències Ambientals i de la Terra", "Salut i Medicina", "Dret i Estudis Legals", "Ciències de la Vida i Biologia", "Matemàtiques i Estadística", "Ciències Físiques (p. ex., Física, Química)", "Ciències Socials", "Altres"],
    "pregunta_experiencia": "Quants anys d'experiència tens en aquest àmbit?:", 
    "opciones_experiencia": ["Menys d'1 any", "1 - 3 anys", "4 - 6 anys", "7 - 10 anys", "Més de 10 anys"], 
    "pregunta_ciudad": "¿En que païs resideix?",
    "Gracias_por_contestar_el_formulario": "Moltes gràcies per contestar el formulari!",

    
    # Texts main
    "navegacion": "Navegació", 
    "selecciona_una_seccion": "Selecciona una secció:", 
    "contacto": "Contacte", 
    "sobre_nosotros": "Sobre Nosaltres",
    "info_sobre_nosotros": "Aquest qüestionari és part del projecte final de la meva carrera.", 
    "info_contacto": "Si desitges posar-te en contacte amb nosaltres, si us plau completa el següent formulari:", 
    "correo_electronico_contacto": "Correu electrònic: ", 
    "mensaje": "Missatge: ", 
    "enviar": "Enviar", 
    "mensaje_enviado": "Missatge enviat amb èxit!",  
    
    #Errores
    "error_nombre": "Si us plau, introdueixi el seu nom. ",  
    "error_apellido": "Si us plau, introdueixi el seu cognom. ",  
    "error_genero": "Si us plau, introdueixi el seu gènere. ",  
    "error_correo": "Correu electrònic no vàlid. ",  
    "error_age": "Si us plau, introdueixi la seva edat. ",  
}
