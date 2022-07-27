# importar librerías
from doctest import DocFileSuite
from tabnanny import check
import streamlit.components.v1 as components
import streamlit as st # !pip install Streamlit
from PIL import Image # !pip install Pillow
import pandas as pd
import texto as t

# configurar la página
def config_page():
    st.set_page_config(
        page_title = 'Calidad del aire en Madrid ',
        page_icon = ':city_sunset:',
        layout = 'wide'
    )

# caché
st.cache(suppress_st_warning=True)

# cargar los datos
def cargar_datos(path):
    df = pd.read_csv(path, sep=",")
    # df.rename(columns={'latidtud':'lat', 'longitud':'lon'}, inplace=True)
    return df
# HOME
def home(df):
    img = Image.open('madrid.jpg')
    st.image(img,use_column_width='madrid')
    with st.expander('¿Quieres saber más?'):
        st.write(t.texto_nox)
    pass
    
    with st.expander('¿Quieres saber más+?'):
        st.write(t.texto_PM25)
    pass
    
    with st.expander('¿Quieres saber más++?'):
        st.write(t.texto_ozono)
    pass

    with st.expander('¿Quieres saber más+++?'):
        st.write(t.texto_info)
    pass


# DATOS
def datos(df):
    # Dos formas de mostra una tabla
    st.write(df)
    #st.table(df)

    # Mostrar un mapa
    st.map(df) #solo funciona si tienes internet

    # Mostrar una tabla filtrada

    nc_distrito=pd.DataFrame(df.groupby('name')['magnitud'].value_counts())
    st.write(nc_distrito)

    # Mostrar archivo html
    filehtml = open('heatmap.html','r')
    sc = filehtml.read()
    components.html(sc, height=700 )


# FILTROS
def filtros(df):
    #Crearnos un desplegable
    #st.write(df)
    list_dis = list(df['magnitud'].unique())
    filtro_dis = st.sidebar.selectbox('Selecciona un contaminate',list_dis)
    df = df[df['magnitud'] == filtro_dis]
    st.write(df)
    #desplegable 2
    list_dis2= list(df['name'].unique())
    filtro_dis2= st.sidebar.selectbox('Selecciona una estación de control',list_dis2)
    df = df[df['name'] == filtro_dis2]
    st.map(df) #solo funciona si tienes internet

    #desplegable 3
    list_dis3 = list(df['anno'].unique())
    filtro_dis3 = st.sidebar.selectbox('Selecciona un año',list_dis3)
    df = df[df['anno'] == filtro_dis3]
    st.write(df)
    
    # Crear un check box (varias opciones)

    #selecciona un intervalo de meses 

    st.sidebar.write('¿Quieres seleccionar un intervalo de meses')
    check_op = st.sidebar.checkbox('Filtrar por meses')
    # if check_op:
    #     list_op = list(df['mes'].unique())
    #     filtro_op = st.sidebar.selectbox('Selecciona un intervalo de meses',list_op)
    #     df = df[df['mes'] == filtro_op]
    #     st.write(df)

    # elif check_nc: 
    #     c_min = df['Nº CARGADORES'].min()
    #     c_max = df['Nº CARGADORES'].max()

    #     if c_min != c_max:
    #         intervalo = range(c_min,c_max+1)
    #         filtro_nc = st.sidebar.select_slider('Selecciona el intervalo',intervalo, value=(c_min,c_max))
    #         mask1 = df['Nº CARGADORES'] >= filtro_nc[0]
    #         mask2 = df['Nº CARGADORES'] <= filtro_nc[1]
    #         df = df[mask1&mask2]
    #         #st.write(df)

   

    