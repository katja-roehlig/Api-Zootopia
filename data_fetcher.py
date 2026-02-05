import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_animal_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
        ...
        },
        'locations': [
        ...
        ],
        'characteristics': {
        ...
        }
    },
    """
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}
    response = requests.get(url, headers=headers, params=params)
    animal_list = response.json()
    return animal_list
