import streamlit as st

# Configuración de página y estilos CSS personalizados
st.set_page_config(
    page_title="DOGGYS - Reconocimiento de Razas",
    page_icon=":dog:",
    layout="wide",
    initial_sidebar_state="expanded",
)

col1, col2, col3 = st.columns(3)

with col2:
    st.image('loguito.png', caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

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
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal y logo
st.markdown('<h1 class="title">Descubre recomendaciones personalizadas para tu mascota</h1>', unsafe_allow_html=True)

import streamlit as st



# Campo de entrada para el nombre de la raza con estilo mejorado
st.markdown('<p class="input-label">Ingrese la raza de su perro:</p>', unsafe_allow_html=True)
user_input = st.text_input("", "")

# Estilos CSS para el campo de entrada mejorado
st.markdown(
    """
    <style>
    .input-label {
        font-size: 24px;
        font-weight: bold;
        color: #5d3a1a;
        text-align: center;
        margin-bottom: 10px;
    }
    .text-input {
        font-size: 18px;
        padding: 12px;
        border: 2px solid #5d3a1a;
        border-radius: 5px;
        width: 100%;
        max-width: 500px;
        margin: 0 auto;
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True
)



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
    """
    ,

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

    "Pit Bull": """
    *Alimentación* 🥩:
    - Dieta rica en proteínas y grasas de calidad.

    *Cuidados específicos* 🛁:
    - Ejercicio regular y cuidado de la piel.

    *Consejos* 🏋️:
    - Necesitan mucho ejercicio y socialización, ideales para dueños experimentados.
    """,

    "Poodle": """
    *Alimentación* 🍗:
    - Comida balanceada con buen contenido de proteínas.

    *Cuidados específicos* 🧼:
    - Cepillado regular y cuidado dental.

    *Consejos* 🐩:
    - Necesitan ejercicio regular y estimulación mental, ideales para familias activas.
    """,

    "Pug": """
    *Alimentación* 🍖:
    - Comida balanceada con control de porciones para evitar la obesidad.

    *Cuidados específicos* 🧼:
    - Limpieza regular de los pliegues de la piel y cuidado dental.

    *Consejos* 🏡:
    - Son ideales para la vida en apartamento y disfrutan de la compañía humana.
    """,

    "Rottweiler": """
    *Alimentación* 🥩:
    - Dieta rica en proteínas y grasas de calidad.

    *Cuidados específicos* 🧽:
    - Ejercicio regular y cuidado de la piel.

    *Consejos* 🏋️:
    - Necesitan mucho ejercicio y son leales, ideales para familias activas.
    """,

    "Saint Bernard": """
    *Alimentación* 🍖:
    - Alimento de alta calidad adecuado para razas grandes.

    *Cuidados específicos* 🪮:
    - Cepillado regular debido a su pelaje denso y ejercicio diario.

    *Consejos* ⛷️:
    - Necesitan espacio para moverse y son excelentes compañeros de familia.
    """
}

def generate_recommendations(dog_breed):
    if dog_breed in recommendations:
        return recommendations[dog_breed]
    else:
        return f"No se encontraron recomendaciones para la raza {dog_breed}. Por favor, verifique el nombre ingresado."

import streamlit as st

# Estilo personalizado para el botón
st.markdown(
    """
    <style>
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

# Botón para buscar la raza ingresada
if st.button("Buscar Raza"):
    st.markdown('<div class="info-box">Raza ingresada por el usuario</div>', unsafe_allow_html=True)
    st.markdown(f"*Raza ingresada:* {user_input}")

    st.subheader('Recomendaciones')
    result = generate_recommendations(user_input)
    st.markdown(result, unsafe_allow_html=True)