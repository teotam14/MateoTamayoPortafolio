import streamlit as st

#Configuración de la página
st.set_page_config(page_title="Retail report",page_icon='🛒',layout='wide')
hide_menu ="""
<style>
#MainMenu {
    visibility:hidden;
}

[data-testid="stSidebar"] {
    display: none !important;
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
    st.markdown(f"<h3 style='text-align:center; font-size: 50px;color: #216D466;'>Reporte Ventas y Entragas Retail</h3>", unsafe_allow_html=True)
with col2:
    if st.button(" 🔙 Ir a la página principal"):
        st.switch_page('Portafolio.py')


# Código del iframe de Power BI (reemplaza con el tuyo)
power_bi_iframe = """
<iframe title="Retail ventas" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=702bee06-ea2d-4de4-88d3-ee2aa159838a&autoAuth=true&ctid=99e1e721-7184-498e-8aff-b2ad4e53c1c2" frameborder="0" allowFullScreen="true"></iframe>
"""

# Insertar el iframe en Streamlit
st.markdown(power_bi_iframe, unsafe_allow_html=True)