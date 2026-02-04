import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_user_choice():
    user_choice = input("Enter a name of an animal: ")
    return user_choice.lower()


def get_animal_data():
    animal = get_user_choice()
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal}
    response = requests.get(url, headers=headers, params=params)
    animal_list = response.json()
    return animal_list, animal
