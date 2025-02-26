import requests
from constants import BASE_URL, API_KEY


def search_movies(query):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={query}"
    response = requests.get(url).json()
    return response.get("results", [])
