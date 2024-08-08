# Harmonix Chatbot 🎤

## Overview

**Harmonix Chatbot** is an interactive Streamlit application that provides users with detailed information about concerts. The chatbot utilizes AI (via Google’s Gemini model) to answer user queries about concerts, including dates, venues, prices, and more. The project also includes a web scraping module to collect concert data from the iTicket website.

## Features

- **Conversational AI**: Chat with the Harmonix Chatbot to get detailed concert information.
- **Image Display**: View images of the concert venue or event as part of the chatbot response.
- **Web Scraping**: Automated scraping of concert data from the iTicket website.
- **Dynamic Data Loading**: The chatbot uses up-to-date concert information stored in a JSON file.
- **Session Management**: Maintains conversation history within the session.

## Project Structure

- harmonix_chatbot/
    - app.py                      # Main application code
    - utils/
        - data_loader.py          # Functions for loading concert data
        - image_display.py        # Functions for displaying images
        - ai_response.py          # Functions to interact with AI model
        - scraper.py              # Web scraping module
    - assets/
        - complete_urls.txt       # Scraped URLs of concert events
        - concert_data.json       # JSON file containing scraped concert data
    - .env                        # Environment variables (e.g., API keys)
    - requirements.txt            # Python dependencies
    - README.md                   # Project documentation


## Getting Started

### Prerequisites

- Python 3.8+
- Google Gemini API Key (for generating AI responses)
- Chrome WebDriver (for web scraping)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AbdIlkin/ResuMatch.git
    cd ResuMatch
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```
### Scraping Concert Data

Before running the chatbot, you need to scrape the concert data:

1. **Run the web scraping script**:
    ```bash
    python utils/scraper.py
    ```
   This script will generate `complete_urls.txt` with event URLs and `concert_data.json` with detailed concert information.

### Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

## Usage

- Enter your queries about concerts (e.g., “Show me the concerts in September”) into the chatbot.
- The chatbot will respond with relevant concert details, including images and additional information.
- You can also ask for specific details such as location, price, or time.

## Project Modules

### `app.py`
- The main entry point of the Streamlit application.
- Handles user interaction and integrates AI responses.

### `utils/scraper.py`
- Scrapes event links and concert details from the iTicket website.
- Saves the scraped data into JSON format for use by the chatbot.

### `utils/data_loader.py`
- Loads concert data from the JSON file.

### `utils/image_display.py`
- Contains functions to display images within the Streamlit app.

### `utils/ai_response.py`
- Handles interaction with the Google Gemini AI model to generate responses.

## Future Enhancements

- Implement additional languages for broader user accessibility.
- Add more sophisticated NLP techniques for better understanding of user queries.
- Enhance the UI/UX of the Streamlit app.

"# Harmonix" 
