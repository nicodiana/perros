import streamlit as st
from datetime import datetime, timedelta
import json

# Configuración de página y estilos CSS personalizados
st.set_page_config(
    page_title="DOGGYS",
    page_icon=":dog:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Función para guardar la historia clínica en el almacenamiento de sesión
def save_history(data):
    st.session_state.history = data

# Función para cargar la historia clínica desde el almacenamiento de sesión
def load_history():
    if "history" not in st.session_state:
        st.session_state.history = []
    return st.session_state.history

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

# Espacio para cargar logo
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
    .chat-box {
        max-height: 300px;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #fafafa;
    }
    .chat-message {
        padding: 5px 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 70%;
    }
    .chat-message.user {
        background-color: #d1e7dd;
        align-self: flex-end;
    }
    .chat-message.bot {
        background-color: #f8d7da;
        align-self: flex-start;
    }
    .history-box {
        max-height: 400px;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #fafafa;
    }
    .history-item {
        padding: 5px 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        background-color: #d1e7dd;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sección de registro/login para usuarios premium
st.markdown("---")
st.markdown("## Funcionalidades Exclusivas para Usuarios Premium")

# Formulario de inicio de sesión/registro
st.markdown("### Registro/Login de Usuarios Premium")
username = st.text_input("Nombre de usuario")
password = st.text_input("Contraseña", type="password")

# Simulación de autenticación
if st.button("Iniciar sesión / Registrarse"):
    if username and password:
        st.success("Inicio de sesión/Registro exitoso.")
        st.session_state.is_premium = True
    else:
        st.error("Por favor, ingrese su nombre de usuario y contraseña.")
        st.session_state.is_premium = False

# Verificar si el usuario es premium
is_premium = st.session_state.get("is_premium", False)

if is_premium:
    st.markdown("### Comunícate ahora con un Veterinario")
    st.write("Como usuario premium, puedes comunicarte en tiempo real con nuestros veterinarios expertos.")

    # Botón para iniciar chat con veterinario
    if st.button("Iniciar Chat con Veterinario"):
        st.session_state.show_chat = True

    if st.session_state.get("show_chat", False):
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = [
                {"sender": "bot", "message": "Bienvenido al chat. Te estamos contactando con un veterinario cerca de tu zona."}
            ]

        def add_message(sender, message):
            st.session_state.chat_history.append({"sender": sender, "message": message})

        st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
        for chat in st.session_state.chat_history:
            sender_class = "user" if chat["sender"] == "user" else "bot"
            st.markdown(f"<div class='chat-message {sender_class}'>{chat['message']}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        user_message = st.text_input("Escribe tu mensaje aquí...")
        if st.button("Enviar Mensaje"):
            if user_message:
                add_message("user", user_message)
                add_message("bot", "Un veterinario está respondiendo a tu consulta...")

        # Subir fotos para el chat
        st.markdown("#### Adjuntar Fotos")
        uploaded_files = st.file_uploader("Selecciona una o varias fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
        if uploaded_files:
            for uploaded_file in uploaded_files:
                st.image(uploaded_file, caption="Foto subida", use_column_width=True)
                add_message("user", "Foto adjunta.")

        # Subir videos para el chat
        st.markdown("#### Adjuntar Videos")
        uploaded_videos = st.file_uploader("Selecciona uno o varios videos", type=["mp4", "mov", "avi"], accept_multiple_files=True)
        if uploaded_videos:
            for uploaded_video in uploaded_videos:
                st.video(uploaded_video)
                add_message("user", "Video adjunto.")

    st.markdown("---")

    st.markdown("### Videos Exclusivos de Entrenamiento de Perro")
    st.write("Accede a nuestros videos exclusivos de entrenamiento para tu perro.")
    video_urls = [
        "https://www.youtube.com/watch?v=video_id_1",  # Reemplazar con URLs reales de videos
        "https://www.youtube.com/watch?v=video_id_2",
        "https://www.youtube.com/watch?v=video_id_3"
    ]
    
    for video_url in video_urls:
        st.video(video_url)

    st.markdown("---")

    # Sección para agregar eventos al historial clínico
    st.markdown("### Historial Clínico y Calendario de Salud")
    st.write("Lleva un registro de la salud de tu perro, incluyendo vacunas, enfermedades, controles médicos, y más.")

    # Cargar historial clínico
    history = load_history()

    # Mostrar historial clínico
    st.markdown("<div class='history-box'>", unsafe_allow_html=True)
    for event in history:
        st.markdown(f"<div class='history-item'>{event['date']}: {event['event']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Formulario para agregar nuevos eventos
    st.markdown("#### Agregar nuevo evento")
    event_date = st.date_input("Fecha del evento")
    event_description = st.text_input("Descripción del evento")

    if st.button("Agregar Evento"):
        if event_date and event_description:
            new_event = {
                "date": event_date.strftime("%Y-%m-%d"),
                "event": event_description
            }
            history.append(new_event)
            save_history(history)
            st.success("Evento agregado exitosamente.")
        else:
            st.error("Por favor, complete todos los campos.")

else:
    st.write("Para acceder a las funcionalidades premium, por favor inicia sesión o regístrate.")

import streamlit as st
from datetime import datetime
import json

# Función para guardar publicaciones de la comunidad en el almacenamiento de sesión
def save_community_posts(data):
    st.session_state.community_posts = data

# Función para cargar publicaciones de la comunidad desde el almacenamiento de sesión
def load_community_posts():
    if "community_posts" not in st.session_state:
        st.session_state.community_posts = []
    return st.session_state.community_posts

# Estilos CSS personalizados
st.markdown(
    """
    <style>
    .community-box {
        max-height: 600px;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #fafafa;
        margin-bottom: 20px;
    }
    .community-post {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
        background-color: #d1e7dd;
    }
    .community-post img {
        max-width: 100%;
        border-radius: 10px;
    }
    .community-post .user {
        font-weight: bold;
        margin-bottom: 5px;
    }
    .community-post .date {
        color: #555;
        font-size: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("# Comunidad")
st.write("Comparte tus experiencias, haz preguntas, da consejos y sube fotos de tus perros.")

# Verificar si el usuario es premium
is_premium = st.session_state.get("is_premium", False)

if is_premium:
    # Cargar publicaciones de la comunidad
    community_posts = load_community_posts()

    # Mostrar publicaciones de la comunidad
    st.markdown("<div class='community-box'>", unsafe_allow_html=True)
    for post in community_posts:
        st.markdown(
            f"""
            <div class='community-post'>
                <div class='user'>{post['username']}</div>
                <div class='date'>{post['date']}</div>
                <div class='message'>{post['message']}</div>
                {'<img src="' + post['image'] + '">' if post['image'] else ''}
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # Formulario para agregar nuevas publicaciones
    st.markdown("## Nueva Publicación")
    username = st.text_input("Nombre de usuario", key="community_username")
    message = st.text_area("Mensaje", key="community_message")
    uploaded_image = st.file_uploader("Subir imagen", type=["jpg", "jpeg", "png"], key="community_image")

    if st.button("Publicar", key="community_publish"):
        if username and message:
            new_post = {
                "username": username,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "message": message,
                "image": None
            }
            if uploaded_image:
                new_post["image"] = f"data:image/jpeg;base64,{uploaded_image.read().decode('utf-8')}"
            
            community_posts.append(new_post)
            save_community_posts(community_posts)
            st.success("Publicación agregada exitosamente.")
            st.experimental_rerun()
        else:
            st.error("Por favor, complete todos los campos.")
else:
    st.error("Para acceder a la comunidad, por favor inicia sesión o regístrate como usuario premium.")