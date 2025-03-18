import streamlit as st # type: ignore
import pandas as pd # type: ignore 
import os  
import tempfile
import re 
import importlib



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

# Depuración: imprimir los textos para verificar que se han cargado correctamente
# st.write("Textos cargados:", textos)

# Opciones de respuesta en escala de 5
SCALE_OPTIONS = [
    textos["totalmente_en_desacuerdo"],
    textos["en_desacuerdo"],
    textos["neutral"],
    textos["de_acuerdo"],
    textos["totalmente_de_acuerdo"]
]

#Create CSV
def create_csv():
    csv_path = os.path.join(tempfile.gettempdir(), 'respuestas.csv')
    if not os.path.isfile('respuestas.csv'):
        # Crear un archivo CSV con encabezados si no existe
        pd.DataFrame(columns=['Nombre', 'Apellido', 'Género', 'Correo Electrónico', 'Edad', 'Sector de Trabajo', 'Años Trabajando', 'País' , 'Pregunta', 'Respuesta']).to_csv('respuestas.csv', index=False)

# Validar el formato del correo electrónico
def is_valid_email(email):
    # Expresión regular para validar el formato del correo electrónico
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Save answers in a CSV
def save_personal_info(nombre, apellido, genero, correo, edad):
    # csv_path = os.path.join(tempfile.gettempdir(), 'respuestas.csv')

    # Verificar si el archivo CSV ya existe
    file_exists = os.path.isfile('respuestas.csv')
    
    # Crear un DataFrame con la nueva respuesta
    new_data = pd.DataFrame({
        'Nombre': [nombre],
        'Apellido': [apellido],
        'Género': [genero],
        'Correo Electrónico': [correo],
        'Edad' : [edad],
    })
    
    # Guardar en CSV, si el archivo ya existe, agregar sin encabezados
    new_data.to_csv('respuestas.csv', mode='a', header=False, index=False)
    
def save_personal_info_work_life( sector_trabajo, years_working, country ):
    # csv_path = os.path.join(tempfile.gettempdir(), 'respuestas.csv')

    # Verificar si el archivo CSV ya existe
    file_exists = os.path.isfile('respuestas.csv')
    
    # Crear un DataFrame con la nueva respuesta
    new_data = pd.DataFrame({
        'Sector de Trabajo' : [sector_trabajo],
        'Años Trabajando' : [years_working],
        'País': [country]
    })
    
    # Guardar en CSV, si el archivo ya existe, agregar sin encabezados
    new_data.to_csv('respuestas.csv', mode='a', header=False, index=False)
    
def save_response(pregunta, respuesta):
    # Verificar si el archivo CSV ya existe
    file_exists = os.path.isfile('respuestas.csv')
    
    # Crear un DataFrame con la nueva respuesta
    new_data = pd.DataFrame({
        'Pregunta': [pregunta],
        'Respuesta': [respuesta]
    })
    
    # Guardar en CSV, si el archivo ya existe, agregar sin encabezados
    new_data.to_csv('respuestas.csv', mode='a', header=False, index=False)

# Next Question
def next_question():
    st.session_state.question_index += 1
    st.session_state.selected_option = None  # Restablecer la opción seleccionada

def next_video(question_index):
    video_path = os.path.join("Media", "Questionarios_videos", f"Q{question_index + 1}.mp4")
    if os.path.isfile(video_path):
        st.video(video_path, format="video/mp4", start_time=0)
    else:
        st.error(textos["video_no_encontrado"])
        

# Display Question
def display_question(questions):
    
    current_question = questions[st.session_state.question_index - 1]  # -1 because index 0 is for personal info
    next_video(st.session_state.question_index - 1) # Mostrar el video 
    
    st.header(f"Pregunta {st.session_state.question_index}:")
    answer = st.radio(current_question["question"], SCALE_OPTIONS, index=None)
        
    # answer_index = st.slider(
    #     label=current_question["question"],
    #     min_value=0,
    #     max_value=4,
    #     step=1,
    #     format=SCALE_OPTIONS[0],  # Muestra el primer valor como referencia
    #     key=f"q{st.session_state.question_index}"
    # )
    # answer = SCALE_OPTIONS[answer_index]

    # Next question + video
    if st.button("Enviar"):
        if answer is not None and answer != "":
            save_response(current_question["question"], answer)
            st.success("Enviado con éxito!")
            # st.button("Siguiente")
            next_question()  # Go to next question 
        else:
            st.warning(textos["selecciona_opción"])

def cuestions():
    
    st.title(textos["cuestionario"])
    
    # Inicializar el estado de la sesión si no existe
    if 'question_index' not in st.session_state:
        st.session_state.question_index = -1  # Comenzar desde la primera pregunta
        st.session_state.selected_option = None  # Opción seleccionada
    
    if st.session_state.question_index == -1:
        st.header(textos["info_personal"])
        st.session_state.nombre = st.text_input(textos["nombre"])
        st.session_state.apellido = st.text_input(textos["apellido"])
        st.session_state.genero = st.radio(textos["pregunta_genero"], textos["genero_opciones"], index=None)
        st.session_state.age = st.radio(textos["pregunta_edad"], textos["edad_opciones"], index=None)
        st.session_state.correo = st.text_input(textos["opcion_correo"])
        
        if st.button(textos["boton_continuar"]):
            if st.session_state.correo and not is_valid_email(st.session_state.correo):
                    st.warning(textos["error_correo"])
            if st.session_state.nombre and st.session_state.apellido and st.session_state.genero and st.session_state.age:
                save_personal_info(st.session_state.nombre, st.session_state.apellido, st.session_state.genero, st.session_state.correo, st.session_state.age)  # Guardar información personal
                st.success(textos["enviado_con_éxtio"])
                next_question()  # Go to next question 
            else:
                st.warning(textos["advertencia_faltan_datos"])   
                
    elif st.session_state.question_index == 0:
        st.header(textos["información_personal"])
        st.session_state.sector_trabajo = st.radio(textos["pregunta_sector_estudio_trabajo"], textos["opciones_sector"], index=None) #ACABARLO
        st.session_state.years_working = st.radio(textos["pregunta_experiencia"], textos["opciones_experiencia"], index=None)
        st.session_state.country = st.selectbox("Porfavor seleccione su país de residéncia:" ,["España", "Francia", "Estados Unidos", "México", "Argentina", "Colombia", "Chile", "Otro"], index=None) # Hacerla para seleccionar todos los countries 
        
        if st.button("Continuar"):
            if st.session_state.sector_trabajo and st.session_state.years_working and st.session_state.country:
                save_personal_info_work_life(st.session_state.sector_trabajo, st.session_state.years_working, st.session_state.country)  # Guardar información personal
                st.success("Enviado con éxito!")
                next_question()  # Go to next question 
            else:
                st.warning("Por favor, ingresa los datos. ")
                

    else:     
        # Lista de preguntas
        questions = [
            {"question": "El trabajo en equipo es esencial para el éxito."},
            {"question": "Me siento motivado en mi trabajo actual."},  # Aquí estaba el error
            {"question": "HOLAAA."}   
        ]
        
        # Mostrar la pregunta actual
        if st.session_state.question_index - 1 < len(questions):
            display_question(questions)
        else:
            st.write("Gracias por completar el cuestionario!")

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
    
    # Crear el archivo CSV si no existe
    create_csv()  
    
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
