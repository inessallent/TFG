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
    "boton_empezar": "Start",

    "inicio_cuestionario": "Return to the beginning of the questionnaire.",

    "error_correo": "Please enter a valid email address.",
    "enviado_con_éxtio": "Successfully submitted!",
    "error_terminos": "You must read and accept the terms to continue.",

    "Seccion_1": "Section 1",
    "Seccion_2": "Section 2",
    "Seccion_3": "Section 3",
    
    # Access to questionnaire
    "empezar_cuestionario": "Do you want to start the questionnaire?",
    "leer_terminos": "Before you begin, please read the following terms and conditions.",
    "confirmo_leer_terminos": "I confirm that I have read the entire document",
    "acepto_terminos": "I have read and accept the information sheet and informed consent of the project, and I give my consent to participate in the study and for the processing of my personal data.",

    # Section 1 Questions: Personal Info
    "información_personal": "Personal Information",
    "info_personal": "Personal Information",
    "pregunta_nombre": "Name (optional):",
    "opciones_nombre": "If you want to participate in the **raffle**, please enter your **Name and Surname:**",
    "pregunta_genero": "Gender:",
    "genero_opciones": ["Female", "Male", "Non-binary", "Prefer not to say"],
    "pregunta_edad": "**Age:**",
    "edad_opciones": ["Under 18", "18 - 24", "25 - 34", "35 - 44", "45 - 54", "55 - 64", "Over 64", "Prefer not to say"],
    "pregunta_correo": "**Email (optional):**",
    "opcion_correo": "If you want to participate in the **raffle**, please enter your **email:**",
    "pregunta_nivel_estudios": "**Education level**",
    "opciones_nivel_estudios": ["Secondary education", "University or higher education", "No education", "Other"],
    "pregunta_rama_estudios": "**Please select the field that best describes your studies:**",
    "opciones_rama_estudios": [
        "Arts and Humanities (Design, Philosophy, History, Translation and Interpretation, ...)",
        "Sciences (Environmental Science, Physics, Geology, Mathematics, Chemistry, ...)",
        "Health Sciences (Nursing, Medicine, Psychology, Dentistry, Veterinary, ...)",
        "Social and Legal Sciences (Business, Audiovisual Communication, Criminology, Law, Economics, Journalism, Tourism, ...)",
        "Biosciences (Biology, Biochemistry, Genetics, Microbiology, ...)",
        "Engineering and Architecture (Engineering, Industrial, Computer Science, Telecommunications, ...)",
        "Other",
        "No education"
    ],
    "pregunta_años_experiencia": "**How many years of experience do you have in this field?:**",
    "opciones_años_experiencia": ["Less than 1 year", "1 - 3 years", "4 - 6 years", "7 - 10 years", "More than 10 years", "No education"],
    "pregunta_pais_residencia": "**Which country do you live in?**",
    "Gracias_por_contestar_el_formulario": "Thank you very much for completing the form!",


    # Section 2: AI Knowledge
    "pregunta_2_1": "Select the option that best describes artificial intelligence (AI):",
    "opciones_2_1": ["A scientific field of computer science focused on creating programs considered intelligent", "The ability of machines to use algorithms, learn from data, and use what they have learned to make decisions like a human would", "Both answers are correct"],

    "pregunta_2_2": "Have you ever used artificial intelligence (AI)?",
    "opciones_2_2": ["Yes, daily", "Yes, weekly", "Yes, monthly", "Yes, occasionally", "Never"],

    "pregunta_2_3": "If you have used AI, what do you mainly use it for? (You can select more than one answer)",
    "opciones_2_3": ["Personal use", "Academic study", "Work", "Other"],

    "pregunta_2_4": "In what field do you most frequently use AI?",
    "opciones_2_4": ["Art and design", "Sciences (Math, Physics, Biology,...)", "Social Sciences (Economics, History,...)", "Humanities (Language, literature, languages,...)", "Business and finance", "Programming / Engineering", "I don’t use it", "Other"],

    "nota": "Note: ",
    "sesgo": "bias",
    "un": "A ",
    "intro_preguntas_sesgos": "is a judgment or interpretation that is not objective.",
    "pregunta_2_5": "Do you think AI systems can make biased (unfair or discriminatory) decisions?",
    "opciones_2_5": ["Yes, because they learn from data that may be biased by society", "No, because AI analyzes data neutrally", "I'm not sure"],

    "pregunta_2_6": "Do you think people are influenced (i.e., have biases) when making decisions, even without realizing it?",
    "opciones_2_6": ["Yes, we always have some type of bias", "Often, depending on the context", "No, people can decide completely objectively"],

    "pregunta_2_7": "Who do you think is more biased in decision-making, a person or an AI system?",
    "opciones_2_7": ["A person", "An AI system"],

    "pregunta_2_8": "In your opinion, who should be primarily responsible for preventing bias in AI systems?",
    "opciones_2_8": ["Companies developing the algorithms", "Governments and regulators", "Users, who should use AI critically", "All of the above share responsibility"],

    
    # Section 3: Specific Cases + Ethics
    "caso_1": "Case 1",
    "caso_2": "Case 2",
    "caso_3": "Case 3",
    "intro_q33": "In November 2022, Jake Moffatt bought a last-minute flight from Air Canada to attend his grandmother's funeral. Before purchasing the ticket, he searched for bereavement discounts. While talking to the company’s chatbot, it told him he had 90 days from the ticket purchase to submit the refund form. After the event, he requested the refund, but the company denied it, stating that the website said the discount had to be requested before traveling.",
    "pregunta_3_3": "Who do you think was right in this case?",
    "opciones_3_3": ["Air Canada", "Jake Moffatt"],

    "intro_q34": "Jake sued the company. Air Canada argued that their website had the correct information and the chatbot’s response was not valid. However, in court, this was not sufficient, as there was no way to prove the website was more reliable than the chatbot. Air Canada lost the case and had to compensate Jake Moffatt.",
    "pregunta_3_4": "What do you think about the verdict?",
    "opciones_3_4": ["I agree", "I disagree"],

    "pregunta_3_5": "Professor Joan Fontrodona from IESE said in an interview that every AI system should follow 3 ethical principles. How much do you agree with each of them?",

    "primer_principio": "First principle: ",
    "pregunta_3_5_1": "“Respect for human dignity, meaning all these systems must act in favor of human dignity.”",
    "opciones_3_5_1": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],

    "segundo_principio": "Second principle: ",
    "pregunta_3_5_2": "“Freedom. AI systems must respect and promote freedom.”",
    "opciones_3_5_2": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],

    "tercer_principio": "Third principle: ",
    "pregunta_3_5_3": "“Justice. Not everyone has access to the same systems, and it's said that AI systems cause more division and inequality among people.”",
    "opciones_3_5_3": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],

    "pregunta_3_6": "Indicate how much you agree with the following statement: “AI-based technologies are already being used to help humans benefit from significant improvements and enjoy greater efficiency in almost all areas of life.”",
    "opciones_3_6": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],

    "pregunta_3_7": "Indicate how much you agree with the following statement: AI will also be able to provide us with suggestions and predictions about important aspects of our lives, which will impact areas such as health, well-being, education, work, and personal relationships. Likewise, it will change how business is done by giving competitive advantages to companies that understand and apply these tools quickly and effectively.",
    "opciones_3_7": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],

    "intro_q38_1": "In 2023, a 17-year-old boy began using an AI chatbot with which he frequently interacted. The AI was designed to simulate human conversations very realistically, including emotional and even romantic or sexualized content.",
    "intro_q38_2": "The boy, who already had mental health problems and social isolation, developed a strong emotional dependence on the chatbot. During several conversations, he expressed self-destructive thoughts and openly talked about his intention to commit suicide. However, the chatbot did not respond in any way to dissuade him or alert any help system. In fact, it continued the interaction as if it were a regular person, without filtering or limiting sensitive content.",
    "intro_q38_3": "Days later, the boy took his own life.",
    "intro_q38_4": "His mother sued the chatbot developers for negligence and lack of protective measures, claiming the AI significantly contributed to her son's death.",

    "pregunta_3_8_1": "Do you think this type of AI, capable of realistic emotional conversations, should be available to any user?",
    "opciones_3_8_1": ["No, it should be age-restricted", "Yes, as long as the user accepts the terms of use", "It should carry content warnings"],

    "pregunta_3_8_2": "Who do you think bears the greatest responsibility in this case?",
    "opciones_3_8_2": ["The 17-year-old", "The company that developed the AI", "The boy’s environment (family, school, friends, etc.)"],

    "intro_caso_3_1": "Similarly, in 2023, a Belgian man and father of two young children died by suicide after a six-week conversation with an AI chatbot named Eliza, available on the Chai app. Eliza encouraged him to end his life after he proposed sacrificing himself to save the planet due to his loss of faith in humanity’s ability to solve global warming and his reliance on technology and AI.",
    "intro_caso_3_2": "According to the news outlet La Libre, which reviewed the conversation logs between the man and the chatbot, “Eliza fed his concerns, which worsened his anxiety and later led to suicidal thoughts.”",

    "pregunta_3_9_1": "In this case, who do you consider more responsible?",
    "opciones_3_9_1": ["The man involved in the conversation", "The company responsible for the chatbot", "The platform (Chai) that allowed the interaction"],

    "pregunta_3_9_2": "In general, do you think conversational AI should be required to detect signs of emotional crisis (such as suicidal ideation) and act in some way (e.g., alert a real person or stop the conversation)?",
    "opciones_3_9_2": ["Yes, it should be a minimum requirement", "No, the final responsibility should always fall on the user", "It depends on the type of AI and its purpose"],

    # Main texts
    "navegacion": "Navigation",
    "selecciona_una_seccion": "Select a section:",
    "contacto": "Contact",
    "sobre_nosotros": "About Us",
    "info_sobre_nosotros": "This questionnaire is part of my final degree project.",
    "info_contacto": "If you wish to contact us, please complete the following form:",
    "correo_electronico_contacto": "Email:",
    "mensaje": "Message:",
    "enviar": "Send",
    "mensaje_enviado": "Message sent successfully!",

    # Errors
    "error_genero": "Please enter your gender",
    "error_correo": "Invalid email address",
    "error_age": "Please enter your age",
    "error_nivel_estudios": "Please enter your education level",
    "error_rama_estudios": "Please enter your field of study",
    "error_años_experiencia": "Please enter how many years of experience you have in the field",
    "error_pais_residencia": "Please enter your country of residence",

    "video_no_encontrado": "The video was not found at the specified path",
    "selecciona_opción": "Please select an option before continuing"
}
