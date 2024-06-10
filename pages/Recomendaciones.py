import streamlit as st
import pandas as pd
import sys
import os
import plotly.express as px
import requests
import io

# Agregar la ruta de la carpeta externa al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Recomendador')))

#Cargando funciones
from Recomendador.ayudantes import hacer_recomendacion

#Configuración de la página
st.set_page_config(page_title="Librería",page_icon='📚',layout='wide')
hide_menu ="""
<style>
#MainMenu {
    visibility:hidden;
}

[data-testid="stApp"] {
    background-color: #808080;
    opacity: 0.8;

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


st.image('./Imagenes/libros.png', use_column_width=True)

# Insertar un espacio vertical de 60px
st.markdown(f'<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)

#Base de los libros
dflibros = pd.read_excel('bbdd_rating.xlsx')

# Configurar el sidebar con inputs y un botón.
with st.sidebar:
    st.header("Libros disponibles en la tienda")
    default = "Harry Potter and The Sorcerer's Stone"
    libro = st.selectbox("Selecciona un libro", dflibros['Title'],index=dflibros['Title'].tolist().index(default))
    
    # Filtrar DataFrame según el término de búsqueda
    if libro:
        try:
            book_details = dflibros[dflibros['Title'] == libro].iloc[0]
            st.image(book_details['image'])
            id_filt = book_details['Id']
        except Exception as e:
            st.error("No se pudo cargar la imagen. Por favor, inténtelo más tarde.")

if libro:
    try:
        st.title('Te recomendamos los siguientes libros')
        col1, col2, col3 = st.columns(3)
        matriz = hacer_recomendacion(id_filt)
        recomendados = dflibros[dflibros['Id'].isin(matriz['id2'])].reset_index()
        df_merged = pd.merge(matriz, recomendados, left_on='id2', right_on='Id', how='left')
        with col1:
            st.write(recomendados.loc[0,'Title'])
            st.image(matriz.loc[0,'image'])
        with col2:
            st.write(recomendados.loc[1,'Title'])
            st.image(matriz.loc[1,'image'])
        with col3:
            st.write(recomendados.loc[2,'Title'])
            st.image(matriz.loc[2,'image'])
        
        # Crear gráfico de barras horizontales con Plotly
        st.title('Similitud entre los libros')
        fig = px.bar(df_merged, x='similitud', y='Title', orientation='h')
        # Mostrar gráfico en Streamlit
        st.plotly_chart(fig)
        
    except Exception as e:
        st.error("No se pudieron obtener recomendaciones, intente con otro libro.")
