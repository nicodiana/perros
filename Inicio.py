import streamlit as st


# Streamlit configuration


import streamlit as st



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
    st.markdown("### Contactanos para más información!")
    email = st.text_input("Email")
    phone = st.text_input("Teléfono")

# Botón para enviar la información
    if st.button("Enviar Información"):
        st.write("Información enviada:")
        st.write(f"Email: {email}")
        st.write(f"Teléfono: {phone}")
  

    st.markdown("---")

    st.write("Gracias por utilizar DOGGYS!")

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
        background-color: #f9e4b7;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .info-box-title {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .btn-box {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .logo-container {
        display: flex;
        
        margin-bottom: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns(3)

with col2:
    st.image('loguito.png', caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    
# App title and logo

st.markdown('<h1 class="title">Bienvenido a tu Dog Breed Identifier</h1>', unsafe_allow_html=True)

# "Sobre Nosotros" section
st.markdown('<h2 class="subtitle">Sobre Nosotros</h2>', unsafe_allow_html=True)
st.markdown('<div class="info-box"><div class="info-box-title"></div>DogBreeds Detector es una aplicación diseñada para ayudarte a conocer más sobre tu perro. Con solo una foto, nuestra avanzada tecnología puede identificar la raza de tu perro y proporcionarte recomendaciones personalizadas.</div>', unsafe_allow_html=True)
st.markdown('<div class="info-box"><div class="info-box-title">¿Cómo usar la App?</div>1. Sube una foto de tu perro.<br>2. Haz clic en el botón para identificar la raza.<br>3. Recibe información detallada y recomendaciones personalizadas.</div>', unsafe_allow_html=True)
st.markdown('<div class="info-box"><div class="info-box-title">Beneficios de usar DOGGYS</div>- Conoce lo mejor para tu mascota.<br>- Ahorra tiempo y dinero, evitando acciones innecesarias.<br>- Sentite seguro: nuestra app utiliza un modelo de IA avanzado entrenado con miles de imágenes para garantizar precisión en la identificación.<br>- Complementa el cuidado de tu mascota junto con tu veterinario de confianza brindandole lo más adecuado para su bienestar.</div>', unsafe_allow_html=True)

# Button to navigate to the second view
<<<<<<< Updated upstream
st.markdown('<div class="btn-box"><a href="/Identificador" target="_self"><button style="background-color:#804000;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:20px;">Comenzá Aquí</button></a></div>', unsafe_allow_html=True)
=======
st.markdown('<div class="btn-box"><a href="/Identificador" target="_self"><button style="background-color:#804000;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:20px;">Comenzá Aquí</button></a></div>', unsafe_allow_html=True)
>>>>>>> Stashed changes
