from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import streamlit as st
import os

col1, col2, col3 = st.columns(3)

with col2:
    st.image('loguito.png', caption=None, width=200, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

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
    Alimentación:
    Comida rica en proteínas de alta calidad. Controlar las porciones para evitar la obesidad, ya que tienden a ganar peso fácilmente.
    Cuidados específicos:
    Revisar sus orejas regularmente para evitar infecciones. Cepillado semanal y ejercicio diario.
    Consejos:
    Proveer juguetes para mantenerlos ocupados, ya que son curiosos y activos.
    """,
    "Bearded Collie": """
    Alimentación:
    Alimento balanceado con un buen contenido de proteínas y grasas.
    Cuidados específicos:
    Cepillado frecuente debido a su pelaje largo y denso.
    Consejos:
    Necesitan mucho ejercicio y estimulación mental. Son ideales para familias activas.
    """,
    "Bernese Mountain Dog": """
    Alimentación:
    Alimento de alta calidad adecuado para razas grandes.
    Cuidados específicos:
    Cepillado regular para controlar la muda.
    Consejos:
    Necesitan espacio para moverse y son excelentes compañeros en climas fríos.
    """,
    "Border Collie": """
    Alimentación:
    Dieta rica en proteínas para mantener su alta energía.
    Cuidados específicos:
    Cepillado regular y chequeos veterinarios para detectar problemas oculares comunes en la raza.
    Consejos:
    Requieren mucho ejercicio y entrenamiento para evitar el aburrimiento y conductas destructivas.
    """,
    "Boston Terrier": """
    Alimentación:
    Dieta balanceada y controlada para evitar el sobrepeso.
    Cuidados específicos:
    Limpieza regular de las arrugas faciales y control de la salud ocular.
    Consejos:
    Ejercicio moderado y juguetes interactivos para mantenerlos activos.
    """,
    "Boxer": """
    Alimentación:
    Comida rica en proteínas y grasas saludables.
    Cuidados específicos:
    Ejercicio diario y control de la salud cardíaca.
    Consejos:
    Necesitan socialización y entrenamiento desde cachorros.
    """,
    "Bull Terrier": """
    Alimentación:
    Alimento balanceado y de alta calidad.
    Cuidados específicos:
    Cepillado semanal y ejercicio regular.
    Consejos:
    Requieren entrenamiento firme pero positivo.
    """,
    "Bulldog": """
    Alimentación:
    Dieta controlada para evitar el sobrepeso.
    Cuidados específicos:
    Limpieza regular de las arrugas faciales y cuidado de su piel.
    Consejos:
    Ejercicio moderado debido a su tendencia a sufrir problemas respiratorios.
    """,
    "Chihuahua": """
    Alimentación:
    Comida especial para razas pequeñas, en porciones controladas.
    Cuidados específicos:
    Abrigo en climas fríos y revisión dental regular.
    Consejos:
    Socialización temprana para evitar problemas de comportamiento.
    """,
    "Chow Chow": """
    Alimentación:
    Dieta balanceada y de alta calidad.
    Cuidados específicos:
    Cepillado regular debido a su denso pelaje.
    Consejos:
    Requieren entrenamiento firme y socialización temprana.
    """,
    "Dálmata": """
    Alimentación:
    Dieta rica en proteínas y bajo en purinas para evitar problemas renales.
    Cuidados específicos:
    Ejercicio regular y cuidado de su piel.
    Consejos:
    Son muy activos y necesitan mucho ejercicio y estímulo mental.
    """,
    "Doberman": """
    Alimentación:
    Dieta rica en proteínas y nutrientes esenciales.
    Cuidados específicos:
    Ejercicio intenso y revisiones veterinarias regulares.
    Consejos:
    Requieren entrenamiento y socialización desde temprana edad.
    """,
    "German Shepherd": """
    Alimentación:
    Dieta de alta calidad con proteínas adecuadas para su tamaño y actividad.
    Cuidados específicos:
    Cepillado regular y ejercicio intenso.
    Consejos:
    Son muy inteligentes y necesitan entrenamiento continuo.
    """,
    "Golden Retriever": """
    Alimentación:
    Comida rica en proteínas y grasas saludables.
    Cuidados específicos:
    Cepillado regular y ejercicio diario.
    Consejos:
    Son muy sociables y disfrutan de actividades con la familia.
    """,
    "Maltese": """
    Alimentación:
    Dieta especial para razas pequeñas, rica en nutrientes.
    Cuidados específicos:
    Cepillado diario y cuidado dental.
    Consejos:
    Necesitan compañía y no les gusta estar solos por mucho tiempo.
    """,
    "Newfoundland": """
    Alimentación:
    Alimento para razas grandes con contenido equilibrado de proteínas y grasas.
    Cuidados específicos:
    Cepillado regular y ejercicio moderado.
    Consejos:
    Son excelentes nadadores y disfrutan de actividades acuáticas.
    """,
    "Pekingese": """
    Alimentación:
    Comida para razas pequeñas, rica en nutrientes y en porciones controladas.
    Cuidados específicos:
    Cepillado regular y cuidado de los ojos.
    Consejos:
    Evitar el calor extremo debido a su estructura facial.
    """,
    "Pit Bull": """
    Alimentación:
    Dieta rica en proteínas y grasas saludables.
    Cuidados específicos:
    Ejercicio regular y chequeos veterinarios frecuentes.
    Consejos:
    Requieren socialización temprana y entrenamiento consistente.
    """,
    "Poodle": """
    Alimentación:
    Dieta balanceada con proteínas de alta calidad.
    Cuidados específicos:
    Cepillado y cortes de pelo regulares.
    Consejos:
    Son muy inteligentes y disfrutan de actividades mentales.
    """,
    "Pug": """
    Alimentación:
    Comida controlada en calorías para evitar el sobrepeso.
    Cuidados específicos:
    Limpieza de arrugas faciales y control de su respiración.
    Consejos:
    Ejercicio moderado y evitar el calor extremo.
    """,
    "Rottweiler": """
    Alimentación:
    Dieta rica en proteínas adecuada para razas grandes.
    Cuidados específicos:
    Ejercicio regular y chequeos de salud.
    Consejos:
    Requieren entrenamiento firme y socialización temprana.
    """,
    "Saint Bernard": """
    Alimentación:
    Alimento de alta calidad para razas gigantes.
    Cuidados específicos:
    Cepillado regular y ejercicio moderado.
    Consejos:
    Son propensos al calor, por lo que es mejor mantenerlos en climas frescos.
    """,
    "Samoyed": """
    Alimentación:
    Dieta equilibrada con un buen contenido de proteínas y grasas.
    Cuidados específicos:
    Cepillado diario debido a su pelaje denso.
    Consejos:
    Les encanta el ejercicio y son muy sociables.
    """,
    "Shih Tzu": """
    Alimentación:
    Comida especial para razas pequeñas, rica en nutrientes.
    Cuidados específicos:
    Cepillado diario y cuidado de los ojos.
    Consejos:
    Necesitan compañía y no les gusta estar solos por mucho tiempo.
    """,
    "Siberian Husky": """
    Alimentación:
    Dieta rica en proteínas y grasas saludables.
    Cuidados específicos:
    Ejercicio intenso y evitar climas cálidos.
    Consejos:
    Son muy activos y necesitan estímulo mental.
    """,
    "Staffordshire Bull Terrier": """
    Alimentación:
    Dieta balanceada con proteínas de alta calidad.
    Cuidados específicos:
    Ejercicio regular y socialización desde temprana edad.
    Consejos:
    Requieren entrenamiento consistente y positivo.
    """,
    "Yorkshire Terrier": """
    Alimentación:
    Comida especial para razas pequeñas, rica en nutrientes.
    Cuidados específicos:
    Cepillado diario y control dental regular.
    Consejos:
    Necesitan estímulo mental y socialización.
    """,
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
            st.markdown('<div class="info-box">Resultado</div>', unsafe_allow_html=True)
            image_file = Image.open(input_img)

            with st.spinner('Analizando imagen...'):
                label, confidence_score = classify_dog(image_file)
                if label is not None and confidence_score is not None:
                    label_description = label.split(maxsplit=1)[1].strip()  # To get breed name
                    st.session_state['label'] = label_description

                    if confidence_score < 0.6:
                        st.error("La confianza en la clasificación es baja. Por favor, adjunta otra foto.")
                    else:
                        st.success(f"Raza: {st.session_state['label']}")
                        st.write(f"Confianza: {confidence_score * 100:.2f}%")

                        # Mostrar recomendaciones si la confianza es alta
                        with st.container():
                            st.markdown('<div class="recommendations">', unsafe_allow_html=True)
                            st.markdown('<p>Recomendaciones</p>', unsafe_allow_html=True)
                            result = generate_recipe(label_description)
                            st.markdown(f"<div class='info-box'>{result}</div>", unsafe_allow_html=True)
                            st.markdown('</div>', unsafe_allow_html=True)
                            st.success("Recomendaciones generadas.")
                else:
                    st.error("No se pudo clasificar la raza del perro.")

        st.markdown('</div>', unsafe_allow_html=True)

# Botón de más recomendaciones
st.markdown('<div class="btn-box">', unsafe_allow_html=True)
st.markdown('<a href="#more-recommendations" class="more-btn">Más recomendaciones</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
