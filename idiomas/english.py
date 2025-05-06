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

    "boton_continuar": "Next",
    "boton_atras": "Back",
    "boton_enviar": "Submit",
    
    "error_correo": "Please enter a valid email address.",
    "enviado_con_éxtio": "Successfully sent!",
    "error_terminos": "You must read and accept the terms to continue.", 
    
    "Seccion_1": "Section 1",
    "Seccion_2": "Section 2",
    "Seccion_3": "Section 3",
    
    #Acess to the questionnaire
    "empezar_cuestionario": "Do you want to start the questionnaire?",
    "leer_terminos": "Before starting, please read the following terms and conditions.",
    "confirmo_leer_terminos": "I confirm that I have read the entire document",
    "acepto_terminos": "I have read and accept the information sheet and the informed consent of the project, and I give my consent to participate in the study and for the processing of my personal data.",

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

    # Section 2: Knowledge of AI
    "pregunta_2_1": "Choose the option that best describes Artificial Intelligence (AI):",
    "opciones_2_1": ["Scientific field focused on intelligent programs", "Machines learning and decision-making like humans", "Both are correct"],
    "pregunta_2_2": "Have you ever used Artificial Intelligence (AI)?",
    "opciones_2_2": ["Yes, daily", "Yes, weekly", "Yes, monthly", "Yes, occasionally", "Never"],
    "pregunta_2_3": "If yes, what do you use AI for? (You can select more than one option).",
    "opciones_2_3": ["Personal use", "Academic study", "Work", "Other"],
    "pregunta_2_4": "In what field do you use AI most frequently?",
    "opciones_2_4": ["Art and design", "Sciences", "Social sciences", "Humanities", "Business and finance", "Programming / Engineering", "I don't use it", "Other"],
    "pregunta_2_5": "AI bias question",
    "opciones_2_5": ["To be determined"],
    "pregunta_2_6": "Do you think people are biased in decision-making?",
    "opciones_2_6": ["Yes, always", "Often, depends on the decision", "No, never"],
    "pregunta_2_7": "Who do you think is more biased in decision-making?",
    "opciones_2_7": ["A person", "An AI system"],
    
    # Section 3: Case studies + ethics
    "intro_q33": "In November 2022, Jake Moffatt booked a last-minute flight with Air Canada to attend his grandmother’s funeral...",
    "pregunta_3_3": "Who do you think was right in this case?",
    "opciones_3_3": ["Air Canada", "Jake Moffatt", "Justification (optional)"],
    "intro_q34": "Jake took the company to court. Air Canada said their website had the correct info, but the court disagreed...",
    "pregunta_3_4": "What do you think of the verdict?",
    "opciones_3_4": ["I agree", "I disagree"],
    "pregunta_3_5": "Prof. Joan Fontrodona said AI should follow 3 ethical principles. How much do you agree with them?",
    "opciones_3_5": ["Respect for human dignity", "Freedom", "Justice"],
    "pregunta_3_6": "To what extent do you agree: “AI-based technologies are already helping humans achieve greater efficiency...”",
    "pregunta_3_7": "To what extent do you agree: AI will impact life, business, and relationships by providing predictions and suggestions.",
    

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
