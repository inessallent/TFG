

import streamlit as st # type: ignore
import pandas as pd # type: ignore 
from streamlit_extras.metric_cards import style_metric_cards  #type ignore 
import base64 

        
def main():  
        
    # Sidebar para la navegación
    st.sidebar.title("Navegación")    #Title 
    st.sidebar.image("UPF_logo.png")  #Upload Logo
    page_web = st.sidebar.selectbox("Selecciona una sección:", ["Inicio", "Questionario", "Sobre Nosotros", "Contacto"])

    #Init 
    if page_web == "Inicio":
        st.title('Inicio')
        st.write("Aquí puedes escribir información sobre quiénes son.")

    #Questionario
    elif page_web == "Questionario":
        questions()
        # st.title('Questionario')
        # st.write("Aquí puedes escribir información sobre quiénes son.")
    
        # st.header("Question 1:")
        # answer_1 = st.radio("What would you choose?", ("1", "2", "3")) 
        # # button1 = st.button("Submit Answer")
        # if st.button("Siguiente"):
        #     st.success("Enviado con éxito!")
            
    
    #Sobre Nosotros   
    elif page_web == "Sobre Nosotros":
        st.title('Sobre Nosotros')
        st.write("This questionnaire is part of the final project from my degree.")

    #Contacto 
    elif page_web == "Contacto":
        st.write("Si deseas ponerte en contacto con nosotros, por favor completa el siguiente formulario:")
        email = st.text_input("Tu correo electrónico:")
        mensaje = st.text_area("Tu mensaje:")
        if st.button("Enviar"):
            st.success("¡Mensaje enviado con éxito!")


    style_metric_cards(border_left_color="#e1ff8b",background_color="#222222")



def questions():
    
    st.title('Questionario')
    st.write("Aquí puedes escribir información sobre quiénes son.")
    
    # Inicializar el estado de la sesión si no existe
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0  # Comenzar desde la primera pregunta

    # Lista de preguntas
    questions = [
        "What would you choose? (1, 2, 3)",
        "What is your favorite color? (Red, Blue, Green)",
        "What is your favorite animal? (Dog, Cat, Bird)",
        "What is your favorite food? (Pizza, Sushi, Salad)",
        "What is your favorite season? (Winter, Spring, Summer)",
        "What is your favorite hobby? (Reading, Sports, Music)",
        "What is your dream job? (Engineer, Artist, Doctor)",
        "What is your favorite movie genre? (Action, Comedy, Drama)",
        "What is your favorite book? (Fiction, Non-Fiction, Mystery)",
        "What is your favorite travel destination? (Beach, Mountains, City)"    
        ]
    # Mostrar la pregunta actual
    if st.session_state.question_index < len(questions):
        st.header(f"Question {st.session_state.question_index + 1}:")
        answer = st.radio(questions[st.session_state.question_index].split(" (")[0], ("1", "2", "3"))

        # Botón para pasar a la siguiente pregunta
        if st.button("Siguiente"):
            st.success("Enviado con éxito!")
            st.session_state.question_index += 1  # Incrementar el índice de la pregunta
    else:
        st.write("Gracias por completar el cuestionario!")

if __name__ == "__main__":
    main() 
