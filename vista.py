from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import os
from openai import OpenAI

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(_file_))

def classify_dog(img):
    np.set_printoptions(suppress=True)
    model_path = os.path.join(script_dir, "..", "modelo", "keras_model.h5")
    if not os.path.exists(model_path):
        st.error(f"Model file not found at {model_path}")
        return None, None

    model = load_model(model_path, compile=False)
    labels_path = os.path.join(script_dir, "..", "modelo", "labels.txt")
    if not os.path.exists(labels_path):
        st.error(f"Labels file not found at {labels_path}")
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

#chat
def generate_recipe(label):
    client = OpenAI(api_key="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") #borre api key

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"sos un experto en animales, especialmente en perros y tenes que recomendar a la persona que publique la imagen de su perro recomendaciones personalizadas dependiendo de la raza del perro que se clasifica como {label} brindandole consejos realmente utiles como por ejemlo que alimentación darle incluyendo marcas, actividad fisica, problemas comunes de la raza, y toda la info que consideres relevante",
        temperature=0.5,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text


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
        justify-content: space-around;
        margin-top: 20px;
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
st.markdown('<h1 class="title">DogBreeds Detector</h1>', unsafe_allow_html=True)


# "Comienza tu aventura" section
st.markdown('<h2 class="subtitle">Comienza tu aventura junto con tu mascota</h2>', unsafe_allow_html=True)

# Upload box
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
input_img = st.file_uploader("", type=['jpg', 'png', 'jpeg'])
st.markdown('</div>', unsafe_allow_html=True)

# Button box
st.markdown('<div class="btn-box">', unsafe_allow_html=True)
if input_img is not None:
    if st.button("Determinar la raza y obtener recomendaciones personalizadas"):
        # Columns for displaying results
        st.markdown('<div class="columns">', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.markdown('<div class="info-box">Imagen cargada</div>', unsafe_allow_html=True)
            st.image(input_img, use_column_width=True)

        with col2:
            st.markdown('<div class="info-box">Resultado</div>', unsafe_allow_html=True)
            image_file = Image.open(input_img)

            with st.spinner('Analizando imagen...'):
                label, confidence_score = classify_dog(image_file)
                if label is not None and confidence_score is not None:
                    label_description = label.split(maxsplit=1)[1].strip()  # To get breed name
                    st.session_state['label'] = label_description

                    st.success(f"Raza: {st.session_state['label']}")
                    st.write(f"Confianza: {confidence_score * 100:.2f}%")
                else:
                    st.error("No se pudo clasificar la raza del perro.")

        with col3:
            st.markdown('<div class="info-box">Recomendaciones</div>', unsafe_allow_html=True)
            if label is not None:
                result = generate_recipe(label_description)
                
                st.markdown(f"<div class='info-box'>{result}</div>", unsafe_allow_html=True)
               
                st.success(result)

        st.markdown('</div>', unsafe_allow_html=True)