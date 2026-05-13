import streamlit as st

st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")
sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"] )
