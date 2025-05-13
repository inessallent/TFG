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
import streamlit.components.v1 as components
import pyperclip
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
def save_response_to_gsheets(genero, correo, nombre_apellido,  edad, nivel_estudios, nivel_estudios_otro, rama_estudios, rama_estudios_otro, años_experiencia, pais_residencia, answers, opcion_otro_8, opcion_otro_9):

    # Crear nueva fila con timestamp
    nueva_respuesta = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'genero': genero,
        'correo_electronico': correo,
        'nombre_apellido': nombre_apellido, 
        'edad': edad,
        'nivel_estudios': nivel_estudios, 
        'nivel_estudios_otro': nivel_estudios_otro, 
        'rama_estudios': rama_estudios,
        'rama_estudios_otro': rama_estudios_otro, 
        'anos_experiencia': años_experiencia,
        'pais_residencia': pais_residencia,
        'opción_otro_8': opcion_otro_8,
        'opción_otro_9':opcion_otro_9
    }
    # Añadir las respuestas a las preguntas dinámicamente
    for i, respuesta in enumerate(answers):
        nueva_respuesta[f"pregunta_{i + 1}"] = respuesta

    # Subir la nueva respuesta a Supabase
    try:
        # Insertar la respuesta en la base de datos
        response = supabase.table("respuestas").insert([nueva_respuesta]).execute()

        # # Verificar si la inserción fue exitosa
        # if response.data:
        #     st.success(textos["enviado_con_éxtio"])
        # else:
        #     st.error(f"{textos['error_envio']}: {response.raw_error or 'Error desconocido'}")

    
    except Exception as e:
        st.error(f"Error al guardar la respuesta: {str(e)}")  # Manejo de error en caso de falla
    # Confirmación en la interfaz 


# Next Question
def next_section():
    st.session_state.question_index += 1
    st.session_state.selected_option = None  # Restablecer la opción seleccionada
    st.session_state.scroll_to_top = True
    st.rerun()  # Forzar la actualización inmediata de la interfaz

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
    if "document_downloaded" not in st.session_state:
        st.session_state.document_downloaded = False
    
    ################################################################ Acceso al cuestionario  ################################################################ 
    if st.session_state.question_index == 1: 
        st.title(textos["empezar_cuestionario"])
        
        st.write(textos["leer_terminos"])
        
        # Mostrar botón de descarga del documento
        with open("consentiment_informat.pdf", "rb") as file:  
            if st.download_button(label="📄 Descargar hoja de información y consentimiento", data=file, file_name="hoja_informacion_consentimiento.pdf", mime="application/pdf"):
                st.session_state.document_downloaded = True

        # Mostrar botón de confirmación solo si se descargó
        if st.session_state.get("document_downloaded", False) and not st.session_state.get("terms_read", False):
            if st.button(textos["confirmo_leer_terminos"]):
                st.session_state.terms_read = True

        # Mostrar aceptación si ya marcó como leído
        if st.session_state.terms_read:
            accept = st.checkbox(textos["acepto_terminos"])
            if accept:
                st.session_state.accepted_terms = True
            else:
                st.warning(textos["error_terminos"])
                
        # Mostrar botón de continuar solo si ha aceptado
        if st.session_state.accepted_terms:
            if st.button(textos["boton_empezar"]):
                next_section()
            
                
    ################################################################ SECTION 1: Personal Information ################################################################ 
    if st.session_state.question_index == 2:
            
        st.header(textos["info_personal"])
        
        # #Pregunta nombre y apellido
        # with st.container(): 
        #     st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">{textos['pregunta_nombre'].replace("**", "")}</p>
        #         </div>
        #         """,unsafe_allow_html=True)
            
        #     # Restaurar respuesta si retrocede
        #     if "nombre_apellido" in st.session_state:
        #         st.session_state.nombre_apellido = st.text_input(textos["opciones_nombre"], value=st.session_state.correo)
        #     else:
        #         st.session_state.nombre_apellido = st.text_input(textos["opciones_nombre"])
                
        # #Pregunta correo
        # with st.container(): 
        #     st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">{textos['pregunta_correo'].replace("**", "")}</p>
        #         </div>
        #         """,unsafe_allow_html=True)
            
        #     # Restaurar respuesta si retrocede
        #     if "correo" in st.session_state:
        #         st.session_state.correo = st.text_input(textos["opcion_correo"], value=st.session_state.correo)
        #     else:
        #         st.session_state.correo = st.text_input(textos["opcion_correo"])
        
        #Pregunta género
        with st.container(): 
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">
                        {textos['pregunta_genero'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            genero_index = None
            if "genero" in st.session_state:
                genero_index = textos["genero_opciones"].index(st.session_state.genero) if st.session_state.genero else None
            st.session_state.genero = st.radio( label="", options=textos["genero_opciones"], index=genero_index , label_visibility="collapsed")
        
        #Pregunta edad
        with st.container(): 
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">
                        {textos['pregunta_edad'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            age_index = None
            if "age" in st.session_state:
                age_index = textos["edad_opciones"].index(st.session_state.age) if st.session_state.age else None
            st.session_state.age = st.radio( label="", options=textos["edad_opciones"], index=age_index, label_visibility="collapsed")
        
        #Pregunta nivel estudios  
        with st.container(): #Pregunta nivel estudios
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">
                        {textos['pregunta_nivel_estudios'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            nivel_estudios_index = None
            opciones = textos["opciones_nivel_estudios"]
            if "nivel_estudios" in st.session_state:
                nivel_estudios_index = textos["opciones_nivel_estudios"].index(st.session_state.nivel_estudios) if st.session_state.nivel_estudios else None
            st.session_state.nivel_estudios = st.radio( label="", options=textos["opciones_nivel_estudios"], index=nivel_estudios_index, label_visibility="collapsed")
            
            if "nivel_estudios_otro" not in st.session_state: # Inicialización
                st.session_state.nivel_estudios_otro = "" 
            otro_estudios = ""
            seleccion = st.session_state.nivel_estudios 
            if seleccion == opciones[-1]:
                otro_estudios = st.text_input(textos["otros_opcion"], key="otro_nivel_estudios")
                if otro_estudios:
                    otro_estudios = st.session_state.nivel_estudios_otro 
        
                
        with st.container(): #Pregunta rama estudios
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">
                        {textos['pregunta_rama_estudios'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            rama_estudios_index = None
            if "rama_estudios" in st.session_state:
                rama_estudios_index = textos["opciones_rama_estudios"].index(st.session_state.rama_estudios) if st.session_state.rama_estudios else None
            st.session_state.rama_estudios = st.radio( label="", options=textos["opciones_rama_estudios"], index=rama_estudios_index, label_visibility="collapsed")
            
            if "rama_estudios_otro" not in st.session_state: # Inicialización
                st.session_state.rama_estudios_otro = "" 
                
            otro_rama_estudios = ""
            seleccion = st.session_state.rama_estudios_otro 
            if seleccion == textos["opciones_rama_estudios"][-1]:
                otro_rama_estudios = st.text_input(textos["otros_opcion"], key="otro_rama_estudios")
                if otro_rama_estudios:
                    otro_rama_estudios = st.session_state.rama_estudios_otro 
        
        
        with st.container(): #Pregunta años experiencia
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">
                        {textos['pregunta_años_experiencia'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            años_experiencia_index = None
            if "años_experiencia" in st.session_state:
                años_experiencia_index = textos["opciones_años_experiencia"].index(st.session_state.años_experiencia) if st.session_state.años_experiencia else None
            st.session_state.años_experiencia = st.radio( label="", options=textos["opciones_años_experiencia"], index=años_experiencia_index, label_visibility="collapsed")
        
        with st.container():
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">
                        {textos['pregunta_pais_residencia'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
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
                    # "genero": st.session_state.genero,
                    # "correo": st.session_state.correo,
                    "nombre_apellido": st.session_state.nombre_apellido,
                    "edad": st.session_state.age,
                    "nivel_estudios": st.session_state.nivel_estudios,
                    "nivel_estudios_otro": st.session_state.nivel_estudios_otro, ####nuevo
                    "rama_estudios": st.session_state.rama_estudios,
                    "rama_estudios_otro": st.session_state.rama_estudios_otro, ####nuevo
                    "años_experiencia": st.session_state.años_experiencia,
                    "pais_residencia": st.session_state.pais_residencia
                }
            
            next_section()  # Avanzamos a la siguiente sección
    
    ################################################################ SECTION 2: (Knowledge about AI) ################################################################ 

    elif st.session_state.question_index == 3:
            
        st.header(textos["Seccion_2"])
                
        with st.container(): #Pregunta 2_1
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_2_1'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            #Restaurar respuesta si retrocede
            q21_index = None
            if "q21" in st.session_state:
                q21_index = textos["opciones_2_1"].index(st.session_state.q21) if st.session_state.q21 else None
            st.session_state.q21 = st.radio( label="", options=textos["opciones_2_1"], index=q21_index , label_visibility="collapsed")
            
        
        with st.container(): #Pregunta 2_2
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_2_2'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            q22_index = None
            if "q22" in st.session_state:
                q22_index = textos["opciones_2_2"].index(st.session_state.q22) if st.session_state.q22  else None
            st.session_state.q22 = st.radio(label="", options=textos["opciones_2_2"], index=q22_index, label_visibility="collapsed")

        with st.container(): #Pregunta 2_3
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_2_3'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            seleccionadas_q23 = []
            for opcion in textos["opciones_2_3"]:
                if st.checkbox(opcion, key=f"q23_{opcion}"):
                    seleccionadas_q23.append(opcion)
            st.session_state.q23 = seleccionadas_q23
    
            if "otro_2_3" not in st.session_state:
                st.session_state.otro_2_3 = "" 
                
            if textos["opciones_2_3"][-1] in seleccionadas_q23:  # Si "Otros" está en las opciones seleccionadas
                otro_2_3 = st.text_input(textos["otros_opcion"], key="otro_2_3")
                
                if otro_2_3:
                    st.session_state.q23_otro = otro_2_3
                else:
                    st.session_state.q23_otro = ""
        
        with st.container(): #Pregunta 2_4
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_2_4'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            if "otro_2_4" not in st.session_state:
                st.session_state.otro_2_4 = ""
    
            q24_index = None
            if "q24" in st.session_state:
                q24_index = textos["opciones_2_4"].index(st.session_state.q24) if st.session_state.q24 else None
            st.session_state.q24 = st.radio(label="", options=textos["opciones_2_4"], index=q24_index, label_visibility="collapsed")
            
            otro_2_4 = ""
            seleccion_2_4 = st.session_state.q24 
            if seleccion_2_4 == textos["opciones_2_4"][-1]:
                otro_2_4 = st.text_input(textos["otros_opcion"], key="otro_2_4")
                if otro_2_4:
                    st.session_state.q24_otro = otro_2_4
        
        ## Definición Sesgos:             
        st.markdown(f"<p style='font-size: 1.2rem;'><strong>{textos["nota"]}</strong>{textos["un"]}<strong>{textos["sesgo"]}</strong> {textos["intro_preguntas_sesgos"]}</p>",unsafe_allow_html=True)

        
        with st.container(): #Pregunta 2_5
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_2_5'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            q25_index = None
            if "q25" in st.session_state:
                q25_index = textos["opciones_2_5"].index(st.session_state.q25) if st.session_state.q25  else None
            st.session_state.q25 = st.radio(label="", options=textos["opciones_2_5"], index=q25_index, label_visibility="collapsed")

            
        with st.container(): #Pregunta 2_6
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_2_6'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            q26_index = None
            if "q26" in st.session_state:
                q26_index = textos["opciones_2_6"].index(st.session_state.q26) if st.session_state.q26  else None
            st.session_state.q26 = st.radio(label="q26", options=textos["opciones_2_6"], index=q26_index, label_visibility="collapsed")


        with st.container(): #Pregunta 2_7
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_2_7'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            q27_index = None
            if "q27" in st.session_state:
                q27_index = textos["opciones_2_7"].index(st.session_state.q27) if st.session_state.q27  else None
            st.session_state.q27 = st.radio(label="", options=textos["opciones_2_7"], index=q27_index, label_visibility="collapsed")

        with st.container(): #Pregunta 2_8
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_2_8'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            q28_index = None
            if "q28" in st.session_state:
                q28_index = textos["opciones_2_8"].index(st.session_state.q28) if st.session_state.q28  else None
            st.session_state.q28 = st.radio(label="", options=textos["opciones_2_8"], index=q28_index, label_visibility="collapsed")

                    
        if st.button(textos["boton_continuar"], key="btn_sec2"):
            if (
                st.session_state.q21 is None or
                st.session_state.q22 is None or
                st.session_state.q24 is None or
                st.session_state.q25 is None or
                st.session_state.q26 is None or
                st.session_state.q27 is None or
                st.session_state.q28 is None  
                
            ):
                st.warning(textos["selecciona_opción"])
            else:
                st.session_state.answer_sec_2 = {
                    "Pregunta 6": st.session_state.q21,
                    "Pregunta 7": st.session_state.q22,
                    "Pregunta 8": st.session_state.q23,
                    "Opción otro_8": st.session_state.otro_2_3,
                    "Pregunta 9": st.session_state.q24,
                    "Opción otro_9": st.session_state.otro_2_4,
                    "Pregunta 10": st.session_state.q25,
                    "Pregunta 11": st.session_state.q26,
                    "Pregunta 12": st.session_state.q27,
                    "Pregunta 13": st.session_state.q28,
                    
                }
                st.session_state.answers.extend([
                    st.session_state.q21, 
                    st.session_state.q22, 
                    st.session_state.q23, 
                    st.session_state.otro_2_3,
                    st.session_state.q24, 
                    st.session_state.otro_2_4,
                    st.session_state.q25, 
                    st.session_state.q26, 
                    st.session_state.q27, 
                    st.session_state.q28
                ])

                next_section()
                
        if st.button(textos["boton_atras"]):
            go_back_section()


    ################################################################ SECTION 3 ################################################################ 

    elif st.session_state.question_index == 4:
        
        st.header(textos["Seccion_3"])
        
        ##### CASO 1 #####
        st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; text-align: justify; margin-bottom: 0.2rem">
                            {textos['caso_1'].replace("**", "")}
                        </p>
                    </div>
                    """,unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 1.05rem; color: #2c2c2c;  text-align: justify; margin-bottom: 0.8rem;'>{textos['intro_q33']}</p>", unsafe_allow_html=True)
        with st.container(): #Pregunta 3_3
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">
                        {textos['pregunta_3_3'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            q33_index = None
            if "q33" in st.session_state:
                q33_index = textos["opciones_3_3"].index(st.session_state.q33) if st.session_state.q33 else None
            st.session_state.q33 = st.radio(label="", options=textos["opciones_3_3"], index=q33_index, label_visibility="collapsed")

        st.markdown(f"<p style='font-size: 1.05rem; color: #2c2c2c;  text-align: justify; margin-bottom: 0.8rem;'>{textos['intro_q34']}</p>", unsafe_allow_html=True)
        with st.container(): #Pregunta 3_4
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">
                        {textos['pregunta_3_4'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            q34_index = None
            if "q34" in st.session_state:
                q34_index = textos["opciones_3_4"].index(st.session_state.q34) if st.session_state.q34 else None
            st.session_state.q34 = st.radio(label="", options=textos["opciones_3_4"], index=q34_index, label_visibility="collapsed")
        
        ##### CASO 2 #####   
        st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; text-align: justify; margin-bottom: 0.2rem">
                        {textos['caso_2'].replace("**", "")}
                    </p>
                </div>
                """,unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 1.05rem; color: #2c2c2c; text-align: justify; margin-bottom: 0.8rem;'>"
            f"{textos['intro_q38_1']}<br>"
            f"{textos['intro_q38_2']}<br>"
            f"{textos['intro_q38_3']}<br>"
            f"{textos['intro_q38_4']}"f"</p>", unsafe_allow_html=True)        
        
        with st.container(): #Pregunta 3_8_1
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_3_8_1'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            q38_1_index = None
            if "q38_1" in st.session_state:
                q38_1_index = textos["opciones_3_8_1"].index(st.session_state.q38_1) if st.session_state.q38_1 else None
            st.session_state.q38_1 = st.radio(label="pregunta_3_8_1", options=textos["opciones_3_8_1"], index=q38_1_index, label_visibility="collapsed")
        
        with st.container(): #Pregunta 3_8_2
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">
                        {textos['pregunta_3_8_2'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            q38_2_index = None
            if "q38_2" in st.session_state:
                q38_2_index = textos["opciones_3_8_2"].index(st.session_state.q38_2) if st.session_state.q38_2 else None
            st.session_state.q38_2 = st.radio(label="pregunta_3_8_2", options=textos["opciones_3_8_2"], index=q38_2_index, label_visibility="collapsed")

        ##### CASO 3 #####
        st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; text-align: justify; margin-bottom: 0.2rem">
                        {textos['caso_3'].replace("**", "")}
                    </p>
                </div>
                """,unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 1.05rem; color: #2c2c2c; text-align: justify; margin-bottom: 0.8rem;'>"
            f"{textos['intro_caso_3_1']}<br>"
            f"{textos['intro_caso_3_2']}"f"</p>", unsafe_allow_html=True)

        with st.container(): #Pregunta 3_9_1
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_3_9_1'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            q39_1_index = None
            if "q39_1" in st.session_state:
                q39_1_index = textos["opciones_3_9_1"].index(st.session_state.q39_1) if st.session_state.q39_1 else None
            st.session_state.q39_1 = st.radio(label="pregunta_3_9_1", options=textos["opciones_3_9_1"], index=q39_1_index, label_visibility="collapsed")

        with st.container(): #Pregunta 3_9_2
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 0.2rem">
                        {textos['pregunta_3_9_2'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            q39_2_index = None
            if "q39_2" in st.session_state:
                q39_2_index = textos["opciones_3_9_2"].index(st.session_state.q39_2) if st.session_state.q39_2 else None
            st.session_state.q39_2 = st.radio(label="pregunta_3_9_2", options=textos["opciones_3_9_2"], index=q39_2_index, label_visibility="collapsed")


        with st.container(): #Pregunta 3_5
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_3_5'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            
            #Pregunta 3_5_1

            st.markdown(f"<p text-align: justify; margin-bottom: 0.8rem;'><strong>{textos["primer_principio"]}</strong>{textos['pregunta_3_5_1']}</p>", unsafe_allow_html=True)
            q35_1_index = None
            if "q35_1" in st.session_state:
                q35_1_index = textos["opciones_3_5_1"].index(st.session_state.q35_1) if st.session_state.q35_1 else None
            st.session_state.q35_1 = st.radio(label="pregunta_3_5_1", options=textos["opciones_3_5_1"], index=q35_1_index, label_visibility="collapsed")
            
            #Pregunta 3_5_2
            st.markdown(f"<p text-align: justify; margin-bottom: 0.8rem;'><strong>{textos["segundo_principio"]}</strong>{textos['pregunta_3_5_2']}</p>", unsafe_allow_html=True)
            q35_2_index = None
            if "q35_2" in st.session_state:
                q35_2_index = textos["opciones_3_5_2"].index(st.session_state.q35_2) if st.session_state.q35_2 else None
            st.session_state.q35_2 = st.radio(label="2", options=textos["opciones_3_5_2"], index=q35_2_index, label_visibility="collapsed")
            
            #Pregunta 3_5_3
            st.markdown(f"<p text-align: justify; margin-bottom: 0.8rem;'><strong>{textos["tercer_principio"]}</strong>{textos['pregunta_3_5_3']}</p>", unsafe_allow_html=True)
            q35_3_index = None
            if "q35_3" in st.session_state:
                q35_3_index = textos["opciones_3_5_3"].index(st.session_state.q35_3) if st.session_state.q35_3 else None
            st.session_state.q35_3 = st.radio(label="pregunta_3_5_3", options=textos["opciones_3_5_3"], index=q35_3_index, label_visibility="collapsed")

        with st.container(): #Pregunta 3_6
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_3_6'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
                </div>
                """,unsafe_allow_html=True)
            q36_index = None
            if "q36" in st.session_state:
                q36_index = textos["opciones_3_6"].index(st.session_state.q36) if st.session_state.q36 else None
            st.session_state.q36 = st.radio(label="q36", options=textos["opciones_3_6"], index=q36_index, label_visibility="collapsed")

        with st.container(): #Pregunta 3_7
            st.markdown(f""" <div style="margin-bottom: -1rem"> <p style="font-size: 1.2rem; font-weight: bold;  text-align: justify; margin-bottom: 0.2rem">
                        {textos['pregunta_3_7'].replace("**", "")}
                        <span style="color: red;">*</span>
                    </p>
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
                st.session_state.q35_1 is None or
                st.session_state.q35_2 is None or
                st.session_state.q35_3 is None or
                st.session_state.q36 is None or
                st.session_state.q37 is None or
                st.session_state.q38_1 is None or
                st.session_state.q38_2 is None or
                st.session_state.q39_1 is None or
                st.session_state.q39_2 is None
            ):
                st.warning(textos["selecciona_opción"])
            else:
                st.session_state.answer_sec_3 = {
            
                    "Pregunta 14": st.session_state.q33,
                    "Pregunta 15": st.session_state.q34,
                    "Pregunta 16": st.session_state.q38_1,
                    "Pregunta 17": st.session_state.q38_2,
                    "Pregunta 18": st.session_state.q39_1,
                    "Pregunta 19": st.session_state.q39_2,
                    "Pregunta 20": st.session_state.q35_1,
                    "Pregunta 21": st.session_state.q35_2,
                    "Pregunta 22": st.session_state.q35_3,
                    "Pregunta 23": st.session_state.q36,
                    "Pregunta 24": st.session_state.q37
                }
                st.session_state.answers.extend([

                    st.session_state.q33,
                    st.session_state.q34,
                    st.session_state.q38_1,
                    st.session_state.q38_2,
                    st.session_state.q39_1,
                    st.session_state.q39_2,
                    st.session_state.q35_1,
                    st.session_state.q35_2,
                    st.session_state.q35_3,
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
        # Enlace para compartir
        link = "https://ai-study-tfg.streamlit.app/"

        # Caja visual con mensaje
        st.markdown(f"""
        <div style="background-color: #e8f5e9; padding: 20px; border-radius: 12px; margin-top: 30px; text-align: center;">
            <h4>📢 ¡Comparte este cuestionario!</h4>
            <p>Haz clic en el botón para copiar el enlace y difundirlo en tus redes sociales.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="display: flex; justify-content: center; margin-top: 10px;">
            <div style="width: fit-content;">
        """, unsafe_allow_html=True)

        st.code("https://ai-study-tfg.streamlit.app/", language="text")

        st.markdown("</div></div>", unsafe_allow_html=True)

        # Diccionario de redes sociales con enlaces e íconos
        social_links = {
            "Facebook": (
                f"https://www.facebook.com/sharer/sharer.php?u={link}",
                "https://cdn-icons-png.flaticon.com/512/145/145802.png"
            ),
            "Twitter": (
                f"https://twitter.com/intent/tweet?url={link}",
                "https://cdn-icons-png.flaticon.com/512/145/145812.png"
            ),
            "LinkedIn": (
                f"https://www.linkedin.com/sharing/share-offsite/?url={link}",
                "https://cdn-icons-png.flaticon.com/512/145/145807.png"
            ),
            "WhatsApp": (
                f"https://wa.me/?text={link}",
                "https://cdn-icons-png.flaticon.com/512/733/733585.png"
            ),
            "Telegram": (
                f"https://t.me/share/url?url={link}",
                "https://cdn-icons-png.flaticon.com/512/2111/2111646.png"
            ),
            "Instagram": (
                "https://www.instagram.com/",  # No se puede compartir enlace directo
                "https://cdn-icons-png.flaticon.com/512/2111/2111463.png"
            )
        }

        # Mostrar íconos en filas de 3
        st.markdown("### Compartir en redes sociales:")
        cols = st.columns(3)
        i = 0
        for name, (url, icon_url) in social_links.items():
            with cols[i % 3]:
                st.markdown(f"""
                <a href="{url}" target="_blank" style="text-decoration: none;">
                    <div style="text-align: center;">
                        <img src="{icon_url}" width="50" style="margin-bottom: 5px;" />
                        <div style="font-size: 12px;">{name}</div>
                    </div>
                </a>
                """, unsafe_allow_html=True)
            i += 1


        st.markdown('')
        st.markdown('')

        # Guardar todas las respuestas acumuladas al final
        if 'personal_data' in st.session_state:
            personal_data = st.session_state.personal_data
            
            # st.write("Datos personales guardados:", st.session_state.personal_data) #Depuración
            opcion_otro_8 = st.session_state.get("q23_otro", "")
            opcion_otro_9 = st.session_state.get("q24_otro", "")
            
            save_response_to_gsheets(
                personal_data["genero"],
                personal_data["correo"],
                personal_data["nombre_apellido"],
                personal_data["edad"],
                personal_data["nivel_estudios"],
                personal_data["nivel_estudios_otro"],
                personal_data["rama_estudios"], 
                personal_data["rama_estudios_otro"],
                personal_data["años_experiencia"],
                personal_data["pais_residencia"],
                st.session_state.answers,
                opcion_otro_8,
                opcion_otro_9
            )

            # Limpiar las respuestas después de guardarlas
            st.session_state.answers = []
            if st.button(textos["inicio_cuestionario"]):
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
