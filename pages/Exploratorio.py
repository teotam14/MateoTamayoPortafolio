import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Configuración de la página
st.set_page_config(page_title="Exploratorio",page_icon='📉')
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
    st.title("Análisis exploratorio de datos para ML")
with col2:
    if st.button(" 🔙 página principal"):
        st.switch_page('Portafolio.py')


#DOWNLOAD_ROOT es la base del GitHub donde vamos a estar descargando las bases de datos.
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/a2Proyectos/MachineLearning_Data/main/"
#Complementos con la dirección especifica de la base de datos que queremos.
MEDICAMENTOS = "Capitulo_3/drug200.csv"

def extraer_datos(root,database):
    csv_path = root + database
    return pd.read_csv(csv_path)

# Cargando datos en un DF
df = extraer_datos(DOWNLOAD_ROOT,MEDICAMENTOS)

st.write("""El set de datos que vamos a analizar contiene información de paciencientes de un centro médico, 
         incluyendo su edad, sexo, presión sanguínea, colosterol, indicador de sodio a potasio en la sangre,
         y el tipo de droga que se le recetó a cada paciente para tratar una enfermedad sanguínea. Se
         analizará el pequeño set de datos, teniendo en cuenta que se quiere predecir el tipo de droga
         que se le debe asignar a un paciente nuevo de acuerdo a las demás variables.""")

st.write('Dale un pequeño vistazo a los datos:')
st.table(df.head())

##ANALISIS DE CADA VARIABLE

#Gráfica la variable 
#Establece una área de figsize(9,5) es decir, el tamaño de la imagen
st.write("""Analizando la variable edad, se puede observar que los datos presentan una distribución
         aproximadamente uniforme, lo que nos dá un indicio de que todas las edades están bien representadas
         dentro del estudio y no vamos a tener un sesgo.""")
plt.figure(figsize = (7,3))
gr1 = sns.displot(df['Age'], kde = True)
st.pyplot(gr1)


st.write("""Tanto la presión sanguínea (alta, normal, baja) colo el colesterol (alto y normal) representan
         aproximadamente 1/3 y 1/2 de los datos respectivamente por lo que no generarán ruido en los
         resultado, aunque se destaque un poco mas las personas con colesterol alto que los normles y bajos.""")
plt.figure(figsize = (7,3))
gr2 = sns.histplot(data=df,x="BP",hue="BP")
gr2 = gr2.get_figure()
st.pyplot(gr2)

# Crea una gráfica de barras para Colesterol
plt.figure(figsize = (7,3))
gr3 = sns.histplot(data=df,x="Cholesterol",hue="Cholesterol")
gr3 = gr3.get_figure()
st.pyplot(gr3)

# Crea un displot para Sodio Potasio
st.write("""Los datos de la vriable de sodio a potasio tienen una distribución aproximadamente normal
         con una asimetría positiva.""")
plt.figure(figsize = (9,5))
gr4 = sns.displot(df.Na_to_K,kde=True)
st.pyplot(gr4)


st.write("""Observando los datos que queremos predecir, podemos anticiparnos a las dificultades que tendrá
         cualquier modelo de machine learning para clasificar a una persona en los medicamentos B y C, 
         a causa de los pocos datos que se tienen sobre ellas, y se espera que se tenga una mejor
         precisión para el medicamento Y.""")
plt.figure(figsize = (9,5))
gr5 = sns.histplot(data=df,x="Drug",hue="Drug")
gr5 = gr5.get_figure()
st.pyplot(gr5)


from pandas.plotting import scatter_matrix
st.write("""La relación entre las 2 variables predictoras que tiene el dataset (edad y nivel de sodio a potasio)
         es practicamente nula entre ellas, su relación tiene un alto componente aleatorio y no afectará los
         resultados de la predicción.""")
#Para graficar scatter_matrix...
columns = ['Age','Na_to_K']
gr9 = scatter_matrix(df[columns], figsize = (12, 12), color = '#D52B06', alpha = 0.3, 
               hist_kwds = {'color':['bisque'], 'edgecolor': 'firebrick'});
gr9 = gr9[0, 0].get_figure()
st.pyplot(gr9)


st.write("""Ahora, comparando estas 2 variables numéricas con la variable a predecir, se observa que
         la edad solo es influyente para diferencia entre la droga B y A. Mientras que la dorga A la
         reciben personas menores de 50 años, la dorga B la reciben mayores, pero el resto de medicamentos
         no tienen diferencia alguna por edad.""")
plt.figure(figsize = (9,5))
gr6 = sns.swarmplot(x = "Drug", y = "Age",data = df,hue='Drug')
plt.legend(df['Drug'])
plt.title("Edad/Medicamento")
gr6 = gr6.get_figure()
st.pyplot(gr6)

#Grafica (con un swarmplot) la relación entre el nivel de Sodio-Potasio y los medicamentos 💊 que se les da
st.write("""En cuanto al sodio a potasio, los datos solo nos permiten identificar que la dorga Y se le
         receta a personas con un nivel mayor a 15, de resto se distribuyen cualquiera de los otros
         medicamentos.""")
plt.figure(figsize = (9,5))
gr7 = sns.swarmplot(x = "Drug", y = "Na_to_K",data = df, hue='Drug')
plt.title("Sodio-Potasio/Medicamentos")
gr7 = gr7.get_figure()
st.pyplot(gr7)

# Grafica la relación entre la Presión Sanguínea y los Medicamentos 💊
st.write("""Para la presión sanguínea y su relación con los tipos de medicamentos, la dorga A y B
         son solo recetadas a personas con presión sanguínea alta, esto probablemente ayudará al
         modelo a clasificar este tipo de drogas que no tienen tanta información en las otras variables
         que hemos analizado.""")
df_BP_Drug = df.groupby(["Drug","BP"]).size().reset_index(name = "Count")
plt.figure(figsize = (9,5))
gr8 = sns.barplot(x = "Drug",y="Count", hue = "BP",data = df_BP_Drug)
plt.title("Presión Sanguinea/Medicamentos")
gr8 = gr8.get_figure()
st.pyplot(gr8)

# Grafica (con una gráfica de barras)nla relación entre el nivel de colesterol y los medicamentos 💊
st.write("""En cuanto al colesterol solo podemos inferir que la droga C es brindada a personas
         con altos niveles de colesterol.""")
df_CH_Drug = df.groupby(["Drug","Cholesterol"]).size().reset_index(name = "Count")
plt.figure(figsize = (9,5))
gr9 = sns.barplot(x = "Drug",y="Count", hue = "Cholesterol",data = df_CH_Drug)
plt.title("Colesterol/Medicamentos")
gr9 = gr9.get_figure()
st.pyplot(gr9)


st.write("""Para el desarrollo de un modelo de machine learning se requiere previamente preporcesar los 
         datos, y aunque nuestro dataset no es muy grande ni contiene muchas variables, hay algunos
         detalles que se deben ajustar. Se deben escalar los datos numéricos para que esten en la misma escala 
         y que el modelo no vaya a presentar confusiones por las escalas tan diferentes que tienen las
         edades y los niveles de sodio a potasio y las variables categóricas se deben codificar para
         pasarlas a numéricas y que el modelo las pueda interpretar.""")

st.write("""En este caso, se aplicó un modelo Random Forest, que es un método de ensamble construido
         a partir de diversos arboles de decisión.""")

st.write("""Validando los resultados del modelo con el set de prueba tenemos la siguiente matriz de confusión,
         donde en la diagonal se encuentran los datos correctamente predichos, teniendo una precisión de 95%.""")

## Utilizar LabelEncoder para procesar variables alfanuméricas como el sexo, BP, Colesterol, étc
from sklearn.preprocessing import LabelEncoder

def label_encoder(datos_categoria):
    le = LabelEncoder()
    df[datos_categoria] = le.fit_transform(df[datos_categoria])

variables = ["Sex","BP","Cholesterol","Na_to_K","Drug"]

for l in variables:
    label_encoder(l)
    
# Crear set de entrenamiento y set de prueba
x = df.drop(["Drug"],axis=1)
y = df['Drug']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 42, shuffle = True)

#Hacer un clasificador de random forest
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)

from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix

y_train_pred = cross_val_predict(rfc, x_train, y_train, cv=3)
conf_mz = confusion_matrix(y_train,y_train_pred)
st.title('Matriz de confusión')
st.table(conf_mz)