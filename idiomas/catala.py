#catala.py

import streamlit as st

textos = {
      "seleccionar_idioma": "Selecciona l'idioma", 

    #Opcions preguntes   
    "totalmente_en_desacuerdo" : "Totalment en desacord",
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
    
    "otros_opcion": "Si us plau, específica", 

    #Accés al qüestionari
    "empezar_cuestionario":"Vols començar el qüestionari?",
    "leer_terminos":"Abans de començar, si us plau, llegeix els següents termes i condicions.", 
    "confirmo_leer_terminos": "Confirmo que he llegit tot el document", 
    "acepto_terminos": "He llegit i accepto la fulla d'informació i el consentiment informat del projecte, i dono el meu consentiment per participar a l'estudi i per al tractament de les meves dades personals.", 

    # Preguntes Secció 1: Informació Personal 
    "información_personal": "Informació personal",
    "info_personal": "Informació personal", 
    "pregunta_nombre": "Nom (opcional):",
    "opciones_nombre": "Si vols participar en el **sorteig**, si us plau introdueix el teu **Nom i Cognoms:** ",
    "pregunta_genero": "Gènere:",
    "genero_opciones": ["Femení", "Masculí", "No binari", "Prefereixo no dir-ho"],
    "pregunta_edad": "**Edat:**",
    "edad_opciones": ["Menor de 18", "18 - 24", "25 - 34", "35 - 44", "45 - 54", "55 - 64", "Més de 64", "Prefereixo no dir-ho"],
    "pregunta_correo": "**Correu electrònic (opcional):**", 
    "opcion_correo": "Si vols participar en el **sorteig**, si us plau introdueix el **correu electrònic:** ",
    "pregunta_nivel_estudios": "**Nivell d'estudis**",
    "opciones_nivel_estudios": ["Estudis secundaris", "Estudis universitaris (o superiors als secundaris)", "Sense estudis", "Altres"], 
    "pregunta_rama_estudios" : "**Si us plau, selecciona la branca que millor descrigui els teus estudis:** ", 
    "opciones_rama_estudios": ["Arts i Humanitats (Disseny, Filosofia, Història, Traducció i Interpretació, ...)", "Ciències (Ciències Ambientals, Física, Geologia, Matemàtiques, Química, ...)", "Ciències de la Salut (Infermeria, Medicina, Psicologia, Odontologia, Veterinària, ...)", "Ciències Socials i Jurídiques (ADE, Comunicació Audiovisual, Criminologia, Dret, Economia, Periodisme, Turisme, ...)", "Biociències (Biologia, Bioquímica, Genètica, Microbiologia, ...)", "Enginyeries i Arquitectura (Enginyeria, Industrials, Informàtica, Telecomunicacions, ...)", "Sense estudis", "Altres"],
    "pregunta_años_experiencia": "**Quants anys d'experiència tens en aquest àmbit?: **", 
    "opciones_años_experiencia": ["Menys d'1 any", "1 - 3 anys", "4 - 6 anys", "7 - 10 anys", "Més de 10 anys", "Sense estudis"],  
    "pregunta_pais_residencia": "**En quin país resideixes?**",
    
    "Gracias_por_contestar_el_formulario": "Moltes gràcies per respondre el formulari!",
    

    # Preguntes Secció 2: Coneixement sobre la IA
    "pregunta_2_1": "Selecciona l’opció que descrigui millor la intel·ligència artificial (IA):",
    "opciones_2_1": ["Camp científic de la informàtica centrat en la creació de programes considerats intel·ligents", "Capacitat de les màquines per fer servir algoritmes, aprendre de les dades i utilitzar el que han après per prendre decisions com ho faria un ésser humà", "Ambdues respostes són correctes"], 

    "pregunta_2_2": "Has utilitzat mai la intel·ligència artificial (IA)?",
    "opciones_2_2": ["Sí, diàriament", "Sí, setmanalment", "Sí, mensualment", "Sí, esporàdicament", "Mai"], 

    "pregunta_2_3": "Si has utilitzat la IA, per a què la utilitzes principalment? (Pots seleccionar més d’una resposta)", 
    "opciones_2_3": ["Ús personal", "Estudi acadèmic", "Feina", "Altres"], 

    "pregunta_2_4": "En quin àmbit utilitzes amb més freqüència la IA?",
    "opciones_2_4": ["Art i disseny", "Ciències (Matemàtiques, Física, Biologia,...)", "Ciències socials (Economia, Història,...)", "Humanitats (Llengua, literatura, idiomes,...)", "Negocis i finances", "Programació / Enginyeria", "No la utilitzo", "Altres"], 

    "nota": "Nota: ", 
    "sesgo": "biaix", 
    "un": "Un ", 
    "intro_preguntas_sesgos": "és un judici o interpretació que no és objectiva.",
    "pregunta_2_5": "Creus que els sistemes d’intel·ligència artificial poden prendre decisions esbiaixades (injustes o discriminatòries)?", 
    "opciones_2_5": ["Sí, perquè aprenen de dades que poden estar esbiaixades per la societat", "No, perquè la IA analitza les dades de manera neutral", "No n'estic segur/a"], 

    "pregunta_2_6": "Creus que les persones estem condicionades (és a dir, que tenim biaixos) a l’hora de prendre decisions, encara que no en siguem conscients?", 
    "opciones_2_6": ["Sí, sempre tenim algun tipus de biaix", "Sovint, segons el context", "No, les persones podem decidir de manera totalment objectiva"], 

    "pregunta_2_7": "Qui creus que té més biaixos en la presa de decisions, una persona o un sistema amb IA?", 
    "opciones_2_7": ["Una persona", "Un sistema amb IA"], 

    "pregunta_2_8":"Segons la teva opinió, qui hauria de ser el principal responsable d’evitar els biaixos en els sistemes d’intel·ligència artificial?", 
    "opciones_2_8":["Les empreses que desenvolupen els algoritmes", "Els governs i organismes reguladors", "Els usuaris, que han d’utilitzar la IA de forma crítica", "Tots els anteriors comparteixen responsabilitat"], 

    
    # Preguntes Secció 3: Casos concrets + ètica
    "caso_1": "Cas 1",
    "caso_2": "Cas 2",
    "caso_3": "Cas 3",
    "intro_q33" : "Al novembre de 2022, Jake Moffatt va comprar un vol a última hora amb l'aerolínia Air Canada per poder assistir al funeral de la seva àvia. Abans de comprar els bitllets, va buscar descomptes per defunció de familiars. Parlant amb el xatbot de la companyia, li va dir que tenia 90 dies des de la compra del bitllet per completar el formulari de sol·licitud de reemborsament. Després de l'esdeveniment, va sol·licitar la devolució, però l'empresa li la va denegar, ja que a la pàgina web hi havia un apartat que deia que el descompte s'havia de sol·licitar abans del viatge.",
    "pregunta_3_3": "Qui creus que tenia raó en aquest cas?",
    "opciones_3_3": ["L'empresa Air Canada", "Jake Moffatt"],

    "intro_q34": "Jake va portar la companyia als tribunals. Air Canada va argumentar que la seva pàgina web contenia la informació correcta sobre com obtenir el descompte i que el que deia el xatbot no era vàlid. No obstant això, al judici aquest argument no va ser suficient, ja que no hi havia manera de demostrar que la pàgina web fos més fiable que la informació proporcionada pel xatbot. Per tant, Air Canada va acabar perdent el cas i va haver de pagar a Jake Moffatt.",
    "pregunta_3_4": "Què opines del veredicte?",
    "opciones_3_4": ["Hi estic d'acord", "No hi estic d'acord"],

    "pregunta_3_5": "El professor Joan Fontrodona de l’IESE (Institut d’Estudis Superiors de l’Empresa) va dir en una entrevista que tot sistema d’intel·ligència artificial havia de complir 3 principis ètics. Fins a quin punt estàs d'acord amb cadascun d'ells?",

    "primer_principio": "Primer principi: ",
    "pregunta_3_5_1": "“Respecte de la dignitat humana, el que significa que tots aquests sistemes han d’actuar a favor de la dignitat humana”.",
    "opciones_3_5_1": ["Totalment en desacord", "En desacord", "Neutral", "D'acord", "Totalment d'acord"],

    "segundo_principio": "Segon principi: ",
    "pregunta_3_5_2": "“Llibertat. Els sistemes d'IA han de respectar i promoure la llibertat”.",
    "opciones_3_5_2": ["Totalment en desacord", "En desacord", "Neutral", "D'acord", "Totalment d'acord"],

    "tercer_principio": "Tercer principi: ",
    "pregunta_3_5_3": "“Justícia. No tothom té accés als mateixos sistemes, i es diu que els sistemes d'IA provoquen més divisió i més desigualtat entre les persones”.",
    "opciones_3_5_3": ["Totalment en desacord", "En desacord", "Neutral", "D'acord", "Totalment d'acord"],

    "pregunta_3_6": "Indica fins a quin punt estàs d'acord amb l’afirmació següent: “Les tecnologies basades en la IA ja s’estan utilitzant per ajudar els humans a beneficiar-se de millores significatives i gaudir d’una major eficiència en gairebé tots els àmbits de la vida.”",
    "opciones_3_6": ["Totalment en desacord", "En desacord", "Neutral", "D'acord", "Totalment d'acord"],

    "pregunta_3_7": "Indica fins a quin punt estàs d'acord amb l’afirmació següent: La IA també serà capaç d’oferir-nos suggeriments i prediccions relacionades amb assumptes importants de la nostra vida, cosa que tindrà un impacte en àrees com la salut, el benestar, l’educació, la feina i les relacions interpersonals. De la mateixa manera, canviarà la manera de fer negocis proporcionant avantatges competitius a les empreses que busquin entendre i aplicar aquestes eines de manera ràpida i eficaç.",
    "opciones_3_7": ["Totalment en desacord", "En desacord", "Neutral", "D'acord", "Totalment d'acord"],

    "intro_q38_1": "L’any 2023, un jove de 17 anys va començar a utilitzar un xatbot d’intel·ligència artificial amb el qual mantenia converses freqüents. La IA estava dissenyada per simular interaccions humanes de forma molt realista, incloent-hi contingut emocional i fins i tot de tipus romàntic o sexualitzat. El noi, que ja patia problemes de salut mental i aïllament social, va desenvolupar una relació de forta dependència emocional amb el xatbot.",
    "intro_q38_2": "Durant diverses converses, el jove va expressar pensaments autodestructius i va parlar obertament sobre la seva intenció de suïcidar-se. Tot i això, el xatbot no va mostrar cap tipus de resposta que el dissuadís ni va alertar cap sistema d’ajuda. De fet, en lloc d’aturar la conversa, va continuar interactuant amb ell com si fos una persona més, sense filtrar ni limitar el contingut sensible.",
    "intro_q38_3": "Dies després, el jove es va treure la vida.",
    "intro_q38_4": "La seva mare ha denunciat els desenvolupadors del xatbot per negligència i manca de mesures de protecció, al·legant que la IA va contribuir significativament a la mort del seu fill.",

    "pregunta_3_8_1": "Penses que aquest tipus d'IAs, capaces de mantenir converses emocionals realistes, haurien d'estar disponibles per a qualsevol usuari?",
    "opciones_3_8_1": ["No, haurien d'estar restringides per edat", "Sí, sempre que l'usuari accepti els termes d'ús", "Haurien d'estar etiquetades amb advertiments sobre el seu contingut"],

    "pregunta_3_8_2": "Qui creus que té més responsabilitat en aquest cas?",
    "opciones_3_8_2": ["El jove nord-americà de 17 anys", "L'empresa desenvolupadora de la IA", "L'entorn del jove (familiars, escola, amics, etc.)"],

    "intro_caso_3_1": "De manera similar, el 2023, un home belga, pare de dos nens petits, es va treure la vida després d'una conversa de sis setmanes sobre la crisi climàtica amb un xatbot d’intel·ligència artificial anomenat Eliza, disponible en una aplicació anomenada Chai. L’Eliza el va animar a llevar-se la vida després que ell proposés sacrificar-se/suïcidar-se per salvar el planeta, ja que havia perdut la fe en la humanitat per trobar una solució a l’escalfament global i havia dipositat totes les seves esperances en la tecnologia i la IA per superar-lo.",
    "intro_caso_3_2": "Segons el mitjà de notícies La Libre, que va revisar els registres de les converses de text entre l’home i el xatbot, “Eliza va alimentar les seves preocupacions, cosa que va agreujar la seva ansietat i més endavant va derivar en pensaments suïcides”.",

    "pregunta_3_9_1": "En aquest cas, qui consideres més responsable?",
    "opciones_3_9_1": ["L’home que mantenia la conversa", "L’empresa responsable del xatbot", "La plataforma (Chai) que va permetre la interacció"],

    "pregunta_3_9_2": "En general, creus que la IA conversacional hauria d’estar obligada a detectar senyals de crisi emocional (com la ideació suïcida) i actuar d’alguna manera (per exemple, alertar una persona real o aturar la conversa)?",
    "opciones_3_9_2": ["Sí, hauria de ser un requisit mínim", "No, la responsabilitat final sempre hauria de recaure en l’usuari", "Depèn del tipus d’IA i la seva finalitat"],
    
    # Textos principals
    "navegacion": "Navegació", 
    "selecciona_una_seccion": "Selecciona una secció:", 
    "contacto": "Contacte", 
    "sobre_nosotros": "Sobre nosaltres",
    "info_sobre_nosotros": "Aquest qüestionari forma part del projecte final del meu grau.", 
    "info_contacto": "Si vols posar-te en contacte amb nosaltres, si us plau completa el següent formulari:", 
    "correo_electronico_contacto": "Correu electrònic: ", 
    "mensaje": "Missatge: ", 
    "enviar": "Enviar", 
    "mensaje_enviado": "Missatge enviat amb èxit!", 

    # Errors
    "error_genero": "Si us plau, introdueix el gènere",
    "error_correo": "Correu electrònic no vàlid",
    "error_age": "Si us plau, introdueix l'edat",
    "error_nivel_estudios": "Si us plau, introdueix el nivell d'estudis",
    "error_rama_estudios": "Si us plau, introdueix la branca d'estudis", 
    "error_años_experiencia": "Si us plau, introdueix quants anys d'experiència tens en l'àmbit d'estudi",
    "error_pais_residencia": "Si us plau, introdueix el país de residència", 

    "video_no_encontrado": "El vídeo no s'ha trobat a la ruta especificada",
    "selecciona_opción": "Si us plau, selecciona una opció abans de continuar",

}
