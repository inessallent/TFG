import streamlit as st

textos = {
    "seleccionar_idioma": "Select language",
    
    # Question options
    "totalmente_en_desacuerdo": "Strongly disagree",
    "en_desacuerdo": "Disagree",
    "neutral": "Neutral",
    "de_acuerdo": "Agree",
    "totalmente_de_acuerdo": "Strongly agree",

    "cuestionario": "Questionnaire",    

    "boton_continuar": "Continue",
    "error_correo": "Please enter a valid email address.",
    "enviado_con_éxtio": "Successfully sent!",
    "Seccion_1": "Section 1",
    "Seccion_2": "Section 2",
    "Seccion_3": "Section 3",

    # Section 1: Personal Information
    "información_personal": "Personal Information",
    "info_personal": "Personal Information", 
    "pregunta_genero": "Gender:",
    "genero_opciones": ["Female", "Male", "Non-binary", "Prefer not to say"],
    "pregunta_edad": "Age:",
    "edad_opciones": ["Under 18", "18 - 24", "25 - 34", "35 - 44", "45 - 54", "55 - 64", "Over 64", "Prefer not to say"],
    "opcion_correo": "Email (optional):",
    "pregunta_nivel_estudios": "Education Level",
    "opciones_nivel_estudios": ["Primary education", "Secondary education", "University education (or higher)", "No education", "Other"], 
    "pregunta_rama_estudios": "Please select the field that best describes your studies:",
    "opciones_rama_estudios": [
        "Arts and Humanities (Design, Philosophy, History, Translation and Interpretation, ...)",
        "Sciences (Environmental Sciences, Physics, Geology, Mathematics, Chemistry, ...)",
        "Health Sciences (Nursing, Medicine, Psychology, Dentistry, Veterinary, ...)",
        "Social and Legal Sciences (Business, Audiovisual Communication, Criminology, Law, Economics, Journalism, Tourism, ...)",
        "Biosciences (Biology, Biochemistry, Genetics, Microbiology, ...)",
        "Engineering and Architecture (Engineering, Industrial, Computer Science, Telecommunications, ...)",
        "Other"
    ],
    "pregunta_años_experiencia": "How many years of experience do you have in this field?:",
    "opciones_años_experiencia": ["Less than 1 year", "1 - 3 years", "4 - 6 years", "7 - 10 years", "More than 10 years"],
    "pregunta_pais_residencia": "In which country do you reside?",
    "Gracias_por_contestar_el_formulario": "Thank you very much for completing the form!",

    # Main texts
    "navegacion": "Navigation",
    "selecciona_una_seccion": "Select a section:",
    "contacto": "Contact",
    "sobre_nosotros": "About Us",
    "info_sobre_nosotros": "This questionnaire is part of the final project from my degree.",
    "info_contacto": "If you would like to contact us, please complete the form below:",
    "correo_electronico_contacto": "Email:",
    "mensaje": "Message:",
    "enviar": "Send",
    "mensaje_enviado": "Message sent successfully!",

    # Errors
    "error_genero": "Please enter your gender.",
    "error_correo": "Invalid email address.",
    "error_age": "Please enter your age.",
    "error_nivel_estudios": "Please enter your education level.",
    "error_rama_estudios": "Please enter your field of study.",
    "error_años_experiencia": "Please enter how many years of experience you have in your field of study.",
    "error_pais_residencia": "Please enter your country of residence.",

    "video_no_encontrado": "The video was not found at the specified path.",
    "selecciona_opción": "Please select an option before continuing.",
}
