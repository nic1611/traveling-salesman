import warnings
warnings.filterwarnings('ignore')  # Hide warnings
from streamlit_folium import folium_static 
import streamlit as st
import folium
from model import geneticAlgorithm, City


cityList = []

cityList.append(City('Parque Barigui',-25.4227643,-49.2982402))
cityList.append(City('Praça Himeji',-25.417052,-49.284218))
cityList.append(City('Memorial Ucraniano',-25.4080748,-49.307594))
cityList.append(City('Passeio Público',-25.4225115,-49.2692025))
cityList.append(City('Museu Egípcio e Rosacruz Tutankhamon',-25.4185763,-49.2686276))
cityList.append(City('Museu Oscar Niemeyer',-25.4304207,-49.3135014))
cityList.append(City('Bosque Alemão',-25.4211749,-49.3103135))
cityList.append(City('Bosque Santa Paula',-25.4405695,-49.3106117))
cityList.append(City('Parque Vista Alegre',-25.4106347,-49.3132573))
cityList.append(City('Parque Bacacheri - Boa Vista - PR',-25.3926211,-49.2464161))


st.title('Caixeiro-viajante')

st.sidebar.header('Escolha novas coordenadas')

with st.sidebar.form("my_form"):
        name = st.text_input('Nome')
        new_latitude = st.number_input('Latitude')
        new_logitude = st.number_input('Logitude')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
                if new_latitude == '' or new_logitude == 0 or name == 0:
                        st.write("Preencha todos os campos")
                else:
                        cityList.append(City(name,new_latitude,new_logitude))





best_route = geneticAlgorithm(population=cityList, popSize=100, eliteSize=6, mutationRate=0.01, generations=30)

trace_path = folium.Map(
    location=[-25.4225115,-49.2692025],    # Coordenadas retiradas do Google Maps
    zoom_start=13
)

for i in range(0, len(best_route)):
    folium.Marker(
        location=[best_route[i].x, best_route[i].y],
        popup=best_route[i].name
    ).add_to(trace_path)

locations = [(item.x, item.y) for item in best_route]

folium.PolyLine(locations,
                color='blue',
                weight=5,
                opacity=0.8).add_to(trace_path)

st.subheader('Melhor caminho encontrado')
folium_static(trace_path)

# st.subheader('Grafico de Valores Médios Móveis')
# st.plotly_chart(fig1)