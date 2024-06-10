import streamlit as st
import sys
import os
import pandas as pd

# Agregar la ruta de la carpeta externa al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Costo_real')))
from Costo_real.Costo_Real import CostoReal

#Configuración de la página
st.set_page_config(page_title="Calculadora CR",page_icon='🔣',layout='wide')
hide_menu ="""
<style>
#MainMenu {
    visibility:hidden;
}

[data-testid="stSidebar"] {
    display: none !important;
}

[data-testid="stApp"] {
    background-color: #020212;
    opacity: 0.8;
    background-image: radial-gradient(#232cd1 0.5px, #020212 0.5px);
    background-size: 10px 10px;
}
[data-testid="stHeader"] {
    visibility:hidden;
    background-color: #020212;
    opacity: 1;
    background-image: radial-gradient(#232cd1 0.5px, #020212 0.5px);
    background-size: 10px 10px;
}
"""
st.markdown(hide_menu,unsafe_allow_html=True)

#Título y regresar
col1, col2 = st.columns([4, 1])
with col1:
    st.title("Calculadora de costo real")
with col2:
    if st.button(" 🔙 Ir a la página principal"):
        st.switch_page('Portafolio.py')

mb52 = None
mb51 = None
#Carga de archivos
col3, col4 = st.columns(2)
with col3:
    archivo_MB51 = st.file_uploader("Cargar archivo MB51", type=["xlsx"])
    centros = st.text_input("Ingrese los centros:")
with col4:
    archivo_MB52 = st.file_uploader("Cargar archivo MB52", type=["xlsx"])
    almacenes = st.text_input("Ingrese los almacenes:")

#Ejecutar costo real
if st.button("Generar informe"):
    if archivo_MB52 is not None:
        # Leer el archivo y convertirlo en DataFrame de Pandas
        mb52 = pd.read_excel(archivo_MB52)
    if archivo_MB51 is not None:
        # Leer el archivo y convertirlo en DataFrame de Pandas
        mb51 = pd.read_excel(archivo_MB51)
    if not mb52 or not mb51 or not centros or not almacenes:
            st.error("Por favor, adjunte todos los archivos.")
    else:
        pd.set_option('display.max_columns', None)
        st.success("Reporte generado correctamente.")
        Cr = CostoReal(mb51=mb51,mb52=mb52)
        informe = Cr.calcular_costo(centros, almacenes)
        st.table(informe)