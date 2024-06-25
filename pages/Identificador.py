from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import streamlit as st
import os

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

col1, col2, col3 = st.columns(3)

with col2:
    st.image('loguito.png', caption=None, width=400, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    

# Obtener la ruta absoluta al directorio que contiene el script
script_dir = os.path.dirname(os.path.abspath(__file__))

def classify_dog(img):
    np.set_printoptions(suppress=True)
    model_path = os.path.join(script_dir, "..", "modelo", "keras_model.h5")
    if not os.path.exists(model_path):
        st.error(f"Modelo no encontrado en {model_path}")
        return None, None

    model = load_model(model_path, compile=False)
    labels_path = os.path.join(script_dir, "..", "modelo", "labels.txt")
    if not os.path.exists(labels_path):
        st.error(f"Archivo de etiquetas no encontrado en {labels_path}")
        return None, None

    class_names = open(labels_path, "r").readlines()

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img.convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name, confidence_score

# Función para generar recomendaciones según el label
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

def generate_recipe(label):
    if label in recommendations:
        return recommendations[label]
    else:
        return "No se encontraron recomendaciones para esta raza."

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
    .upload-box {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .btn-box {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .columns {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 20px;
    }
    .column {
        flex: 1;
        margin: 10px;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 40px;
    }
    .recommendations {
        padding: 20px;
        background-color: #faf0e6;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 40px;
    }
    .recommendations p {
        font-size: 18px;
        color: #5d3a1a;
        margin-bottom: 10px;
    }
    .more-btn {
        background-color: #5d3a1a;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        text-decoration: none;
    }
    .more-btn:hover {
        background-color: #824c1a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title and logo
st.markdown('<h1 class="title">Comienza tu aventura junto a tu mascota</h1>', unsafe_allow_html=True)

# Upload box
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
input_img = st.file_uploader("", type=['jpg', 'png', 'jpeg'])
st.markdown('</div>', unsafe_allow_html=True)

# Button box
st.markdown('<div class="btn-box">', unsafe_allow_html=True)
if input_img is not None:
    if st.button("Determinar la raza"):
        # Columns for displaying results
        st.markdown('<div class="columns">', unsafe_allow_html=True)

        with st.container():
            st.markdown('<div class="info-box">Imagen cargada</div>', unsafe_allow_html=True)
            st.image(input_img, use_column_width=True)

        with st.container():
            st.subheader('Resultado')
            image_file = Image.open(input_img)

            with st.spinner('Analizando imagen...'):
                label, confidence_score = classify_dog(image_file)
                if label is not None and confidence_score is not None:
                    label_description = label.split(maxsplit=1)[1].strip()  # To get breed name
                    st.session_state['label'] = label_description

                    if confidence_score < 0.89:
                        st.error("No pudimos identificar a tu mascota. Por favor, adjunta otra foto.")
                    else:
                        st.success(f"Raza: {st.session_state['label']}")
                        st.write(f"Seguridad de identificación: {confidence_score * 100:.2f}%")

                        # Mostrar recomendaciones si la confianza es alta
                        st.subheader('Recomendaciones')
                        result = generate_recipe(label_description)
                        st.markdown(result, unsafe_allow_html=True)

                else:
                    st.error("No se pudo clasificar la raza del perro.")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st

# Agregar estilos CSS personalizados
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: white;
        color: black;
        border: 2px solid black;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Button to navigate to the second view
st.markdown('<div class="btn-box"><a href="/Conozco_la_raza" target="_self"><button style="background-color:#804000;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:20px;">Ya se la raza de mi perro</button></a></div>', unsafe_allow_html=True)