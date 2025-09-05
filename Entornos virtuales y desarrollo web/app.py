import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Visualización de datos de anuncios de venta de coches')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# seleccionar rango de precio con un deslizador
min_price, max_price = st.slider(
    'Selecciona el rango de precio de los coches',
    int(car_data['price'].min()),  # valor mínimo del deslizador
    int(car_data['price'].max()),  # valor máximo del deslizador
    (int(car_data['price'].min()), int(
        car_data['price'].max()))  # valor por defecto
)
# filtrar los datos según el rango de precio seleccionado
filtered_data = car_data[(car_data['price'] >= min_price) & (
    car_data['price'] <= max_price)]
st.write(
    f'Número de coches en el rango de precio seleccionado: {len(filtered_data)}')
st.dataframe(filtered_data)  # mostrar los datos filtrados en una tabla

# crear un botón para el histograma.
hist_button = st.button('Construir histograma')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x='odometer',
                       title='Histograma del kilometraje(millas) de los coches')
    # agregar etiquetas
    fig.update_layout(
        xaxis_title='Kilometraje (millas)',
        yaxis_title='Cantidad de coches',
        bargap=0.2,  # espacio entre barras
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")

# crear un botón para el diagrama de dispersión.
disp_button = st.button('Construir diagrama de dispersión')
if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un diagrama de dispersión
    fig = px.scatter(car_data, x='model_year', y='price',
                     title='Diagrama de dispersión del modelo respecto al precio de los coches')

    # agregar etiquetas
    fig.update_layout(
        xaxis_title='Modelo del vehículo (año)',
        yaxis_title='Precio (USD)',
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")
    st.write('¡Gracias por usar la aplicación!')
