import streamlit as st

st.title("📊 Mi Primera App de Estadística")
st.header("Semana 1: Fundamentos y Entorno de Trabajo")

st.write("""
¡Bienvenido/a al curso de Estadística Aplicada con Python y R!
Esta aplicación web fue creada usando **Streamlit**.
""")

nombre_estudiante = st.text_input("Por favor, ingresa tu nombre:")

if nombre_estudiante:
    st.success(f"¡Hola, {nombre_estudiante}! Tu entorno está funcionando correctamente. ¡Buen trabajo!")
    st.balloons()
