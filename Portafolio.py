import streamlit as st
from streamlit_option_menu import option_menu

#Configuración de la página
st.set_page_config(page_title="Mateo Tamayo",page_icon='📊')

hide_menu ="""
<style>
#MainMenu {
    visibility:hidden;
}

[data-testid="stApp"] {
    background-color: #020212;
    opacity: 0.8;
    background-image: radial-gradient(#232cd1 0.5px, #020212 0.5px);
    background-size: 10px 10px;
}

[data-testid="stHeader"] {
    background-color: #020212;
    opacity: 1;
    background-image: radial-gradient(#232cd1 0.5px, #020212 0.5px);
    background-size: 10px 10px;
}

[data-testid="stSidebar"] {
    display: none !important;
}
"""
st.markdown(hide_menu,unsafe_allow_html=True)

#Contenido principal de la página
st.markdown(f"<h3 style='text-align:center; font-size: 25px;'>Hola! ✌🏼 Soy</h3>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align:center; font-size: 75px;color: #00a4f6;'>Mateo Tamayo</h3>", unsafe_allow_html=True)

#Descripción general
st.write("""
         Un ingeniero industrial con énfasis en analítica de datos, y desde entonces 
         me he apasionado por el poder que pueden llegar a tener los datos desde sus diferentes aplicaciones
         en variedad de industrias...
         """)

# Social Icons
linkedin_icon = "imagenes/github.png"
github_icon = "imagenes/linkedin.png"
social_icons_data = {
    # Platform: [URL, Icon]
    "LinkedIn": ["https://www.linkedin.com/in/mateo-andres-tamayo-quiros/", "https://cdn.icon-icons.com/icons2/2429/PNG/512/linkedin_logo_icon_147268.png"],
    "GitHub": ["https://github.com/teotam14", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"]
    }

social_icons_html = [
    f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 20px;'>"
    f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}' style='width: 30px; height: 30px;filter: brightness(20.5);'>"
    "</a>" 
    for platform in social_icons_data
]

st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 2px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

st.markdown(f"<div style='height: 3px;background-color: #00a4f6; margin: 10px 0 20px 0'></div>", unsafe_allow_html=True)

#Opciones del portafolio
selected = option_menu(
    menu_title = None,
    options = ['Acerca de', 'Proyectos', 'Contacto'],
    icons = ['person', 'code-slash', 'chat-left-text-fill'],
    orientation = 'horizontal',
    styles={
            "container": {"background-color": "#555", "color": "white"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"font-size": "15px", "text-align": "left","margin":"0px", "--hover-color": "#eee", "color": "white"},
            "nav-link-selected": {"background-color": "#00a4f6", "color": "white", "font-weight": "bold"},
        } 
)
st.markdown(f"<div style='height: 3px;background-color: #00a4f6; margin: 0px 0;'></div>", unsafe_allow_html=True)

imagenes = ["⚙️", "📊", "📈", "🛠️"]
nombre_proyectos = ["Recomendador", "BI Report Retail", "Dashboard Streamlit","Análisis exploratorio"]
ver_mas = ["Proyecto 1", "Proyecto 2", "Proyecto 3","Proyecto 4"]
pagina = ['pages/Recomendaciones.py','pages/RetailBI.py','pages/Dashboard.py','pages/Exploratorio.py']


#Contenido de cada opción
#Acerca de mí
if selected == 'Acerca de':
    #Skills
    st.write(" ")
    st.markdown(f"<h3 style='text-align:center; font-size: 30px;color: #00a4f6;'>Mis principales skills</h3>", unsafe_allow_html=True)
    st.write(" ")
    col3, col4, col5, col6 = st.columns(4)
    with col3:
        st.markdown(f'<img src="https://1000logos.net/wp-content/uploads/2022/08/Microsoft-Power-BI-Logo-768x432.png" style="width: 80px; height: 50px;display: block; margin: auto;">',
                        unsafe_allow_html=True
                    )
        st.markdown(f" <div style='height: 3px;background-color: #4682B4; margin: 10px; max-width: 180px;'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; font-size: 17px;color: white;'>Power BI</h3>", unsafe_allow_html=True)
        st.write(" ")
        st.write(" ")
        st.markdown("<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Pandas_mark.svg/1200px-Pandas_mark.svg.png' style='width: 50px; height: 50px;display: block; margin: auto;'>",
                       unsafe_allow_html=True
                    )
        st.markdown(f" <div style='height: 3px;background-color: #4682B4; margin: 10px; max-width: 180px;'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; font-size: 17px;color: white;'>Pandas</h3>", unsafe_allow_html=True)
    with col4:
        st.markdown("<img src='https://cdn-icons-png.flaticon.com/512/4492/4492311.png' style='width: 50px; height: 50px;display: block; margin: auto;'>",
                       unsafe_allow_html=True
                    )
        st.markdown(f"<div style='height: 3px;background-color: #4682B4; margin: 10px; max-width: 180px;'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; font-size: 17px;color: white;'>SQL</h3>", unsafe_allow_html=True)
        st.write(" ")
        st.write(" ")
        st.markdown("<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/2560px-NumPy_logo_2020.svg.png' style='width: 90px; height: 50px;display: block; margin: auto;'>",
                       unsafe_allow_html=True
                    )
        st.markdown(f" <div style='height: 3px;background-color: #4682B4; margin: 10px; max-width: 180px;'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; font-size: 17px;color: white;'>Numpy</h3>", unsafe_allow_html=True)
    with col5:
        st.markdown("<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Tableau_Logo.png/640px-Tableau_Logo.png' style='width: 130px; height: 50px;display: block; margin: auto;'>",
                       unsafe_allow_html=True
                    )
        st.markdown(f"<div style='height: 3px;background-color: #4682B4; margin: 10px; max-width: 180px;'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; font-size: 17px;color: white;'>Tableau</h3>", unsafe_allow_html=True)
        st.write(" ")
        st.write(" ")
        st.markdown("<img src='https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png' style='width: 70px; height: 50px;display: block; margin: auto;'>",
                       unsafe_allow_html=True
                    )
        st.markdown(f" <div style='height: 3px;background-color: #4682B4; margin: 10px; max-width: 180px;'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; font-size: 17px;color: white;'>Streamlit</h3>", unsafe_allow_html=True)
    with col6:
        st.markdown("<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png' style='width: 50px; height: 50px;display: block; margin: auto;'>",
                       unsafe_allow_html=True
                    )
        st.markdown(f"<div style='height: 3px;background-color: #4682B4; margin: 10px; max-width: 180px;'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; font-size: 17px;color: white;'>Python</h3>", unsafe_allow_html=True)
        st.write(" ")
        st.write(" ")
        st.markdown("<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/2560px-Scikit_learn_logo_small.svg.png' style='width: 80px; height: 50px;display: block; margin: auto;'>",
                       unsafe_allow_html=True
                    )
        st.markdown(f" <div style='height: 3px;background-color: #4682B4; margin: 10px; max-width: 180px;'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; font-size: 17px;color: white;'>Scikitlearn</h3>", unsafe_allow_html=True)
        
    #Experiencia
    st.write(" ")
    st.markdown(f"<h3 style='text-align:center; font-size: 30px;color: #00a4f6;'>Mi experiencia</h3>", unsafe_allow_html=True)
    
    st.markdown("""
<div style="position: relative; height: 300px;">
  <div style="position: absolute; top: 10%; left: 50%; transform: translateX(-50%); width: 2px; height: 80%; background-color: #00a4f6;"></div>
  <div style="position: absolute; top: 5%; left: 50%; transform: translate(-50%, -50%); width: 20px; height: 20px; border-radius: 50%; background-color: #4682B4; border: 2px solid #fff;"></div>
  <div style="position: absolute; top: 35%; left: 50%; transform: translate(-50%, -50%); width: 20px; height: 20px; border-radius: 50%; background-color: #4682B4; border: 2px solid #fff;"></div>
  <div style="position: absolute; top: 65%; left: 50%; transform: translate(-50%, -50%); width: 20px; height: 20px; border-radius: 50%; background-color: #4682B4; border: 2px solid #fff;"></div>
  <div style="position: absolute; top: 95%; left: 50%; transform: translate(-50%, -50%); width: 20px; height: 20px; border-radius: 50%; background-color: #4682B4; border: 2px solid #fff;"></div>
  <div style="position: absolute; top: 15%; left: 60%; transform: translate(-50%, -50%); font-size: 16px; color: white; text-align: center;">Analista de datos</div>
  <div style="position: absolute; top: 20%; left: 62%; transform: translate(-50%, -50%); font-size: 12px; color: white; text-align: center;">Perez y cardona: Compras</div>
  <div style="position: absolute; top: 42%; left: 39%; transform: translate(-50%, -50%); font-size: 16px; color: white; text-align: center;">Practicante analítica</div>
  <div style="position: absolute; top: 47%; left: 37%; transform: translate(-50%, -50%); font-size: 12px; color: white; text-align: center;">Almacenes Flamingo: Retail</div>
  <div style="position: absolute; top: 72%; left: 65%; transform: translate(-50%, -50%); font-size: 15px; color: white; text-align: center;">Analista planeación comercial</div>
  <div style="position: absolute; top: 77%; left: 58%; transform: translate(-50%, -50%); font-size: 12px; color: white; text-align: center;">Cueros Nemiza</div>
</div>
""", unsafe_allow_html=True)
    
    st.write(" ")
    st.write("""
             A lo largo de mi carrera, he tenido la oportunidad de aprender y desarrollar modelos analíticos desde diversas 
             perspectivas de negocio. Utilizando herramientas como Excel, Power BI, SQL y Python, he analizado datos históricos 
             para generar insights valiosos y tomar decisiones fundamentadas. Además, he aplicado técnicas de machine learning para desarrollar modelos predictivos y 
             optimizar procesos empresariales. Mi enfoque se centra en convertir los datos en información significativa que impulse el éxito y la eficiencia operativa de las organizaciones.
             """)
    #Educación
    st.write(" ")
    st.markdown(f"<h3 style='text-align:center; font-size: 30px;color: #00a4f6;'>Educación</h3>", unsafe_allow_html=True)
    
    col7,col8 = st.columns([4,2])
    with col7:
        st.write(f"<span style='color: #4682B4;font-size: 20px;'>&#9733;</span> &nbsp;<span style='font-size: 17px;'>Pregrado: Ingeniería industrial </span>", unsafe_allow_html=True)
        st.write("<p style='font-size: smaller;'>Analítica aplicada, cadena de suministro, machine learning, gestión de proyectos</p>", unsafe_allow_html=True)
        st.write(f"<span style='color: #4682B4;font-size: 22px;'>&#10003;</span> &nbsp;<span style='font-size: 15px;'>Curso: Administración de bases de datos </span>", unsafe_allow_html=True)
        st.write(f"<span style='color: #4682B4;font-size: 22px;'>&#10003;</span> &nbsp;<span style='font-size: 15px;'>Curso: Ciencia de datos Mintic Universidad distrital Francisco José </span>", unsafe_allow_html=True)
        st.write(f"<span style='color: #4682B4;font-size: 22px;'>&#10003;</span> &nbsp;<span style='font-size: 15px;'>Consultoria solidaria U de A: Automatización sitema inventarios</span>", unsafe_allow_html=True)
        st.write(f"<span style='color: #4682B4;font-size: 22px;'>&#10003;</span> &nbsp;<span style='font-size: 15px;'>Curso A2: Python para ciencia de datos</span>", unsafe_allow_html=True)
        st.write(f"<span style='color: #4682B4;font-size: 22px;'>&#10003;</span> &nbsp;<span style='font-size: 15px;'>Curso LinkedIn Learning: SQL Server 2019</span>", unsafe_allow_html=True)
        st.write(f"<span style='color: #4682B4;font-size: 22px;'>&#10003;</span> &nbsp;<span style='font-size: 15px;'>Actualmente: Profundizando mis conocimientos y habilidades en Deep Learning con python</span>", unsafe_allow_html=True)
        st.write(f"<span style='color: #4682B4;font-size: 20px;'>&#9733;</span> &nbsp;<span style='font-size: 17px;'>Próximamente: Esp. Ciencia datos y analítica </span>", unsafe_allow_html=True)

#Imagenes proyectos
imagen = ['Imagenes/Recomendaciones.jpg','Imagenes/Retail.jpg','Imagenes/Dashboard.jpg','Imagenes/Exploratorio.jpg']
    
#Proyectos
if selected == 'Proyectos':
    row1 = st.columns(2)
    row2 = st.columns(2)

    for i, col in enumerate(row1 + row2):
        with col.container(height=280,border=True):
            col1, col2 = st.columns([2,4])
            with col1:
                if st.button(f"{ver_mas[i]}"):
                    st.switch_page(pagina[i])
                    st.markdown(f"<h3 style='text-align:center; font-size: 25px;color: #00a4f6;'>{nombre_proyectos[i]}</h3>", unsafe_allow_html=True)
            with col2:
               st.markdown(f"<h3 style='text-align:center; font-size: 20px;color: #00a4f6;'>{nombre_proyectos[i]}</h3>", unsafe_allow_html=True)
            st.image(imagen[i], use_column_width=True)


#Contacto
if selected == 'Contacto':
    #Correo
    correo = """
    <div style="text-align:center;">
        <div style="width: 100%; border-bottom: 1px solid #ccc;color: #00a4f6; line-height: 0.1em; margin: 40px 0 30px;">
            <span style="background:#00a4f6; color:white;padding:0 10px;">Email</span>
        </div>
        <img src="https://cdn-icons-png.freepik.com/512/668/668189.png" alt="Correo" style="width: 30px; height: 26px; margin-right: 10px;">
        <span style="vertical-align: middle;">mateotamayoquiros@gmail.com</span>
    </div>
    """
    # Mostrar el contenido HTML en Streamlit
    st.markdown(correo, unsafe_allow_html=True)
  
    
    #Telefono
    telefono = """
    <div style="text-align:center;">
        <div style="width: 100%; border-bottom: 1px solid #ccc;color: #00a4f6; line-height: 0.1em; margin: 40px 0 30px;">
            <span style="background:#00a4f6; color:white;padding:0 10px;">Telefono</span>
        </div>
        <img src="https://cdn-icons-png.freepik.com/256/3616/3616230.png" alt="Telefono" style="width: 30px; height: 30px; margin-right: 10px;">
        <span style="vertical-align: left;">+57 319 704 3031</span>
    </div>
    """
    # Mostrar el contenido HTML en Streamlit
    st.markdown(telefono, unsafe_allow_html=True)
    
    msm = """
    <div style="text-align:center;">
        <div style="width: 100%; border-bottom: 1px solid #ccc;color: #00a4f6; line-height: 0.1em; margin: 40px 0 20px;">
            <span style="background:#00a4f6; color:white;padding:0 10px;">MSM</span>
        </div>
    </div>
    """
    # Mostrar el contenido HTML en Streamlit
    st.markdown(msm, unsafe_allow_html=True)
    
    st.write("O enviame un mensaje 😁")
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    mensaje = st.text_area("Mensaje")
    enviar = st.button("Enviar")
    if enviar:
        if not nombre or not email or not mensaje:
            st.error("Por favor, completa todos los campos.")
        else:
            # Lógica para enviar el correo electrónico
            st.success("¡Mensaje enviado con éxito! Te responderé pronto.")
 
    