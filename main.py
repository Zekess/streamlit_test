from Solver_codigos.fun_aux import createdf as crt
import streamlit as st


data = {'Nombre': ['Alvaro'], 'Apellido': ['Guzman']}
df = crt(data)
st.write(df)
st.image('Imagenes_web/Descargas ejemplo.jpg')

