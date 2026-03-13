#Importar librerias 
import streamlit as st
import pandas as pd
import plotly.express as px

# Colocar título de tu página
st.header('Mi Primer Panel de Control de Coches')

# Leer los datos
df = pd.read_csv('vehicles_us.csv')

# Botón para el gráfico 1
if st.button('Ver Histograma'):
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)

# Botón para el gráfico 2
if st.button('Ver Gráfico de Dispersión'):
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig)