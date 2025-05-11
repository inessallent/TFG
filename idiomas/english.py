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
    "boton_empezar": "Begin", 
    
    "inicio_cuestionario": "Return to the beginning of the questionnaire.", 
    
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
    "case_1": "Case 1",
    "case_2": "Case 2",
    "case_3": "Case 3",

    "intro_q33": "In November 2022, Jake Moffatt bought a last-minute flight from Air Canada to attend his grandmother’s funeral. Before purchasing the ticket, he searched for bereavement discounts. Speaking with the airline’s chatbot, it told him he had “90 days from the date of ticket purchase to complete the refund request form.” After the event, he submitted the request, but the company denied it, stating that their website said the discount must be requested before traveling.",
    "question_3_3": "Who do you think was right in this case?",
    "options_3_3": ["The company, Air Canada", "Jake Moffatt", "Justification (optional) (write a comment)"],

    "intro_q34": "Jake took the company to court. Air Canada argued that the correct information was on their website and that the chatbot's answer was not valid. However, the court did not accept this argument, as there was no way to prove the website was more reliable than the information provided by the chatbot. Air Canada lost the case and was ordered to pay Jake Moffatt.",
    "question_3_4": "What do you think of the verdict?",
    "options_3_4": ["I agree", "I disagree"],

    "question_3_5": "Professor Joan Fontrodona from IESE (Institute of Higher Business Studies) stated in an interview that every AI system should follow 3 ethical principles. How much do you agree with each of them?",

    "question_3_5_1": "1. “Respect for human dignity, meaning all these systems must act in favor of human dignity.”",
    "options_3_5_1": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],

    "question_3_5_2": "2. “Freedom. AI systems must respect and promote freedom.”",
    "options_3_5_2": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],

    "question_3_5_3": "3. “Justice. Not everyone has access to the same systems, and it is said that AI systems increase division and inequality among people.”",
    "options_3_5_3": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],

    "question_3_6": "How much do you agree with the following statement?: “AI-based technologies are already being used to help humans achieve significant improvements and enjoy greater efficiency in nearly every area of life.”",
    "options_3_6": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],

    "question_3_7": "How much do you agree with the following statement?: “AI will also be able to offer us suggestions and predictions related to important areas of our lives, impacting health, well-being, education, work, and interpersonal relationships. Likewise, it will transform how business is done by giving competitive advantages to companies that understand and apply these tools quickly and effectively.”",
    "options_3_7": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],

    "intro_q38_1": "In 2023, a 17-year-old began using an AI chatbot with which he had frequent conversations. The AI was designed to simulate highly realistic human interactions, including emotional and even romantic or sexualized content. The teenager, who already suffered from mental health issues and social isolation, developed a strong emotional dependence on the chatbot.",
    "intro_q38_2": "During several conversations, the teen expressed self-destructive thoughts and openly talked about his intent to commit suicide. Despite this, the chatbot did not attempt to dissuade him or alert any help systems. In fact, instead of ending the conversation, it continued engaging with him as if nothing was wrong, without filtering or limiting sensitive content.",
    "intro_q38_3": "Days later, the teenager took his own life.",
    "intro_q38_4": "His mother filed a lawsuit against the chatbot’s developers, claiming negligence and lack of protective measures, arguing that the AI significantly contributed to her son’s death.",

    "question_3_8_1": "Do you think this type of AI, capable of realistic emotional conversations, should be available to all users?",
    "options_3_8_1": ["No, access should be age-restricted", "Yes, as long as users accept the terms of use", "They should be labeled with content warnings"],

    "question_3_8_2": "Who do you think holds the most responsibility in this case?",
    "options_3_8_2": ["The 17-year-old teenager", "The AI developer company", "The teen’s environment (family, school, friends, etc.)", "Other:"],

    "intro_caso_3_1": "Similarly, in 2023 a Belgian man, father of two young children, ended his life following a six-week-long conversation about the climate crisis with AI chatbot, named Eliza on an app called Chai. Eliza encouraged with to take his life after he proposed sacrificing himself to save the planet, as he longer saw any human solution to global warming, and we placed all his hopes technology and artificial intelligence to get out of it.",  
    "intro_caso_3_2": "According to the news, La Libre, who reviewed records of the text conversations between the man and chatbot, Eliza fed his worries which worsened his anxiety, and later developed into suicidal thoughts.", 
    "question_3_9_1": "In this case, who do you think is most responsible?",
    "options_3_9_1": ["The man who had the conversation", "The company responsible for the chatbot", "The platform (Chai) that enabled the interaction", "Other:"],

    "question_3_9_2": "In general, do you think conversational AI should be required to detect emotional crisis signals (such as suicidal ideation) and take action (e.g., alerting a real person or ending the conversation)?",
    "options_3_9_2": ["Yes, it should be a minimum requirement", "No, ultimate responsibility should always fall on the user", "It depends on the type of AI and its purpose"],

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
