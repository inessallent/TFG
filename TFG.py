

import streamlit as st # type: ignore
import pandas as pd # type: ignore 
from streamlit_extras.metric_cards import style_metric_cards # type: ignore 
import base64 

    
def main():  
    # Sidebar para la navegación
    st.sidebar.title("Navegación") 
    st.sidebar.image("UPF_logo.png")
    page_web = st.sidebar.selectbox("Selecciona una sección:", ["Inicio", "Questionario", "Sobre Nosotros", "Contacto"])

    # Cargar una imagen en la página inicial
    if page_web == "Inicio":
        st.title('Inicio')
        st.write("Aquí puedes escribir información sobre quiénes son.")

    elif page_web == "Questionario":
        st.title('Questionario')
        st.write("Aquí puedes escribir información sobre quiénes son.")
    
        st.header("Question 1:")
        answer_1 = st.radio("What would you choose?", ("1", "2", "3")) 
        button1 = st.button("Submit Answer")
        
    elif page_web == "Sobre Nosotros":
        st.title('Sobre Nosotros')
        st.write("This questionnaire is part of the final project from my degree.")


    elif page_web == "Contacto":
        st.write("Si deseas ponerte en contacto con nosotros, por favor completa el siguiente formulario:")
        email = st.text_input("Tu correo electrónico:")
        mensaje = st.text_area("Tu mensaje:")
        if st.button("Enviar"):
            st.success("¡Mensaje enviado con éxito!")


    style_metric_cards(border_left_color="#e1ff8b",background_color="#222222")

if __name__ == "__main__":
    main()