import streamlit as st

# Inicializar la sesión
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

if 'input' not in st.session_state:
    st.session_state['input'] = ""

def add_message():
    user_input = st.session_state['input']
    if user_input:
        # Añadir mensaje del usuario
        st.session_state['messages'].append({"role": "user", "content": user_input})
        
        # Generar y añadir respuesta
        response = generate_response(user_input)
        st.session_state['messages'].append({"role": "bot", "content": response})
        
        # Limpiar el campo de texto
        st.session_state['input'] = ""

def generate_response(user_input):
    # Aquí puedes implementar la lógica para generar respuestas
    # Por ahora, simplemente devolveremos un mensaje fijo
    return f"Has preguntado: {user_input}"

# Configuración de la interfaz
st.set_page_config(page_title="Chat Empresarial", page_icon=":speech_balloon:")

st.markdown("""
    <style>
    body {
        background-color: #f4f4f9;
    }
    .chat-container {
        max-width: 700px;
        margin: auto;
        padding: 20px;
        border: 2px solid #d3d3d3;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .user-message {
        background-color: #c2f9bb;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        text-align: right;
        font-size: 16px;
        border: 1px solid #a4e57e;
        color: #333;
    }
    .bot-message {
        background-color: #e1e1e1;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        text-align: left;
        font-size: 16px;
        border: 1px solid #d3d3d3;
        color: #333;
    }
    .title {
        text-align: center;
        color: #333;
        font-size: 36px;
        margin-bottom: 10px;
    }
    .input-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 20px;
    }
    .input-container input {
        width: 80%;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #d3d3d3;
        font-size: 16px;
    }
    .input-container button {
        width: 18%;
        padding: 10px;
        border-radius: 5px;
        border: none;
        background-color: #4caf50;
        color: white;
        font-size: 16px;
        cursor: pointer;
    }
    .input-container button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">Chat Empresarial</h1>', unsafe_allow_html=True)

# Contenedor principal del chat
with st.container():

    # Mostrar la conversación
    for message in st.session_state['messages']:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message"><b>Tú:</b> {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message"><b>Bot:</b> {message["content"]}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Contenedor para la entrada del usuario y el botón de envío
with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    # Obtener la entrada del usuario
    st.text_input("Escribe tu mensaje aquí:", key='input', placeholder="Escribe tu mensaje...", on_change=add_message)
    
    # Botón para enviar el mensaje
    if st.button("Enviar"):
        add_message()

    st.markdown('</div>', unsafe_allow_html=True)





