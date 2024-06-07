import streamlit as st

# Streamlit configuration
st.set_page_config(page_title="DogBreeds Detector", page_icon="🐾", layout="centered", initial_sidebar_state="auto")

# Apply custom CSS for background color and styling
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
    .subtitle {
        font-size: 24px;
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
    .btn-box {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title and logo
st.markdown('<div class="logo-container"><img src="loguito.png" width="200"></div>', unsafe_allow_html=True)
st.markdown('<h1 class="title">Bienvenido a tu Dog Breed Identifier</h1>', unsafe_allow_html=True)

# "Sobre Nosotros" section
st.markdown('<h2 class="subtitle">Sobre Nosotros</h2>', unsafe_allow_html=True)
st.markdown('<div class="info-box">DogBreeds Detector es una aplicación diseñada para ayudarte a conocer más sobre tu perro. Con solo una foto, nuestra avanzada tecnología puede identificar la raza de tu perro y proporcionarte recomendaciones personalizadas.</div>', unsafe_allow_html=True)
st.markdown('<div class="info-box">**¿Cómo usar la App?**<br>1. Sube una foto de tu perro.<br>2. Haz clic en el botón para identificar la raza.<br>3. Recibe información detallada y recomendaciones personalizadas.</div>', unsafe_allow_html=True)
st.markdown('<div class="info-box">**Beneficios de usar DOGGYS**<br>- Conoce mejor a tu mascota.<br>- Recibe recomendaciones personalizadas para el cuidado de tu perro.<br>- Diferenciación de la app: Nuestra app utiliza un modelo de IA avanzado entrenado con miles de imágenes para garantizar precisión en la identificación.<br>- Consulta a un veterinario: Además de nuestras recomendaciones, te recomendamos siempre consultar con tu veterinario para el mejor cuidado de tu mascota.</div>', unsafe_allow_html=True)

# Button to navigate to the second view
st.markdown('<div class="btn-box"><a href="/vista2" target="_self"><button style="background-color:#8BC34A;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:20px;">Comenzá Aquí</button></a></div>', unsafe_allow_html=True)
