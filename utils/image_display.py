import requests
from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st
from io import BytesIO

def display_image(image_url):
    """Display an image from a URL in Streamlit."""
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            fig, ax = plt.subplots()
            ax.imshow(img)
            ax.axis('off')
            st.pyplot(fig)
            plt.close(fig)
        else:
            st.warning("Image could not be retrieved.")
    except Exception as e:
        st.error(f"An error occurred while fetching the image: {e}")
