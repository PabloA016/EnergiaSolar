# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 7: Energía Asequible y No Contaminante ''')
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir el impacto de la intensidad solar 
en la energia de salida""")
#Imagen
st.image("Solar.jpg", caption="el impacto de la intensidad solar en la energia de salida")



# Usaremos un deslizador
st.sidebar.header("Intensidad Solar")
#Limites
  # Límite inferior: 200 Limite aproximado en la grafica
  # Límite superior: 1200 Limite un poc mas alto de que 1000 (limite que se ve en la garfica)
temp_input = st.sidebar.slider("Temperatura del Agua (°C)", 200.0, 1200.0)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('EnergiaClean.csv', encoding='latin-1')
# Seleccionamos las variables
X = df[['VAR_2']]
y = df['VAR_4']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*temp_input

# Presentamos loa resultados
st.subheader(' Prediccion Energia Solar de Salida con Intensidad de Radiacion Solar')
st.write(f'El porcentaje de blanqueamiento es: {prediccion:.2f}%')

