import google.generativeai as genai
import os
import json

# Load API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the prompt template
prompt_template = """
You are a helpful assistant that provides information about concerts. Based on the given data and user query, respond appropriately. When the user wants to find the concerts by time, please enhance sentences. Then when the user asks for more detailed information about the concert, please give the image URL and additional text.
Please print the URL as "[Second Image]: url". You replace url with given concerts URLs. Only once time give url on given concert. If user ask location, price, and time dont give the url. If user ask pricing give the web_page_url.

Data: {data}

Conversation History:
{history}

User Query: {text}

Response:
"""

def get_gemini_response(user_query, concert_data, conversation_history):
    """Generate a response from the Gemini model."""
    input_text = prompt_template.format(
        history="\n".join(conversation_history),
        data=json.dumps(concert_data, ensure_ascii=False),
        text=user_query
    )
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input_text)
    return response.text.strip()
