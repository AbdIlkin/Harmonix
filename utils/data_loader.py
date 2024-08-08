import json

def load_concert_data(data_path='assets/concert_data.json'):
    """Load concert data from a JSON file."""
    with open(data_path, 'r', encoding='utf-8') as file:
        return json.load(file)
