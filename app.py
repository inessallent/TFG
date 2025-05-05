import streamlit as st # type: ignore
import pandas as pd # type: ignore 
import os  
# import tempfile
import re 
# import dns.resolver
import importlib
import datetime 
from supabase import create_client, Client
from streamlit_scroll_to_top import scroll_to_here
import base64


# Create a connection object (with google sheets)
url = "https://okxrqxueywqdngrvvxrt.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9reHJxeHVleXdxZG5ncnZ2eHJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDYzMDk1MjQsImV4cCI6MjA2MTg4NTUyNH0.kkS759PQXtIME1cBT8wr4FZZGaN7w20fqIy-Om94G0Y"
supabase = create_client(url, key)

    
# Sidebar para seleccionar idioma
st.sidebar.title("Seleccionar Idioma")
idioma = st.sidebar.radio("Idioma", ["Castellano", "English", "Català"])

# Importar módulo de idioma seleccionado
idiomas_dict = {
    "Castellano": "idiomas.castellano",
    "English": "idiomas.english",
    "Català": "idiomas.catala"
}

# Cargar idioma correspondiente
modulo_idioma = importlib.import_module(idiomas_dict[idioma])
textos = modulo_idioma.textos  # Cargar los textos del idioma seleccionado

# Depuración diccionarios
# st.write("Textos cargados:", textos)

# Validar el formato del correo electrónico
def is_valid_email(email):
    # Regex que permite múltiples subdominios
    email_regex = r"^(?=.{1,256}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,24}$"
    return re.match(email_regex, email) is not None


# Save answers in New CSV
def save_response_to_gsheets(genero, correo, edad, nivel_estudios, rama_estudios, años_experiencia, pais_residencia, answers):

    # Crear nueva fila con timestamp
    nueva_respuesta = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'genero': genero,
        'correo_electronico': correo,
        'edad': edad,
        'nivel_estudios': nivel_estudios, 
        'rama_estudios': rama_estudios,
        'anos_experiencia': años_experiencia,
        'pais_residencia': pais_residencia
    }
    # Añadir las respuestas a las preguntas dinámicamente
    for i, respuesta in enumerate(answers):
        nueva_respuesta[f"pregunta_{i + 1}"] = respuesta

    # Subir la nueva respuesta a Supabase
    try:
        # Insertar la respuesta en la base de datos
        response = supabase.table("respuestas").insert([nueva_respuesta]).execute()

        # Verificar si la inserción fue exitosa
        if response.data:
            st.success(textos["enviado_con_éxtio"])
        else:
            st.error(f"{textos['error_envio']}: {response.raw_error or 'Error desconocido'}")

    
    except Exception as e:
        st.error(f"Error al guardar la respuesta: {str(e)}")  # Manejo de error en caso de falla
    # Confirmación en la interfaz
    


# Next Question
def next_section():
    st.session_state.question_index += 1
    st.session_state.selected_option = None  # Restablecer la opción seleccionada
    st.session_state.scroll_to_top = True  # Activar scroll
    st.rerun()  # Forzar la actualización inmediata de la interfaz
    
    

def next_video(question_index):
    video_path = os.path.join("Media", "Questionarios_videos", f"Q{question_index + 1}.mp4")
    if os.path.isfile(video_path):
        st.video(video_path, format="video/mp4", start_time=0)
    else:
        st.error(textos["video_no_encontrado"])

def go_back_section():
    # Guardar las respuestas actuales antes de retroceder
    if st.session_state.selected_option is not None:
        st.session_state.answers.append(st.session_state.selected_option)

    st.session_state.question_index -= 1
    st.session_state.scroll_to_top = True  # Activar scroll
    st.rerun()  # Forzar la actualización inmediata de la interfaz


#Display seccions
def display_questions(questions):
    
    if "terms_read" not in st.session_state:
        st.session_state.terms_read = False
    if "accepted_terms" not in st.session_state:
        st.session_state.accepted_terms = False
    ################################################################ Acceso al cuestionario  ################################################################ 
    if st.session_state.question_index == 1: 
        st.title("¿Quieres empezar el cuestionario?")
        
        st.write("Antes de comenzar, por favor, lee los siguientes términos y condiciones.")
        
        # # Incrustamos el documento de Google Docs (público)
        # st.markdown("""
        # <iframe src="https://docs.google.com/document/d/1-GhwIccPJfcAKDb5eIjpp8GpEt_EikjI6l-6NjJ-FSY/edit?usp=sharing"
        #         width="100%" height="500px" style="border:1px solid #ccc;"></iframe>
        # """, unsafe_allow_html=True)
        
        with open("consentiment_informat.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        # Incrustar el PDF con un iframe
        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px" type="application/pdf"></iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)

        # Botón para que el usuario confirme que ha leído el documento
        if not st.session_state.terms_read:
            if st.button("Confirmo que he leído todo el documento"):
                st.session_state.terms_read = True

        # Mostrar aceptación si ya marcó como leído
        if st.session_state.terms_read:
            accept = st.checkbox(textos["acepto_terminos"])
            if accept:
                st.session_state.accepted_terms = True

        # Mostrar botón de continuar solo si ha aceptado
        if st.session_state.accepted_terms:
            if st.button("Empezar"):
                next_section()
        else:
            st.warning("Debes leer y aceptar los términos para continuar.")
                
    ################################################################ SECTION 1: Personal Information ################################################################ 
    if st.session_state.question_index == 2:
        if 'scroll_to_top' not in st.session_state:
            st.session_state.scroll_to_top = False

        if st.session_state.scroll_to_top:
            scroll_to_here(delay=0, key="top-scroll-trigger")
            st.session_state.scroll_to_top = False
            
        st.header(textos["info_personal"])
    
        #Pregunta género
        with st.container(): 
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">{textos['pregunta_genero'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            genero_index = None
            if "genero" in st.session_state:
                genero_index = textos["genero_opciones"].index(st.session_state.genero) if st.session_state.genero else None
            st.session_state.genero = st.radio( label="", options=textos["genero_opciones"], index=genero_index , label_visibility="collapsed")
        
        #Pregunta edad
        with st.container(): 
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">{textos['pregunta_edad'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            age_index = None
            if "age" in st.session_state:
                age_index = textos["edad_opciones"].index(st.session_state.age) if st.session_state.age else None
            st.session_state.age = st.radio( label="", options=textos["edad_opciones"], index=age_index, label_visibility="collapsed")
        
        #Pregunta correo
        with st.container(): 
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">{textos['opcion_correo'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            # Restaurar respuesta si retrocede
            if "correo" in st.session_state:
                st.session_state.correo = st.text_input(textos["opcion_correo"], value=st.session_state.correo)
            else:
                st.session_state.correo = st.text_input(textos["opcion_correo"])
            
        #Pregunta nivel estudios  
        with st.container(): #Pregunta nivel estudios
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">{textos['pregunta_nivel_estudios'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            nivel_estudios_index = None
            if "nivel_estudios" in st.session_state:
                nivel_estudios_index = textos["opciones_nivel_estudios"].index(st.session_state.nivel_estudios) if st.session_state.nivel_estudios else None
            st.session_state.nivel_estudios = st.radio( label="", options=textos["opciones_nivel_estudios"], index=nivel_estudios_index, label_visibility="collapsed")
        
        with st.container(): #Pregunta rama estudios
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">{textos['pregunta_rama_estudios'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            rama_estudios_index = None
            if "rama_estudios" in st.session_state:
                rama_estudios_index = textos["opciones_rama_estudios"].index(st.session_state.rama_estudios) if st.session_state.rama_estudios else None
            st.session_state.rama_estudios = st.radio( label="", options=textos["opciones_rama_estudios"], index=rama_estudios_index, label_visibility="collapsed")
        
        with st.container(): #Pregunta años experiencia
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">{textos['pregunta_años_experiencia'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            años_experiencia_index = None
            if "años_experiencia" in st.session_state:
                años_experiencia_index = textos["opciones_años_experiencia"].index(st.session_state.años_experiencia) if st.session_state.años_experiencia else None
            st.session_state.años_experiencia = st.radio( label="", options=textos["opciones_años_experiencia"], index=años_experiencia_index, label_visibility="collapsed")
        
        with st.container():
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">{textos['pregunta_pais_residencia'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            # Restaurar respuesta si retrocede
            pais_residencia_index = None
            if "pais_residencia" in st.session_state:
                pais_residencia_index = (
                    ["Alemania", "Argentina", "Brasil", "Bulgaria", "Canadá", "Chile", "China", "Colombia", "Ecuador", "España", "Estados Unidos", "Francia", "Honduras", "India", "Japón", "Marruecos", "México", "Pakistán", "Paraguay", "Perú", "Portugal", "Rusia", "Reino Unido", "Ucrania", "Venezuela", "Otro"]
                    .index(st.session_state.pais_residencia) if st.session_state.pais_residencia else None
                )
            
            st.session_state.pais_residencia = st.selectbox(textos["pregunta_pais_residencia"], ["Alemania", "Argentina", "Brasil", "Bulgaria", "Canadá", "Chile", "China", "Colombia", "Ecuador", "España", "Estados Unidos", "Francia", "Honduras", "India", "Japón", "Marruecos", "México", "Pakistán", "Paraguay", "Perú", "Portugal", "Rusia", "Reino Unido", "Ucrania", "Venezuela", "Otro"], index=pais_residencia_index, label_visibility="collapsed")
    


        if st.button(textos["boton_continuar"]):
            errores = []
            
            
            if not st.session_state.genero:
                errores.append(textos["error_genero"])
            
            if not st.session_state.age:
                errores.append(textos["error_age"])
                
            # if st.session_state.correo and not is_valid_email(st.session_state.correo):
            #     errores.append(textos["error_correo"])  # Formato inválido 
            
            if not st.session_state.nivel_estudios:
                errores.append(textos["error_nivel_estudios"])
            
            if not st.session_state.rama_estudios:
                errores.append(textos["error_rama_estudios"])
                
            if not st.session_state.años_experiencia:
                errores.append(textos["error_años_experiencia"])
            
            if not st.session_state.pais_residencia:
                errores.append(textos["error_pais_residencia"])
            
            
            if errores:
                for error in errores:
                    st.warning(error)
                return #Deter ejecucion si hay errores
                
            else:
                st.session_state.personal_data = {
                    "genero": st.session_state.genero,
                    "correo": st.session_state.correo,
                    "edad": st.session_state.age,
                    "nivel_estudios": st.session_state.nivel_estudios,
                    "rama_estudios": st.session_state.rama_estudios,
                    "años_experiencia": st.session_state.años_experiencia,
                    "pais_residencia": st.session_state.pais_residencia
                }
            
            next_section()  # Avanzamos a la siguiente sección
    
    ################################################################ SECTION 2: (Knowledge about AI) ################################################################ 

    elif st.session_state.question_index == 3:
        if 'scroll_to_top' not in st.session_state:
            st.session_state.scroll_to_top = False

        if st.session_state.scroll_to_top:
            scroll_to_here(delay=0, key="top-scroll-trigger")
            st.session_state.scroll_to_top = False
            
        st.header(textos["Seccion_2"])
                
        with st.container(): #Pregunta 2_1
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">{textos['pregunta_2_1'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            q21_index = None
            if "q21" in st.session_state:
                q21_index = textos["opciones_2_1"].index(st.session_state.q21) if st.session_state.q21 else None
            st.session_state.q21 = st.radio( label="", options=textos["opciones_2_1"], index=q21_index , label_visibility="collapsed")
            
        
        with st.container(): #Pregunta 2_2
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">{textos['pregunta_2_2'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            q22_index = None
            if "q22" in st.session_state:
                q22_index = textos["opciones_2_2"].index(st.session_state.q22) if st.session_state.q22  else None
            st.session_state.q22 = st.radio(label="", options=textos["opciones_2_2"], index=q22_index, label_visibility="collapsed")

        with st.container(): #Pregunta 2_3
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">{textos['pregunta_2_3'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            seleccionadas_q23 = []
            for opcion in textos["opciones_2_3"]:
                if st.checkbox(opcion, key=f"q23_{opcion}"):
                    seleccionadas_q23.append(opcion)
            st.session_state.q23 = seleccionadas_q23
        
        with st.container(): #Pregunta 2_4
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">{textos['pregunta_2_4'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            q24_index = None
            if "q24" in st.session_state:
                q24_index = textos["opciones_2_4"].index(st.session_state.q24) if st.session_state.q24 else None
            st.session_state.q24 = st.radio(label="", options=textos["opciones_2_4"], index=q24_index, label_visibility="collapsed")

        with st.container(): #Pregunta 2_5
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">{textos['pregunta_2_5'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            q25_index = None
            if "q25" in st.session_state:
                q25_index = textos["opciones_2_5"].index(st.session_state.q25) if st.session_state.q25  else None
            st.session_state.q25 = st.radio(label="", options=textos["opciones_2_5"], index=q25_index, label_visibility="collapsed")

            
        with st.container(): #Pregunta 2_6
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">{textos['pregunta_2_6'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            q26_index = None
            if "q26" in st.session_state:
                q26_index = textos["opciones_2_6"].index(st.session_state.q26) if st.session_state.q26  else None
            st.session_state.q26 = st.radio(label="", options=textos["opciones_2_6"], index=q26_index, label_visibility="collapsed")


        with st.container(): #Pregunta 2_7
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">{textos['pregunta_2_7'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            
            q27_index = None
            if "q27" in st.session_state:
                q27_index = textos["opciones_2_7"].index(st.session_state.q27) if st.session_state.q27  else None
            st.session_state.q27 = st.radio(label="", options=textos["opciones_2_7"], index=q27_index, label_visibility="collapsed")

                    
        if st.button(textos["boton_continuar"], key="btn_sec2"):
            if (
                st.session_state.q21 is None or
                st.session_state.q22 is None or
                st.session_state.q24 is None or
                st.session_state.q25 is None or
                st.session_state.q26 is None or
                st.session_state.q27 is None  
                
            ):
                st.warning(textos["selecciona_opción"])
            else:
                st.session_state.answer_sec_2 = {
                    "Pregunta 6": st.session_state.q21,
                    "Pregunta 7": st.session_state.q22,
                    "Pregunta 8": st.session_state.q23,
                    "Pregunta 9": st.session_state.q24,
                    "Pregunta 10": st.session_state.q25,
                    "Pregunta 11": st.session_state.q26,
                    "Pregunta 12": st.session_state.q27,
                    
                }
                st.session_state.answers.extend([
                    st.session_state.q21, 
                    st.session_state.q22, 
                    st.session_state.q23, 
                    st.session_state.q24, 
                    st.session_state.q25, 
                    st.session_state.q26, 
                    st.session_state.q27
                ])

                next_section()
                
        if st.button(textos["boton_atras"]):
            go_back_section()


    ################################################################ SECTION 3 ################################################################ 

    elif st.session_state.question_index == 4:
        if 'scroll_to_top' not in st.session_state:
            st.session_state.scroll_to_top = False

        if st.session_state.scroll_to_top:
            scroll_to_here(delay=0, key="top-scroll-trigger")
            st.session_state.scroll_to_top = False
        
        st.header(textos["Seccion_3"])

        # answer_q31 = st.radio("Hola buenos días", SCALE_OPTIONS, index=None, key="q31", horizontal=True)
        
        # answer_q32 = st.radio("Hola buenos días 2", SCALE_OPTIONS, index=None, key="q32", horizontal=True)
        
        st.markdown(f"<p style='font-size: 1.05rem; color: #2c2c2c;  text-align: justify; margin-bottom: 0.8rem;'>{textos['intro_q33']}</p>", unsafe_allow_html=True)
        with st.container(): #Pregunta 3_3
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">{textos['pregunta_3_3'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            q33_index = None
            if "q33" in st.session_state:
                q33_index = textos["opciones_3_3"].index(st.session_state.q33) if st.session_state.q33 else None
            st.session_state.q33 = st.radio(label="", options=textos["opciones_3_3"], index=q33_index, label_visibility="collapsed")

        st.markdown(f"<p style='font-size: 1.05rem; color: #2c2c2c;  text-align: justify; margin-bottom: 0.8rem;'>{textos['intro_q34']}</p>", unsafe_allow_html=True)
        with st.container(): #Pregunta 3_4
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">{textos['pregunta_3_4'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            q34_index = None
            if "q34" in st.session_state:
                q34_index = textos["opciones_3_4"].index(st.session_state.q34) if st.session_state.q34 else None
            st.session_state.q34 = st.radio(label="", options=textos["opciones_3_4"], index=q34_index, label_visibility="collapsed")

        with st.container(): #Pregunta 3_5
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">{textos['pregunta_3_5'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            q35_index = None
            if "q35" in st.session_state:
                q35_index = textos["opciones_3_5"].index(st.session_state.q35) if st.session_state.q35 else None
            st.session_state.q35 = st.radio(label="", options=textos["opciones_3_5"], index=q35_index, label_visibility="collapsed")

        with st.container(): #Pregunta 3_6
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">{textos['pregunta_3_6'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            q36_index = None
            if "q36" in st.session_state:
                q36_index = textos["opciones_3_6"].index(st.session_state.q36) if st.session_state.q36 else None
            st.session_state.q36 = st.radio(label="q36", options=textos["opciones_3_6"], index=q36_index, label_visibility="collapsed")

        with st.container(): #Pregunta 3_7
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">{textos['pregunta_3_7'].replace("**", "")}</p>
                </div>
                """,unsafe_allow_html=True)
            q37_index = None
            if "q37" in st.session_state :
                q37_index = textos["opciones_3_7"].index(st.session_state.q37) if st.session_state.q37 else None
            st.session_state.q37 = st.radio(label="q37", options=textos["opciones_3_7"], index=q37_index, label_visibility="collapsed")


        if st.button(textos["boton_enviar"], key="btn_sec3"):
            if (
                # st.session_state.q31 is None or
                # st.session_state.q32 is None or
                st.session_state.q33 is None or
                st.session_state.q34 is None or
                st.session_state.q35 is None or
                st.session_state.q36 is None or
                st.session_state.q37 is None
            ):
                st.warning(textos["selecciona_opción"])
            else:
                st.session_state.answer_sec_3 = {
                    # "Pregunta 11": st.session_state.q31,
                    # "Pregunta 12": st.session_state.q32,
                    "Pregunta 13": st.session_state.q33,
                    "Pregunta 14": st.session_state.q34,
                    "Pregunta 15": st.session_state.q35,
                    "Pregunta 16": st.session_state.q36,
                    "Pregunta 17": st.session_state.q37,
                }
                st.session_state.answers.extend([
                    
                    # st.session_state.q31,
                    # st.session_state.q32,
                    st.session_state.q33,
                    st.session_state.q34,
                    st.session_state.q35,
                    st.session_state.q36,
                    st.session_state.q37,
                ])

                next_section()
                
        if st.button(textos["boton_atras"]):
            go_back_section()

    
def cuestions():
    
    # Inicializar el estado de la sesión si no existe
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 1
    
    
    if 'answers' not in st.session_state:
        st.session_state.answers = []
        
    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = None
        


    seccion_lens = 4 # Apartados de preguntas
        
    # Mostrar la pregunta actual
    if st.session_state.question_index - 1 < seccion_lens:
        display_questions(st.session_state.question_index)
    else:
        st.write(textos["Gracias_por_contestar_el_formulario"])

        # Guardar todas las respuestas acumuladas al final
        if 'personal_data' in st.session_state:
            personal_data = st.session_state.personal_data
            
            # st.write("Datos personales guardados:", st.session_state.personal_data) #Depuración
            
            save_response_to_gsheets(
                personal_data["genero"],
                personal_data["correo"],
                personal_data["edad"],
                personal_data["nivel_estudios"],
                personal_data["rama_estudios"], 
                personal_data["años_experiencia"],
                personal_data["pais_residencia"],
                st.session_state.answers
            )

            # Limpiar las respuestas después de guardarlas
            st.session_state.answers = []
            st.session_state.question_index = 1  # Resetear al inicio            

# Aplicar estilos CSS personalizados
st.markdown(
    """
    <style>
    
        /* Cambiar el color de la flecha que abre/cierra el sidebar */
        [data-testid="collapsedControl"] {
            color: #007BFF !important; /* Azul */
        }
        
        /* Cambiar el color del texto en el sidebar */
        .css-1d391kg {
            color: white !important;
        }
        
        # /* Cambiar el color de fondo del sidebar */
        # section[data-testid="stSidebar"] {
        #     background-color: #4A90E2;
        # }

        # /* Cambiar color de la flecha del selectbox */
        # div[data-baseweb="select"] svg {
        #     fill: #007BFF !important; /* Azul */
        # }

    </style>
    """,
    unsafe_allow_html=True
)


def main():  
    
    # Sidebar para la navegación
    st.sidebar.title(textos["navegacion"]) #Title 
    # UPF_logo_path = os.path.join("Media", "Logos", "UPF_logo.png")
    # st.sidebar.image(UPF_logo_path)  #Upload Logo
    page_web = st.sidebar.selectbox(textos["selecciona_una_seccion"], [textos["cuestionario"], textos["sobre_nosotros"], textos["contacto"]])


    #Cuestionario
    if page_web == textos["cuestionario"]:
        cuestions()            
    
    #Sobre Nosotros   
    elif page_web == textos["sobre_nosotros"]:
        st.title(textos["sobre_nosotros"])
        st.write(textos["info_sobre_nosotros"])

    #Contacto 
    elif page_web == textos["contacto"]:
        st.title(textos["contacto"])
        st.write(textos["info_contacto"])
        email = st.text_input(textos["correo_electronico_contacto"])
        mensaje = st.text_area(textos["mensaje"])
        if st.button(textos["enviar"]):
            st.success(textos["mensaje_enviado"])


if __name__ == "__main__":
    main() 
