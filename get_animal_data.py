import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_animal_data(animal):
    url = f"https://api.api-ninjas.com/v1/animals?name={animal}"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
