import streamlit as st

# Configuración de página y estilos CSS personalizados
st.set_page_config(
    page_title="DOGGYS",
    page_icon=":dog:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Contenido de la sidebar
with st.sidebar:
    st.markdown("## 🐶 DOGGYS")
    st.write("Consejos, recomendaciones y más...")

    st.markdown("---")

    # Campos de entrada de contacto
    st.markdown("### Contáctanos para más información!")
    email = st.text_input("Email")
    phone = st.text_input("Teléfono")

    # Botón para enviar la información
    if st.button("Enviar Información"):
        st.write("Información enviada:")
        st.write(f"Email: {email}")
        st.write(f"Teléfono: {phone}")

    st.markdown("---")
    st.write("Gracias por utilizar DOGGYS!")

col1, col2, col3 = st.columns(3)

with col2:
    st.image('loguito.png', caption=None, width=400, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

# Estilos CSS para fondo y logo
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f5dc;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #5d3a1a;
        text-align: center;
        margin-bottom: 20px;
    }
    .info-box {
        font-size: 18px;
        color: #5d3a1a;
        padding: 20px;
        background-color: #faf0e6;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 40px;
    }
    .stButton button {
        background-color: #804000;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #955f34;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal y logo
st.markdown('<h1 class="title">Descubre recomendaciones personalizadas para tu mascota</h1>', unsafe_allow_html=True)

# Función para generar recomendaciones según la raza ingresada
recommendations = {
    "Beagle": """
    *Alimentación* 🍖:
    - Comida rica en proteínas de alta calidad.
    - Controlar las porciones para evitar la obesidad.

    *Cuidados específicos* 🐕:
    - Revisar sus orejas regularmente para evitar infecciones.
    - Cepillado semanal y ejercicio diario.

    *Consejos* 💡:
    - Proveer juguetes para mantenerlos ocupados, ya que son curiosos y activos.
    """,
    "Bearded Collie": """
    *Alimentación* 🍗:
    - Dieta rica en proteínas y carbohidratos de calidad para soportar su energía.

    *Cuidados específicos* 🧼:
    - Cepillado regular para manejar su pelaje doble y denso.

    *Consejos* 🏃:
    - Necesitan mucho ejercicio y estimulación mental, ideales para familias activas.
    """,
    "Bermaise": """
    *Alimentación* 🥩:
    - Dieta rica en proteínas y grasas saludables.

    *Cuidados específicos* 🧼:
    - Cepillado regular debido a su pelaje denso.

    *Consejos* ❄️:
    - Prefieren climas fríos y necesitan espacio para moverse.
    """,
    "Border Collie": """
    *Alimentación* 🍗:
    - Dieta rica en proteínas y carbohidratos de calidad para soportar su energía.

    *Cuidados específicos* 🧼:
    - Cepillado regular para manejar su pelaje doble y denso.

    *Consejos* 🏃:
    - Necesitan mucho ejercicio y estimulación mental, ideales para familias activas.
    """,
    "Boston Terrier": """
    *Alimentación* 🍖:
    - Alimento balanceado adecuado para perros de tamaño pequeño a mediano.

    *Cuidados específicos* 🧽:
    - Revisar sus ojos y orejas regularmente, ya que pueden ser propensos a infecciones.

    *Consejos* 🏠:
    - Son perros sociales y disfrutan de la compañía humana, ideales para la vida en apartamento.
    """,
    "Boxer": """
    *Alimentación* 🥩:
    - Comida rica en proteínas y grasas saludables para mantener su musculatura.

    *Cuidados específicos* 🐾:
    - Ejercicio regular y cuidado de su piel, especialmente en climas cálidos.

    *Consejos* 🏋️:
    - Necesitan mucho ejercicio y son muy leales, ideales para familias activas.
    """,
    "Bull Terrier": """
    *Alimentación* 🍗:
    - Alimento de alta calidad con buen contenido de proteínas.

    *Cuidados específicos* 🛁:
    - Cuidado regular de la piel y los oídos.

    *Consejos* 🎾:
    - Necesitan ejercicio diario y juguetes resistentes debido a su fuerza y energía.
    """,
    "Bulldog": """
    *Alimentación* 🥩:
    - Comida balanceada con control de porciones para evitar la obesidad.

    *Cuidados específicos* 🧼:
    - Limpieza regular de los pliegues de la piel y cuidado dental.

    *Consejos* 🏡:
    - Son ideales para la vida en apartamento y disfrutan de la compañía humana.
    """,
    "Chihuahua": """
    *Alimentación* 🍖:
    - Comida adecuada para perros pequeños con control de porciones.

    *Cuidados específicos* 🧼:
    - Cuidado dental regular y abrigo en climas fríos.

    *Consejos* 🏠:
    - Ideales para la vida en apartamento, necesitan socialización y compañía humana.
    """,
    "Chow": """
    *Alimentación* 🥩:
    - Dieta rica en proteínas y grasas saludables.

    *Cuidados específicos* 🪮:
    - Cepillado regular debido a su pelaje denso.

    *Consejos* ❄️:
    - Prefieren climas fríos y necesitan espacio para moverse.
    """,
    "Dalmation": """
    *Alimentación* 🍖:
    - Comida rica en proteínas y con control de porciones.

    *Cuidados específicos* 🧽:
    - Ejercicio regular y cuidado de su piel, especialmente en climas cálidos.

    *Consejos* 🚴:
    - Necesitan mucho ejercicio y estimulación mental, ideales para familias activas.
    """,
    "Doberman": """
    *Alimentación* 🍗:
    - Dieta rica en proteínas de alta calidad.

    *Cuidados específicos* 🧼:
    - Ejercicio regular y cuidado de la piel.

    *Consejos* 🏃:
    - Necesitan mucho ejercicio y son leales, ideales para dueños experimentados.
    """,
    "German Sheperd": """
    *Alimentación* 🥩:
    - Comida rica en proteínas y grasas de calidad.

    *Cuidados específicos* 🧼:
    - Cepillado regular para manejar la muda y ejercicio diario.

    *Consejos* 🏋️:
    - Necesitan mucho ejercicio y estimulación mental, ideales para tareas de trabajo y compañía.
    """,
    "Golden Retriever": """
    *Alimentación* 🍗:
    - Dieta balanceada con proteínas y grasas saludables.

    *Cuidados específicos* 🧼:
    - Cepillado regular y ejercicio diario.

    *Consejos* 🏊:
    - Son excelentes nadadores y necesitan mucho ejercicio y socialización.
    """,
    "Maltese": """
    *Alimentación* 🍖:
    - Comida adecuada para perros pequeños con control de porciones.

    *Cuidados específicos* 🧼:
    - Cepillado diario y cuidado dental regular.

    *Consejos* 🏠:
    - Ideales para la vida en apartamento, necesitan socialización y compañía humana.
    """,
    "Newfoundland": """
    *Alimentación* 🍗:
    - Alimento de alta calidad adecuado para razas grandes.

    *Cuidados específicos* 🪮:
    - Cepillado regular debido a su pelaje denso y ejercicio diario.

    *Consejos* 🛶:
    - Son excelentes nadadores y necesitan espacio para moverse.
    """,
    "Pekinese": """
    *Alimentación* 🍖:
    - Comida adecuada para perros pequeños con control de porciones.

    *Cuidados específicos* 🧼:
    - Cepillado regular y cuidado dental.

    *Consejos* 🏠:
    - Ideales para la vida en apartamento, necesitan socialización y compañía humana.
    """,
    "Pinscher": """
    *Alimentación* 🥩:
    - Comida rica en proteínas de alta calidad.

    *Cuidados específicos* 🧽:
    - Cuidado regular de la piel y ejercicio diario.

    *Consejos* 🏃:
    - Necesitan mucho ejercicio y son muy activos, ideales para dueños experimentados.
    """,
    "Pitbull": """
    *Alimentación* 🍖:
    - Comida rica en proteínas y con control de porciones.

    *Cuidados específicos* 🧼:
    - Ejercicio regular y cuidado de la piel.

    *Consejos* 🏋️:
    - Necesitan mucho ejercicio y son leales, ideales para dueños experimentados.
    """,
    "Poodle": """
    *Alimentación* 🍗:
    - Dieta balanceada con proteínas y grasas saludables.

    *Cuidados específicos* 🧼:
    - Cepillado regular y cuidado dental.

    *Consejos* 🏠:
    - Son muy inteligentes y necesitan estimulación mental y ejercicio diario.
    """,
    "Pug": """
    *Alimentación* 🍖:
    - Comida adecuada para perros pequeños con control de porciones.

    *Cuidados específicos* 🧼:
    - Cuidado regular de la piel y los ojos.

    *Consejos* 🏠:
    - Ideales para la vida en apartamento, necesitan socialización y compañía humana.
    """,
    "Rottweiler": """
    *Alimentación* 🍗:
    - Dieta rica en proteínas de alta calidad.

    *Cuidados específicos* 🧼:
    - Ejercicio regular y cuidado de la piel.

    *Consejos* 🏋️:
    - Necesitan mucho ejercicio y son leales, ideales para dueños experimentados.
    """,
    "Shar Pei": """
    *Alimentación* 🥩:
    - Comida rica en proteínas y grasas saludables.

    *Cuidados específicos* 🧼:
    - Limpieza regular de los pliegues de la piel y cuidado dental.

    *Consejos* 🏡:
    - Son ideales para la vida en apartamento y disfrutan de la compañía humana.
    """,
    "Shih Tzu": """
    *Alimentación* 🍖:
    - Comida adecuada para perros pequeños con control de porciones.

    *Cuidados específicos* 🧼:
    - Cepillado regular y cuidado dental.

    *Consejos* 🏠:
    - Ideales para la vida en apartamento, necesitan socialización y compañía humana.
    """,
    "Siberian Husky": """
    *Alimentación* 🍗:
    - Dieta rica en proteínas y carbohidratos de calidad para soportar su energía.

    *Cuidados específicos* 🧼:
    - Cepillado regular para manejar su pelaje doble y denso.

    *Consejos* 🏃:
    - Necesitan mucho ejercicio y estimulación mental, ideales para familias activas.
    """,
    "Yorkshire Terrier": """
    *Alimentación* 🍖:
    - Comida adecuada para perros pequeños con control de porciones.

    *Cuidados específicos* 🧼:
    - Cepillado regular y cuidado dental.

    *Consejos* 🏠:
    - Ideales para la vida en apartamento, necesitan socialización y compañía humana.
    """
}

# Lista de razas disponibles
breed_list = [
    "Beagle", "Bearded Collie", "Bermaise", "Border Collie", "Boston Terrier", "Boxer", 
    "Bull Terrier", "Bulldog", "Chihuahua", "Chow", "Dalmation", "Doberman", 
    "German Sheperd", "Golden Retriever", "Maltese", "Newfoundland", "Pekinese", 
    "Pinscher", "Pitbull", "Poodle", "Pug", "Rottweiler", "Shar Pei", "Shih Tzu", 
    "Siberian Husky", "Yorkshire Terrier"
]

# Selección de raza desde una lista desplegable
selected_breed = st.selectbox('Selecciona la raza de tu perro:', breed_list)

# Mostrar recomendaciones según la raza seleccionada
import streamlit as st
import webbrowser

# Lista de veterinarias en Buenos Aires (ejemplo)
veterinarias = [
    {"nombre": "Veterinaria Central", "lat": -34.6021, "lon": -58.3845},
    {"nombre": "Vet Amigos", "lat": -34.6035, "lon": -58.3800},
    {"nombre": "Animal Health", "lat": -34.6040, "lon": -58.3820},
    {"nombre": "Pet Care", "lat": -34.6010, "lon": -58.3870},
    {"nombre": "Pet Hospital", "lat": -34.6005, "lon": -58.3855},
    {"nombre": "Clínica Veterinaria Norte", "lat": -34.6050, "lon": -58.3835},
    {"nombre": "Veterinaria Paws", "lat": -34.6065, "lon": -58.3880},
    {"nombre": "Pet Life", "lat": -34.6070, "lon": -58.3865},
    {"nombre": "Vet Plus", "lat": -34.6080, "lon": -58.3890},
    {"nombre": "Animal Care", "lat": -34.6090, "lon": -58.3905},
    {"nombre": "Pet House", "lat": -34.6100, "lon": -58.3910},
    {"nombre": "Veterinaria Sur", "lat": -34.6110, "lon": -58.3920},
    {"nombre": "Vet Clinic", "lat": -34.6120, "lon": -58.3930},
    {"nombre": "Animal Clinic", "lat": -34.6130, "lon": -58.3940},
    {"nombre": "Pet World", "lat": -34.6140, "lon": -58.3950},
    {"nombre": "Vet 24/7", "lat": -34.6150, "lon": -58.3960},
    {"nombre": "Animal Health Care", "lat": -34.6160, "lon": -58.3970},
    {"nombre": "Vet Express", "lat": -34.6170, "lon": -58.3980},
    {"nombre": "Pet Vet", "lat": -34.6180, "lon": -58.3990},
    {"nombre": "Animal Friends", "lat": -34.6190, "lon": -58.4000}
]

if selected_breed:
    st.markdown(f"### Recomendaciones para {selected_breed}")
    st.markdown(recommendations[selected_breed])

    with st.expander("Mapa de Veterinarias 🗺️🌿"):
        user_location = st.text_input("Ingrese su dirección para encontrar veterinarias cercanas:")

        if user_location:
            st.write(f"Ubicación ingresada: {user_location}")
            if st.button("Ver veterinarias cercanas en Google Maps"):
                # Utilizar la búsqueda de Google Maps con la ubicación del usuario
                query = f"veterinarias cercanas {user_location}"
                google_maps_url = f"https://www.google.com/maps/search/{query}"
                webbrowser.open_new_tab(google_maps_url)
                st.write("Abriendo Google Maps para mostrar veterinarias cercanas...")


                