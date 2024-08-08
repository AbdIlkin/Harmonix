import streamlit as st
from streamlit_chat import message
from utils.data_loader import load_concert_data
from utils.image_display import display_image
from utils.ai_response import get_gemini_response
import os

# Load concert data
concerts_data = load_concert_data()

# Streamlit session state initialization
if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello! Ask me anything about the concerts."]

if 'past' not in st.session_state:
    st.session_state['past'] = ["Hey! 👋"]

# Main conversation function
def conversational_chat(query):
    history = st.session_state['history']
    
    # Handle exit commands
    if query.lower() in ["bye", "exit", "quit"]:
        response = "Goodbye! If you have more questions later, feel free to ask."
        st.session_state['history'].append(f"User: {query}")
        st.session_state['history'].append(f"Bot: {response}")
        st.stop()

    # Generate AI response
    response = get_gemini_response(query, concerts_data, history)
    
    # Extract image URL if present
    image_url = None
    if '[Second Image]:' in response:
        image_url = response.split('[Second Image]:')[-1].strip()
        response = response.replace(f'[Second Image]: {image_url}', '').strip()
    
    st.session_state['history'].append(f"User: {query}")
    st.session_state['history'].append(f"Bot: {response}")
    
    return response, image_url

# Streamlit layout
st.title("Harmonix Chatbot 🎤")

response_container = st.container()
input_container = st.container()

# User input form
with input_container:
    with st.form(key='input_form', clear_on_submit=True):
        user_input = st.text_input("Query:", placeholder="Ask about concerts here", key='input')
        submit_button = st.form_submit_button(label='Send')
        
    if submit_button and user_input:
        output, image_url = conversational_chat(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

# Display chat messages and images
if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            if i < len(st.session_state['past']):
                message(st.session_state["past"][i], is_user=True, key=f"{i}_user", avatar_style="big-smile")
            message(st.session_state["generated"][i], key=f"{i}", avatar_style="thumbs")
            
            # Display image if available and it's the latest message
            if i == len(st.session_state['generated']) - 1 and image_url:
                display_image(image_url)
