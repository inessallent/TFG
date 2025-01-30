import streamlit as st # type: ignore
import pandas as pd # type: ignore 
# from streamlit_extras.metric_cards import style_metric_cards  #type ignore 
import os  

#Create CSV
def create_csv():
    if not os.path.isfile('respuestas.csv'):
        # Crear un archivo CSV con encabezados si no existe
        pd.DataFrame(columns=['Pregunta', 'Respuesta']).to_csv('respuestas.csv', index=False)


# Save answers in a CSV
def save_response(pregunta, respuesta):
    # Verificar si el archivo CSV ya existe
    file_exists = os.path.isfile('respuestas.csv')
    
    # Crear un DataFrame con la nueva respuesta
    new_data = pd.DataFrame({
        'Pregunta': [pregunta],
        'Respuesta': [respuesta]
    })
    
    # Guardar en CSV, si el archivo ya existe, agregar sin encabezados
    new_data.to_csv('respuestas.csv', mode='a', header=not file_exists, index=False)

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
    current_question = questions[st.session_state.question_index]
    
    # Mostrar el video 
    next_video(st.session_state.question_index)

    # Mostrar pregunta
    st.header(f"Question {st.session_state.question_index + 1}:")
    answer =  st.radio(current_question["question"], current_question["options"])

    # Next question + video
    if st.button("Enviar"):
        if answer:
            save_response(current_question["question"], answer)  # Guardar respuesta
            st.success("Enviado con éxito!")
            st.button("Siguiente")
            next_question()  # Go to next question 
        else:
            st.warning("Por favor, selecciona una opción antes de continuar.")

def cuestions():
    
    st.title('Cuestionario')
    
    # Inicializar el estado de la sesión si no existe
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0  # Comenzar desde la primera pregunta
        st.session_state.selected_option = None  # Opción seleccionada
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
    if st.session_state.question_index < len(questions):
        display_question(questions)
    else:
        st.write("Gracias por completar el cuestionario!")


def main():  
    
    # Crear el archivo CSV si no existe
    create_csv()  
    
    # Sidebar para la navegación
    st.sidebar.title("Navegación") #Title 
    UPF_logo_path = os.path.join("Media", "Logos", "UPF_logo.png")
    st.sidebar.image(UPF_logo_path)  #Upload Logo
    page_web = st.sidebar.selectbox("Selecciona una sección:", ["Inicio", "Questionario", "Sobre Nosotros", "Contacto"])

    #Init 
    if page_web == "Inicio":
        st.title('Inicio')
        st.write("Aquí puedes escribir información sobre quiénes son.")

    #Questionario
    elif page_web == "Cuestionario":
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


    # style_metric_cards(border_left_color="#e1ff8b",background_color="#222222")

if __name__ == "__main__":
    main() 
