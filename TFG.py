import streamlit as st # type: ignore
import pandas as pandas # type: ignore 
# import plotly.express as px # type: ignore 
import base64 






# Función para establecer el fondo

def set_background(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64_image}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Establecer el fondo
# set_background("C:/Users/isall/OneDrive/UNI/TFG/TFG/fondo.png")


# Función para aplicar estilos personalizados al texto
def set_inicio_styles():
    custom_style = """
    <style>
    .custom-text {
        color: white 
        # font-size: 18px;  /* Tamaño del texto */
        # font-weight: bold;  /* Negrita */
    }
    </style>
    """
    st.markdown(custom_style, unsafe_allow_html=True)
    
    
# Title App 
st.title("TFG") #Redefinir

# Sidebar para la navegación
st.sidebar.title("Navegación") 
page_web = st.sidebar.selectbox("Selecciona una sección:", ["Inicio", "Questionario", "Sobre Nosotros", "Contacto"])

# Cargar una imagen en la página inicial
if page_web == "Inicio":
    st.title('Inicio')
    set_inicio_styles()
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
