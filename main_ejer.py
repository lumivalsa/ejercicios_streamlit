# importar librerías
import streamlit as st
import function_ejer as ft

# configurar la página
ft.config_page()

# cargas los datos
path = '/Users/luismi/Documents/BootCamp_Data_Science/Alumno /ds_thebridge_6_22/taller/Streamlit/taller_streamlit/taller_streamlit/ejercicio_streamlit/air_quality_madrid.csv'
df = ft.cargar_datos(path)

st.title('Calidad del aire en Madrid')

# menú
menu = st.sidebar.selectbox('Selecciona la página',['Home','Datos','Filtros'])

if menu == 'Home':
    ft.home(df)
elif menu == 'Datos':
    ft.datos(df)
else: 
    ft.filtros(df)