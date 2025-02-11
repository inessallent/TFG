import streamlit as st # type: ignore
import pandas as pd # type: ignore 
import os  
import tempfile
import re 

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
        st.error("El video no se encontró en la ruta especificada.")
        

# Display Question
def display_question(questions):
    current_question = questions[st.session_state.question_index - 1]  # -1 because index 0 is for personal info
    
    # Mostrar el video 
    next_video(st.session_state.question_index - 1)

    # Mostrar pregunta
    st.header(f"Question {st.session_state.question_index }:")
    answer =  st.radio(current_question["question"], current_question["options"],index=0)

    # Next question + video
    if st.button("Enviar"):
        if answer is not None and answer != "":
            save_response(current_question["question"], answer)
            st.success("Enviado con éxito!")
            st.button("Siguiente")
            next_question()  # Go to next question 
        else:
            st.warning("Por favor, selecciona una opción antes de continuar.")

def cuestions():
    
    st.title('Cuestionario')
    
    # Inicializar el estado de la sesión si no existe
    if 'question_index' not in st.session_state:
        st.session_state.question_index = -1  # Comenzar desde la primera pregunta
        st.session_state.selected_option = None  # Opción seleccionada
    
    if st.session_state.question_index == -1:
        st.header("Información Personal")
        st.session_state.nombre = st.text_input("Nombre:")
        st.session_state.apellido = st.text_input("Apellido:")
        st.session_state.genero = st.radio("Género:", ["Femenino", "Masculino", "No binario", "Prefiero no decirlo"], index=None)
        st.session_state.age = st.radio("Edad:", ["Menor de 18", "18 - 24", "25 - 34", "35- 44", "55 - 64", "mayor de 64", "Prefiero no decirlo"], index=None)
        st.session_state.correo = st.text_input("Correo Electrónico (opcional):")
        
        if st.button("Continuar"):
            if st.session_state.correo and not is_valid_email(st.session_state.correo):
                    st.warning("Por favor, ingresa un correo electrónico válido.")
            if st.session_state.nombre and st.session_state.apellido and st.session_state.genero and st.session_state.age:
                save_personal_info(st.session_state.nombre, st.session_state.apellido, st.session_state.genero, st.session_state.correo, st.session_state.age)  # Guardar información personal
                st.success("Enviado con éxito!")
                st.button("Siguiente")
                next_question()  # Go to next question 
            else:
                st.warning("Por favor, ingresa tu nombre, apellido, género y edad. Gracias. ")   
                
    elif st.session_state.question_index == 0:
        st.header("Información Personal")
        st.session_state.sector_trabajo = st.radio("Porfavor seleccione el sector que mejor describa su trabajo o Estudios (en el caso que sea estudiante):", [ "Artes y Humanidades", "Negocios y Economía", "Ciencias de la Computación e Informática", "Educación", "Ingeniería y Tecnologia","Ciencias Ambientales y de la Tierra", "Salud y Medicina", "Derecho y Estudios Legales", "Ciencias de la Vida y Biología", "Matemáticas y Estadística", "Ciencias Físicas (p. ej., Física, Química)", "Ciencias Sociales", "Otros" ], index=None) #ACABARLO
        st.session_state.years_working = st.radio("¿Cuántos años de experiéncia tiene en este ámbito? :", ["Menor de 1 año", "1 - 3 años", "4 - 6 años", " 7 - 10 años", "Más de 10 años"], index=None)
        st.session_state.country = st.selectbox("Porfavor seleccione su país de residéncia:" ,["España", "Francia", "Estados Unidos", "México", "Argentina", "Colombia", "Chile", "Otro"], index=None) # Hacerla para seleccionar todos los countries 
        
        if st.button("Continuar"):
            if st.session_state.sector_trabajo and st.session_state.years_working and st.session_state.country:
                save_personal_info_work_life(st.session_state.sector_trabajo, st.session_state.years_working, st.session_state.country)  # Guardar información personal
                st.success("Enviado con éxito!")
                st.button("Siguiente")
                next_question()  # Go to next question 
            else:
                st.warning("Por favor, ingresa los datos. ")
                

    else:     
        # Lista de preguntas
        questions = [
            {
                "question": "What would you choose?",
                "options": ["Option A", "Option B", "Option C"]
            },
            {
                "question": "What is your favorite color?",
                "options": ["Red", "Blue", "Green"]
            },    
        ]
        # Mostrar la pregunta actual
        if st.session_state.question_index <= len(questions):
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
    st.sidebar.title("Navegación") #Title 
    # UPF_logo_path = os.path.join("Media", "Logos", "UPF_logo.png")
    # st.sidebar.image(UPF_logo_path)  #Upload Logo
    page_web = st.sidebar.selectbox("Selecciona una sección:", ["Cuestionario", "Sobre Nosotros", "Contacto"])


    #Cuestionario
    if page_web == "Cuestionario":
        cuestions()            
    
    #Sobre Nosotros   
    elif page_web == "Sobre Nosotros":
        st.title('Sobre Nosotros')
        st.write("This questionnaire is part of the final project from my degree.")

    #Contacto 
    elif page_web == "Contacto":
        st.title("Contacto")
        st.write("Si deseas ponerte en contacto con nosotros, por favor completa el siguiente formulario:")
        email = st.text_input("Tu correo electrónico:")
        mensaje = st.text_area("Tu mensaje:")
        if st.button("Enviar"):
            st.success("¡Mensaje enviado con éxito!")


if __name__ == "__main__":
    main() 
