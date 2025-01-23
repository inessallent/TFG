import streamlit as st


# Title App 
st.title("TFG") #Redefinir

# Sidebar para la navegación
st.sidebar.title("Navegación") 
page = st.sidebar.selectbox("Selecciona una sección:", ["Inicio", "Cuestionario", "Sobre Nosotros", "Contacto"])

# Cargar una imagen en la página inicial
if page == "Inicio":
    #st.image("ruta/a/tu/imagen.jpg", caption="Descripción de la imagen", use_column_width=True)
    st.write("Aquí puedes escribir información sobre quiénes son.")

elif page == "Cuestionario":
    st.write("Aquí puedes escribir información sobre quiénes son.")
    
elif page == "Sobre Nosotros":
    st.write("This questionnaire is part of the final project from my degree.")


elif page == "Contacto":
    st.write("Si deseas ponerte en contacto con nosotros, por favor completa el siguiente formulario:")
    email = st.text_input("Tu correo electrónico:")
    mensaje = st.text_area("Tu mensaje:")
    if st.button("Enviar"):
        st.success("¡Mensaje enviado con éxito!")