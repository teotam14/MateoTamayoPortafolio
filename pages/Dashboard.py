import streamlit as st
import pandas as pd
import plotly.express as px

#Configuración de la página
st.set_page_config(page_title="Reporte de ventas",page_icon='🛒',layout='wide')
hide_menu ="""
<style>
#MainMenu {
    visibility:hidden;
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
st.markdown(f"<h3 style='text-align:center; font-size: 50px;color: #9f0000;'>Dashboard ventas Streamlit</h3>", unsafe_allow_html=True)

#Cargando datos
df = pd.read_excel('Reporte de Ventas.xlsx', sheet_name='BASE DE DATOS')
print(df.head())

#Barra lateral
st.sidebar.header('Filtros')

#Filtros en barra lateral
vendedor = st.sidebar.multiselect('Seleccione el vendedor',
                       options = df['Vendedor'].unique(),
                       default = df['Vendedor'].unique())

status_factura = st.sidebar.multiselect('Factura pagada',
                                        options = df['Pagada'].unique(),
                                        default = df['Pagada'].unique())

ciudad = st.sidebar.multiselect('Ciudad',
                                options = df['Ciudad'].unique(),
                                default = df['Ciudad'].unique())

industria = st.sidebar.multiselect('Industria',
                                    options = df['Industria'].unique(),
                                    default = df['Industria'].unique())

terminos = st.sidebar.multiselect('Terminos',
                                options = df['Términos'].unique(),
                                default = df['Términos'].unique())

cliente = st.sidebar.multiselect('Cliente',
                                options = df['Cliente'].unique(),
                                default = df['Cliente'].unique())

#Conectar filtros con los datos
df_filtros = df.query('Vendedor == @vendedor & Ciudad == @ciudad & Pagada == @status_factura & Industria == @industria & Cliente == @cliente & Términos == @terminos')

#Indicadores
total_ventas = int(df_filtros['Valor'].sum())
total_facturas = int(df_filtros['Valor'].count())
venta_promedio = int(df_filtros['Valor'].mean())

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('ventas totales')
    st.subheader(f'$ {total_ventas:,}')
    
with col2:
    st.subheader('Número de facturas')
    st.subheader(f'{total_facturas}')
    
with col3:
    st.subheader('Venta promedio')
    st.subheader(f'$ {venta_promedio:,}')

st.write('---')

#Grafico de barras
ventas_industria = df_filtros.groupby(by=['Industria']).agg({'Valor' : 'sum'}).sort_values(by='Valor', ascending=True)
grafico1 = px.bar(ventas_industria,x='Valor', y=ventas_industria.index, color_discrete_sequence=['#9f0000'], title='Ventas por industria')

col4, col5 = st.columns(2)
col4.plotly_chart(grafico1, use_container_width=True)

#Grafico de torta
ventas_ciudad = df_filtros.groupby(by=['Ciudad']).agg({'Valor' : 'sum'}).sort_values(by='Valor', ascending=True)
grafico2 = px.pie(ventas_ciudad,ventas_ciudad.index, 'Valor', title='Ventas por ciudad')
col5.plotly_chart(grafico2, use_container_width=True)

grafico3 = px.line(df_filtros.sort_values(by='fecha documento'), 'fecha documento', 'Valor', title='Ventas')
st.plotly_chart(grafico3, use_container_width=True)

st.write('Detalle ventas')
st.table(df_filtros.head(10))