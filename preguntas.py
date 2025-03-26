import streamlit as st
import os
import pandas as pd
import re

# from main import textos, save_personal_info, save_personal_info_work_life, save_response, next_question, display_question, next_video, is_valid_email

def cuestions():
    st.title(textos["cuestionario"])
    
    if 'question_index' not in st.session_state:
        st.session_state.question_index = -1  
        st.session_state.selected_option = None  
    
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
                save_personal_info(st.session_state.nombre, st.session_state.apellido, st.session_state.genero, st.session_state.correo, st.session_state.age)
                st.success(textos["enviado_con_éxtio"])
                next_question()
            else:
                st.warning(textos["advertencia_faltan_datos"])   
                
    elif st.session_state.question_index == 0:
        st.header(textos["información_personal"])
        st.session_state.sector_trabajo = st.radio(textos["pregunta_sector_estudio_trabajo"], textos["opciones_sector"], index=None)
        st.session_state.years_working = st.radio(textos["pregunta_experiencia"], textos["opciones_experiencia"], index=None)
        st.session_state.country = st.selectbox("Por favor, seleccione su país de residencia:", ["España", "Francia", "Estados Unidos", "México", "Argentina", "Colombia", "Chile", "Otro"], index=None)
        
        if st.button("Continuar"):
            if st.session_state.sector_trabajo and st.session_state.years_working and st.session_state.country:
                save_personal_info_work_life(st.session_state.sector_trabajo, st.session_state.years_working, st.session_state.country)
                st.success("Enviado con éxito!")
                next_question()
            else:
                st.warning("Por favor, ingresa los datos.")
                
    else:     
        questions = [
            {"question": "El trabajo en equipo es esencial para el éxito."},
            {"question": "Me siento motivado en mi trabajo actual."},
            {"question": "HOLAAA."}   
        ]
        
        if st.session_state.question_index - 1 < len(questions):
            display_question(questions)
        else:
            st.write("Gracias por completar el cuestionario!")
