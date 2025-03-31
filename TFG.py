import streamlit as st # type: ignore
import pandas as pd # type: ignore 
import os  
import tempfile
import re 
import dns.resolver
import importlib
import datetime 
from streamlit_gsheets import GSheetsConnection 

# Create a connection object (with google sheets)
conn = st.connection("gsheets", type=GSheetsConnection)
    
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

# Opciones de respuesta en escala de 5
SCALE_OPTIONS = [
    textos["totalmente_de_acuerdo"],
    textos["de_acuerdo"],
    textos["neutral"],
    textos["en_desacuerdo"],
    textos["totalmente_en_desacuerdo"]
]

# Validar el formato del correo electrónico
def is_valid_email(email):
    # Regex que permite múltiples subdominios
    email_regex = r"^(?=.{1,256}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,24}$"
    return re.match(email_regex, email) is not None


# Save answers in New CSV
def save_response_to_gsheets(correo, genero, edad, sector_trabajo, years_working, country, answers):
    
    df = conn.read()

    # Crear nueva fila con timestamp
    nueva_respuesta = {
        "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Género': genero,
        'Correo Electrónico': correo,
        'Edad': edad,
        'Sector de Trabajo': sector_trabajo,
        'Años Trabajando': years_working,
        'País': country
    }
    # Añadir las respuestas a las preguntas (de manera dinámica)
    for i, respuesta in enumerate(answers):
        nueva_respuesta[f"Pregunta {i + 1}"] = respuesta

    # Añadir las respuestas a las preguntas dinámicamente
    for i, respuesta in enumerate(answers):
        nueva_respuesta[f"Pregunta {i + 1}"] = respuesta

    # Convertir a DataFrame
    nueva_fila = pd.DataFrame([nueva_respuesta])

    # Verificar columnas faltantes
    for col in df.columns:
        if col not in nueva_fila.columns:
            nueva_fila[col] = ""  # Rellenar con vacío si falta

    # Convertir a DataFrame solo con la nueva fila
    nueva_fila = pd.DataFrame([nueva_respuesta])

    # Asegurarse de que las columnas coincidan exactamente
    nueva_fila = nueva_fila.reindex(columns=df.columns, fill_value="")

    # **Actualizar usando `conn.update()` sumando la nueva fila**
    df_actualizado = pd.concat([df, nueva_fila], ignore_index=True)
    
    # Verificar el resultado (Depuración)
    #print("DataFrame actualizado:", df_actualizado.tail())

    # Subir la nueva fila (sin sobrescribir todo)
    conn.update(data=df_actualizado)
    
    st.success(textos["enviado_con_éxtio"])


# Next Question
def next_question():
    st.session_state.question_index += 1
    st.session_state.selected_option = None  # Restablecer la opción seleccionada
    st.rerun()  # Forzar la actualización inmediata de la interfaz

def next_video(question_index):
    video_path = os.path.join("Media", "Videos_Questionarios", f"Q{question_index + 1}.mp4")
    if os.path.isfile(video_path):
        st.video(video_path, format="video/mp4", start_time=0)
    else:
        st.error(textos["video_no_encontrado"])
        

# Display Question
def display_question(questions):
    
    current_question = questions[st.session_state.question_index - 1]  # -1 because index 0 is for personal info
    next_video(st.session_state.question_index - 1) # Mostrar el video 
    
    st.header(f"Pregunta {st.session_state.question_index}:")
    answer = st.radio(current_question["question"], SCALE_OPTIONS, index=None, key=f"question_{st.session_state.question_index}")
        

    if st.button(textos["boton_continuar"]):
        if not answer:  # Verificar que haya una respuesta seleccionada
            st.warning(textos["selecciona_opción"])  # Mostrar advertencia si no se ha seleccionado respuesta
            st.stop() 
            
        else:
            st.session_state.answers.append(answer) # Guardar la respuesta temporalmente en la lista
            next_question()  

def cuestions():
    st.title(textos["cuestionario"])

    # Inicializar el estado de la sesión si no existe
    if 'question_index' not in st.session_state:
        st.session_state.question_index = -1
    
    
    if 'answers' not in st.session_state:
        st.session_state.answers = []
        
    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = None
        

    if st.session_state.question_index == -1:
        st.header(textos["info_personal"])
        st.session_state.genero = st.radio(textos["pregunta_genero"], textos["genero_opciones"], index=None)
        st.session_state.age = st.radio(textos["pregunta_edad"], textos["edad_opciones"], index=None)
        st.session_state.correo = st.text_input(textos["opcion_correo"])

        if st.button(textos["boton_continuar"]):
            errores = []
            
            if not st.session_state.genero:
                errores.append(textos["error_genero"])
            
            if not st.session_state.age:
                errores.append(textos["error_age"])
        
                
            # if st.session_state.correo and not is_valid_email(st.session_state.correo):
            #     errores.append(textos["error_correo"])  # Formato inválido
            
            if errores:
                for error in errores:
                    st.warning(error)
                return #Deter ejecucion si hay errores
                
            else:
                st.session_state.personal_data = {
                    "genero": st.session_state.genero,
                    "correo": st.session_state.correo,
                    "edad": st.session_state.age
                }
            
            next_question()  # Avanzamos a la siguiente pregunta

    elif st.session_state.question_index == 0:
        st.header(textos["información_personal"])
        st.session_state.nivel_estudios = st.radio(textos["pregunta_nivel_estudio"], textos["opciones_nivel_estudios"], index=None)
        st.session_state.sector_trabajo = st.radio(textos["pregunta_sector_estudio_trabajo"], textos["opciones_sector"], index=None)
        st.session_state.years_working = st.radio(textos["pregunta_experiencia"], textos["opciones_experiencia"], index=None)
        st.session_state.country = st.selectbox(textos["pregunta_ciudad"], ["España", "Francia", "Estados Unidos", "México", "Argentina", "Colombia", "Chile", "Otro"], index=None)

        if st.button(textos["boton_continuar"]):
            
            if not (st.session_state.nivel_estudios and st.session_state.sector_trabajo and st.session_state.years_working and st.session_state.country):
                st.warning(textos["selecciona_opción"]) 
                st.stop() 
                
            else:
                # Guardamos esta información adicional en el estado de la sesión
                st.session_state.work_info = {
                    "sector_trabajo": st.session_state.sector_trabajo,
                    "years_working": st.session_state.years_working,
                    "country": st.session_state.country
                }
                next_question()  # Avanzamos a la siguiente pregunta

    else:     
        # Mostrar preguntas restantes
        questions = [
            {"question": textos["totalmente_en_desacuerdo"]},
            {"question": textos["en_desacuerdo"]},
            {"question": textos["neutral"]}
        ]
        
        # Mostrar la pregunta actual
        if st.session_state.question_index - 1 < len(questions):
            display_question(questions)
        else:
            st.write(textos["Gracias_por_contestar_el_formulario"])

            # Guardar todas las respuestas acumuladas al final
            if 'personal_data' in st.session_state and 'work_info' in st.session_state:
                personal_data = st.session_state.personal_data
                work_info = st.session_state.work_info
                
                # st.write("Datos personales guardados:", st.session_state.personal_data) #Depuración
                # st.write("Información laboral guardada:", st.session_state.work_info) #Depuración
                
                save_response_to_gsheets(
                    personal_data["genero"],
                    personal_data["correo"],
                    personal_data["edad"],
                    work_info["sector_trabajo"],
                    work_info["years_working"],
                    work_info["country"],
                    st.session_state.answers
                )

                # Limpiar respuestas después de guardar
                st.session_state.answers = []

                

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
