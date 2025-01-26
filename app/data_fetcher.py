import requests

def fetch_json_data(url):
    return requests.get(url).json()
